"""
Equilibrium utilities library
"""

import sys, time
import numpy as np
from scipy.ndimage.interpolation import map_coordinates
from scipy.interpolate import UnivariateSpline, interp1d, InterpolatedUnivariateSpline, RectBivariateSpline
try:
    from . import cocos
except:
    import cocos

def get_nearest_index(tim_eq, tarr):
    """Find nearest time idnex for a given time"""

    tarr = np.minimum(np.maximum(tarr, tim_eq[0]), tim_eq[-1])
    if len(tim_eq) == 1:
        idx = 0
    else:
        idx = interp1d(tim_eq, np.arange(len(tim_eq)), kind='nearest')(tarr)
    idx = np.atleast_1d(np.int_(idx))
    unique_idx = np.unique(idx)

    return unique_idx, idx


def rho2rho(eqsf, rho_in, t_in=None, \
           coord_in='rho_pol', coord_out='rho_tor', extrapolate=False):

    """Mapping from/to rho_pol, rho_tor, r_V, rho_V, Psi, r_a
    r_V is the STRAHL-like radial coordinate

    Input
    ----------
    t_in : float or 1darray
        time
    rho_in : float, ndarray
        radial coordinates, 1D (time constant) or 2D+ (time variable) of size (nt,nx,...)
    coord_in:  str ['rho_pol', 'rho_tor' ,'rho_V', 'r_V', 'Psi','r_a']
        input coordinate label
    coord_out: str ['rho_pol', 'rho_tor' ,'rho_V', 'r_V', 'Psi','r_a']
        output coordinate label
    extrapolate: bool
        extrapolate rho_tor, r_V outside the separatrix

    Output
    -------
    rho : 2d+ array (nt, nr, ...)
    converted radial coordinate
    """

    if t_in is None:
        t_in = eqsf.time

    tarr = np.atleast_1d(t_in)
    rho = np.atleast_1d(rho_in)

    nt_in = np.size(tarr)

    if rho.ndim == 1:
        rho = np.tile(rho, (nt_in, 1))

# Trivial case
    if coord_out == coord_in: 
        return rho
 
    unique_idx, idx =  get_nearest_index(eqsf.time, tarr)

    if coord_in in ['rho_pol', 'Psi']:
        label_in = eqsf.pfl
    elif coord_in == 'rho_tor':
        label_in = eqsf.tfl
    elif coord_in in ['rho_V','r_V']:
        label_in = eqsf.vol
        R0 = eqsf.Rmag
    elif coord_in == 'r_a':
        R, _ = rhoTheta2rz(eqsf, eqsf.pfl, [0, np.pi], coord_in='Psi')
        label_in = (R[:, 0] - R[:, 1]).T**2
    else:
        raise Exception('unsupported input coordinate')

    if coord_out in ['rho_pol', 'Psi']:
        label_out = eqsf.pfl
    elif coord_out == 'rho_tor':
        label_out = eqsf.tfl
    elif coord_out in ['rho_V','r_V']:
        label_out = eqsf.vol
        R0 = eqsf.Rmag
    elif coord_out == 'r_a':
        R, _ = rhoTheta2rz(eqsf, eqsf.pfl[unique_idx], [0, np.pi], \
                    t_in=eqsf.time[unique_idx], coord_in='Psi')
        label_out = np.zeros_like(eqsf.pfl)
        label_out[unique_idx, :] = (R[:, 0] - R[:, 1])**2
    else:
        raise Exception('unsupported output coordinate')

    PFL  = eqsf.orientation*eqsf.pfl
    PSIX = eqsf.orientation*eqsf.psix
    PSI0 = eqsf.orientation*eqsf.psi0
    rho_output = np.zeros_like(rho)

    for i in unique_idx:
  
# Calculate a normalized input and output flux 
#            sort_wh = eqsf.ind_sort[i][:eqsf.lpfp[i]]    # Up to separatrix   

        sep_out, mag_out = np.interp([PSIX[i], PSI0[i]], PFL[i], label_out[i])
        sep_in , mag_in  = np.interp([PSIX[i], PSI0[i]], PFL[i], label_in [i])

        if (abs(sep_out - mag_out) < 1e-4) or (abs(sep_in - mag_in) < 1e-4): #corrupted timepoint
            continue

# Normalize between 0 and 1
        rho_out = (label_out[i] - mag_out)/(sep_out - mag_out)
        rho_in  = (label_in [i] - mag_in )/(sep_in  - mag_in )

        rho_out[(rho_out > 1) | (rho_out < 0)] = 0  #remove rounding errors
        rho_in[ (rho_in  > 1) | (rho_in  < 0)] = 0

        rho_out = np.r_[np.sqrt(rho_out), 1]
        rho_in  = np.r_[np.sqrt(rho_in ), 1]

        ind = (rho_out==0) | (rho_in==0)
        rho_out, rho_in = rho_out[~ind], rho_in[~ind]
        
# Profiles can be noisy!  smooth spline must be used
        sortind = np.unique(rho_in, return_index=True)[1]
        w = np.ones_like(sortind)*rho_in[sortind]
        w = np.r_[w[1]/2, w[1:], 1e3]
        ratio = rho_out[sortind]/rho_in[sortind]
        rho_in = np.r_[0, rho_in[sortind]]
        ratio = np.r_[ratio[0], ratio]

        s = UnivariateSpline(rho_in, ratio, w=w, k=4, s=5e-3,ext=3)  #BUG s = 5e-3 can be sometimes too much, sometimes not enought :( 

        if len(idx) == 1:
            jt = 0
        else:
            jt = idx == i

        rho_ = np.copy(rho[jt])

        r0_in = 1
        if coord_in == 'r_V' :
            r0_in  = np.sqrt(sep_in/ (2*np.pi**2*R0[i]))
        r0_out = 1
        if coord_out == 'r_V' :
            r0_out = np.sqrt(sep_out/(2*np.pi**2*R0[i]))

        if coord_in == 'Psi' :
            rho_  = np.sqrt(np.maximum(0, (rho_ - eqsf.psi0[i])/(eqsf.psix[i] - eqsf.psi0[i])))

# Evaluate spline

        rho_output[jt] = s(rho_.flatten()/r0_in).reshape(rho_.shape)*rho_*r0_out/r0_in

        if np.any(np.isnan(rho_output[jt])):  # UnivariateSpline failed
            rho_output[jt] = np.interp(rho_/r0_in, rho_in, ratio)*rho_*r0_out/r0_in
            
        if not extrapolate:
            rho_output[jt] = np.minimum(rho_output[jt],r0_out) # rounding errors

        rho_output[jt] = np.maximum(0,rho_output[jt]) # rounding errors

        if coord_out  == 'Psi':
            rho_output[jt]  = rho_output[jt]**2*(eqsf.psix[i] - eqsf.psi0[i]) + eqsf.psi0[i]
    
    return rho_output


def rz2brzt(eqsf, r_in, z_in, t_in=None):

    """calculates Br, Bz, Bt profiles
    Input
    ----------
    r_in : ndarray
        R coordinates 
        1D, size(nrz_in) or 2D, size (nt, nrz_in)
    z_in : ndarray
        Z coordinates 
        1D, size(nrz_in) or 2D, size (nt, nrz_in)
    t_in : float or 1darray
        time
        If t_in=None, take the whole time array from the shotfile

    Output
    -------
    interpBr : ndarray
        profile of Br(nt, nrz_in)
    interpBz : ndarray
        profile of Bz(nt, nrz_in)
    interpBt : ndarray
        profile of Bt(nt, nrz_in)
    """

    if t_in is None:
        t_in = eqsf.time
        
    tarr = np.atleast_1d(t_in)
    r_in = np.atleast_1d(r_in)
    z_in = np.atleast_1d(z_in)

    nt = np.size(tarr)
    nrz_in = r_in.shape[-1]

    if r_in.shape != z_in.shape:
        print('r_in and z_in must have the same shape')
        return

    if r_in.ndim == 2 and r_in.shape[0] != nt:
        print('Time array missmatching first dim of r_in')
        return

    if np.size(r_in, 0)!= nt:
        r_in = np.tile(r_in, nt).reshape((nt, nrz_in))
        z_in = np.tile(z_in, nt).reshape((nt, nrz_in))

    interpBr = np.zeros((nt, nrz_in), dtype=np.float32)
    interpBz = np.zeros((nt, nrz_in), dtype=np.float32)
    interpBt = np.zeros((nt, nrz_in), dtype=np.float32)

    from scipy.constants import mu_0
    nr, nz = len(eqsf.Rmesh), len(eqsf.Zmesh)
    dr = (eqsf.Rmesh[-1] - eqsf.Rmesh[0])/float(nr - 1)
    dz = (eqsf.Zmesh[-1] - eqsf.Zmesh[0])/float(nz - 1)

# COCOS, Eq. 19, 24
    cocos_in = eqsf.cocos
    jc_in    = cocos_in%10 - 1
    ebp_in   = cocos_in//10
    sign_ip  = np.sign(np.nanmean(eqsf.ipipsi))
    sign_b0  = np.sign(np.nanmean(eqsf.jpol))
    sigma_ip = sign_ip*cocos.sigma['rphiz'][jc_in]
    sigma_b0 = sign_b0*cocos.sigma['rphiz'][jc_in]
    phi_sign = sigma_b0
    psi_sign = sigma_ip*cocos.sigma['bp'][jc_in]
    psi_2pi  = (2.*np.pi)**ebp_in
    psi_fac = psi_sign*psi_2pi
    print('COCOS %d, Sign Bt %d, Sign Ip %d' %(cocos_in, sign_b0, sign_ip))

    unique_idx, idx =  get_nearest_index(eqsf.time, tarr)

    for i in unique_idx:

        jt = (idx == i)
        Psi = eqsf.pfm[:, :, i]
        Br =  np.gradient(Psi, axis=1)/eqsf.Rmesh[:, None]
        Bz = -np.gradient(Psi, axis=0)/eqsf.Rmesh[:, None]
        fBt = interp1d(eqsf.pfl[i], eqsf.jpol[i], kind='linear', fill_value='extrapolate')
        Bt = fBt(Psi)*mu_0/eqsf.Rmesh[:, None]
        r = np.squeeze(r_in[jt])
        z = np.squeeze(z_in[jt])
        f_br = RectBivariateSpline(eqsf.Rmesh, eqsf.Zmesh, Br, kx=2, ky=2)
        f_bz = RectBivariateSpline(eqsf.Rmesh, eqsf.Zmesh, Bz, kx=2, ky=2)
        f_bt = RectBivariateSpline(eqsf.Rmesh, eqsf.Zmesh, Bt, kx=2, ky=2)
        interpBr[jt] = f_br(r, z, grid=False)
        interpBz[jt] = f_bz(r, z, grid=False)
        interpBt[jt] = f_bt(r, z, grid=False)

    return interpBr/(psi_fac*dz), \
           interpBz/(psi_fac*dr), \
           np.abs(interpBt)/psi_2pi * phi_sign


def Bmesh(eqsf, t_in=None):

    """calculates Br, Bz, Bt profiles
    Input
    ----------
    t_in : float or 1darray
        time

    Output
    -------
    Br : ndarray
        profile of Br on the PFM grid
    Bz : ndarray
        profile of Bz on the PFM grid
    interpBt : ndarray
        profile of Bt on the PFM grid
    """

    if t_in is None:
        t_in = eqsf.time

    tarr = np.atleast_1d(t_in)
    nt = len(tarr)

# Poloidal current 

    from scipy.constants import mu_0

    nr = len(eqsf.Rmesh)
    nz = len(eqsf.Zmesh)
    dr = (eqsf.Rmesh[-1] - eqsf.Rmesh[0])/float(nr - 1)
    dz = (eqsf.Zmesh[-1] - eqsf.Zmesh[0])/float(nz - 1)

# COCOS, Eq. 24
    cocos_in = eqsf.cocos
    jc_in    = cocos_in%10 - 1
    ebp_in   = cocos_in//10
    sign_ip  =  eqsf.orientation
    sign_b0  = -eqsf.orientation
    sigma_ip = sign_ip*cocos.sigma['rphiz'][jc_in]
    sigma_b0 = sign_b0*cocos.sigma['rphiz'][jc_in]
    phi_sign = sigma_b0
    psi_sign = cocos.sigma['bp'][jc_in]
    psi_2pi  = (2.*np.pi)**ebp_in
    psi_fac = psi_sign*psi_2pi
    print('COCOS %d' %cocos_in)

    unique_idx, idx =  get_nearest_index(eqsf.time, tarr)

    Br = np.zeros((nt, nr, nz), dtype=np.float32)
    Bz = np.zeros_like(Br)
    Bt = np.zeros_like(Br)
    for i in unique_idx:

        jt = (idx == i)
        Psi = eqsf.pfm[:, :, i]
# Eq 12 in COCOs paper
        Br[jt] = np.gradient(Psi, axis=1)/eqsf.Rmesh[:, None]
        Bz[jt] = -np.gradient(Psi, axis=0)/eqsf.Rmesh[:, None]
        fBt = interp1d(eqsf.pfl[i], eqsf.jpol[i], kind='linear', fill_value='extrapolate')
        Bt[jt] = fBt(Psi)*mu_0/eqsf.Rmesh[:, None]

    return Br/(psi_fac*dz), \
           Bz/(psi_fac*dr), \
           Bt/psi_2pi * phi_sign


def rz2rho(eqsf, r_in, z_in, t_in=None, coord_out='rho_pol', extrapolate=True):

    """
    Equilibrium mapping routine, map from R,Z -> rho (pol,tor,r_V,...)
    Fast for a large number of points

    Input
    ----------
    t_in : float or 1darray
        time
    r_in : ndarray
        R coordinates 
        1D (time constant) or 2D+ (time variable) of size (nt,nx,...)
    z_in : ndarray
        Z coordinates 
        1D (time constant) or 2D+ (time variable) of size (nt,nx,...)
    coord_out: str
        mapped coordinates - rho_pol,  rho_tor, r_V, rho_V, Psi
    extrapolate: bool
        extrapolate coordinates (like rho_tor) for values larger than 1

    Output
    -------
    rho : 2D+ array (nt,nx,...)
    Magnetics flux coordinates of the points
    """

    if t_in is None:
        t_in = eqsf.time

    tarr = np.atleast_1d(t_in)
    r_in = np.atleast_2d(r_in)
    z_in = np.atleast_2d(z_in)

    dr = (eqsf.Rmesh[-1] - eqsf.Rmesh[0])/(len(eqsf.Rmesh) - 1)
    dz = (eqsf.Zmesh[-1] - eqsf.Zmesh[0])/(len(eqsf.Zmesh) - 1)

    nt_in = np.size(tarr)

    if np.size(r_in, 0) == 1:
        r_in = np.tile(r_in, (nt_in, 1))
    if np.size(z_in, 0) == 1:
        z_in = np.tile(z_in, (nt_in, 1))

    if r_in.shape!= z_in.shape:
        raise Exception('Wrong shape of r_in or z_in')
    
    if np.size(r_in,0) != nt_in:
        raise Exception('Wrong shape of r_in %s, nt=%d' %(str(r_in.shape), nt_in))
    if np.size(z_in,0) != nt_in:
        raise Exception('Wrong shape of z_in %s, nt=%d' %(str(z_in.shape), nt_in))
    if np.shape(r_in) != np.shape(z_in):
        raise Exception( 'Not equal shape of z_in and r_in %s,%s'\
                        %(str(z_in.shape), str(z_in.shape)) )

    Psi = np.empty((nt_in,)+r_in.shape[1:], dtype=np.single)

    scaling = np.array([dr, dz])
    offset  = np.array([eqsf.Rmesh[0], eqsf.Zmesh[0]])
    
    unique_idx, idx =  get_nearest_index(eqsf.time, tarr)
  
    for i in unique_idx:
        if len(idx) == 1:
            jt = 0
        else:
            jt = idx == i
        coords = np.array((r_in[jt], z_in[jt]))
        index = ((coords.T - offset) / scaling).T
        Psi[jt] =  map_coordinates(eqsf.pfm[:, :, i], index, mode='nearest',
                                   order=2, prefilter=True)

    t1 = time.time()
    rho_out = rho2rho(eqsf, Psi, t_in=t_in, extrapolate=extrapolate, \
              coord_in='Psi', coord_out=coord_out)
    t2 = time.time()
    return rho_out


def rho2rz(eqsf, rho_in, t_in=None, coord_in='rho_pol', all_lines=False):

    """
    Get R, Z coordinates of a flux surfaces contours

    Input
    ----------

    t_in : float or 1darray
        time
    rho_in : 1darray,float
        rho coordinates of the searched flux surfaces
    coord_in: str
        mapped coordinates - rho_pol or rho_tor
    all_lines: bool:
        True - return all countours , False - return longest contour

    Output
    -------
    rho : array of lists of arrays [npoinst,2]
        list of times containg list of surfaces for different rho 
        and every surface is decribed by 2d array [R,Z]
    """

    if t_in is None:
        t_in = eqsf.time

    tarr  = np.atleast_1d(t_in)
    rhoin = np.atleast_1d(rho_in)

    rho_in = rho2rho(eqsf, rhoin, t_in=t_in, \
             coord_in=coord_in, coord_out='Psi', extrapolate=True )

    from matplotlib import _contour

    nr = len(eqsf.Rmesh)
    nz = len(eqsf.Zmesh)

    R, Z = np.meshgrid(eqsf.Rmesh, eqsf.Zmesh)
    Rsurf = np.empty(len(tarr), dtype='object')
    zsurf = np.empty(len(tarr), dtype='object')
    unique_idx, idx =  get_nearest_index(eqsf.time, tarr)

    for i in unique_idx:

        (jt, ) = np.where(idx == i)
        Flux = rho_in[jt[0]]
        
# matplotlib's contour creation
        try:
            cgen = _contour.QuadContourGenerator(R, Z, eqsf.pfm[:nr, :nz, i].T, None, True, 0)
        except Exception as e:
            print(R.shape, Z.shape, eqsf.pfm[:nr, :nz, i].T.shape)
            raise e 

        Rs_t = []
        zs_t = []

        for jfl, fl in enumerate(Flux):
            segs = cgen.create_contour(fl)
            n_segs = len(segs)
            if n_segs == 0:
                if fl == eqsf.psi0[i]:
                    Rs_t.append(np.atleast_1d(eqsf.Rmag[i]))
                    zs_t.append(np.atleast_1d(eqsf.Zmag[i]))
                else:
                    Rs_t.append(np.zeros(1))
                    zs_t.append(np.zeros(1))
                continue
            elif all_lines: # for open field lines
                line = np.vstack(segs)
            else:  #longest filed line, default
                line = []
                for l in segs:
                    if len(l) > len(line):
                        line = l

            R_surf, z_surf = list(zip(*line))
            R_surf = np.array(R_surf, dtype = np.float32)
            z_surf = np.array(z_surf, dtype = np.float32)
            if not all_lines:
                ind = (z_surf >= eqsf.Zunt[i])
                if len(ind) > 1:
                    R_surf = R_surf[ind]
                    z_surf = z_surf[ind]
            Rs_t.append(R_surf)
            zs_t.append(z_surf)
   
        for j in jt:
            Rsurf[j] = Rs_t
            zsurf[j] = zs_t

    return Rsurf, zsurf


def cross_surf(eqsf, rho=1., r_in=1.65, z_in=0, theta_in=0, t_in=None, coord_in='rho_pol'):

    """
    Computes intersections of a line with any flux surface.

    Input:
    ----------
    rho: float
        coordinate of the desired flux surface
    t_in: float or 1darray
        time point/array for the evaluation
    r_in: float
        R position of the point
    z_in: float
        z position of the point
    theta_in: float
        angle of the straight line with respect to horizontal-outward
    coord_in:  str ['rho_pol', 'rho_tor' ,'rho_V', 'r_V', 'Psi','r_a']
        input coordinate label

    Output:
    ----------
    Rout: 3darray size(nt, nx, 2)
        R-position of intersections
    zout: 3darray size(nt, nx, 2)
        z-position of intersections
    """

    if t_in is None:
        t_in = eqsf.time

    tarr = np.atleast_1d(t_in)
    rho  = np.float32(rho)
    r_in = np.float32(r_in)
    z_in = np.float32(z_in)

    unique_idx, idx = get_nearest_index(eqsf.time, tarr)

    line_m = 3. # line length: 6 m
    n_line = int(200*line_m) + 1 # 1 cm, but then there's interpolation!
    t = np.linspace(-line_m, line_m, n_line, dtype=np.float32)

    t1 = time.time()
    line_r = t*np.cos(theta_in) + r_in
    line_z = t*np.sin(theta_in) + z_in
    rho_line = rz2rho(eqsf, line_r, line_z, t_in=eqsf.time[unique_idx], \
                           coord_out=coord_in, extrapolate=True)

    t2 = time.time()
    if coord_in == 'Psi':
        rho_line *= eqsf.orientation
        rho      *= eqsf.orientation
    nt_in = len(tarr)
    Rout = np.zeros((nt_in, 2), dtype=np.float32)
    zout = np.zeros((nt_in, 2), dtype=np.float32)
    for i, ii in enumerate(unique_idx):
        if len(idx) == 1:
            jt = 0
        else:
            jt = idx == i
        ind_gt = (rho_line[i] > rho)
        ind_cross = [j for j, x in enumerate(np.diff(ind_gt)) if x]
        if len(ind_cross) > 2:
            print('More than 2 intersections, problems')
            zout[jt, :] = 0
            Rout[jt, :] = 0
            continue

        pos = 0
        for j in ind_cross:
            if rho_line[i, j + 1] > rho_line[i, j]:
                ind = [j, j + 1]
            else:
                ind = [j + 1, j]
            ztmp = np.interp(rho, rho_line[i, ind], line_z[ind])
            if ztmp >= eqsf.Zunt[ii] and ztmp <= eqsf.Zoben[ii]:
                zout[jt, pos] = ztmp
                Rout[jt, pos] = np.interp(rho, rho_line[i, ind], line_r[ind])
                pos += 1
    del line_r, line_z, rho_line

    return Rout, zout


def cross_sep(eqsf, r_in=1.65, z_in=0, theta_in=0, t_in=None):

    """
    Computes intersections of a line with any flux surface.

    Input:
    ----------
    t_in: float or 1darray
        time point/array for the evaluation
    r_in: float
        R position of the point
    z_in: float
        z position of the point
    theta_in: float
        angle of the straight line with respect to horizontal-outward

    Output:
    ----------
    Rout: 3darray size(nt, nx, 2)
        R-position of intersections
    zout: 3darray size(nt, nx, 2)
        z-position of intersections
    """

    if t_in is None:
        t_in = eqsf.time

    tarr = np.atleast_1d(t_in)
    r_in = np.float32(r_in)
    z_in = np.float32(z_in)

    unique_idx, idx = get_nearest_index(eqsf.time, tarr)

    line_m = 3. # line length: 6 m
    n_line = int(200*line_m) + 1 # 1 cm, but then there's interpolation!
    t = np.linspace(-line_m, line_m, n_line, dtype=np.float32)

    t1 = time.time()
    line_r = t*np.cos(theta_in) + r_in
    line_z = t*np.sin(theta_in) + z_in
    psi_line = rz2rho(eqsf, line_r, line_z, t_in=eqsf.time[unique_idx], \
                           coord_out='Psi', extrapolate=True)

    t2 = time.time()
    psi_line *= eqsf.orientation
    psi_sep = eqsf.pfl[:, max(eqsf.lpfp)]*eqsf.orientation
    nt_in = len(tarr)
    Rout = np.zeros((nt_in, 2), dtype=np.float32)
    zout = np.zeros((nt_in, 2), dtype=np.float32)
    for i, ii in enumerate(unique_idx):
        if len(idx) == 1:
            jt = 0
        else:
            jt = idx == i
        ind_gt = (psi_line[i] > psi_sep[ii])
        ind_cross = [j for j, x in enumerate(np.diff(ind_gt)) if x]
        if len(ind_cross) > 2:
            print('More than 2 intersections, problems')
            zout[jt, :] = 0
            Rout[jt, :] = 0
            continue

        pos = 0
        for j in ind_cross:
            if psi_line[i, j + 1] > psi_line[i, j]:
                ind = [j, j + 1]
            else:
                ind = [j + 1, j]
            ztmp = np.interp(psi_sep[ii], psi_line[i, ind], line_z[ind])
            if ztmp >= eqsf.Zunt[ii] and ztmp <= eqsf.Zoben[ii]:
                zout[jt, pos] = ztmp
                Rout[jt, pos] = np.interp(psi_sep[ii], psi_line[i, ind], line_r[ind])
                pos += 1
    del line_r, line_z, psi_line

    return Rout, zout


def rhoTheta2rz(eqsf, rho, theta_in, t_in=None, coord_in='rho_pol', n_line=201):
    
    """
    This routine calculates the coordinates R, z of the intersections of
    a ray starting at the magnetic axis with fluxsurfaces 
    at given values of some radial coordinate.
    (slower than countours)

    Input:
    ----------
    rho: float or 1D array (nr) or nD array (nt,nr,...)
        coordinate of the desired flux surface inside LCFS!
    t_in: float or 1darray
        time point/array for the evaluation

    theta_in: float or 1D array n_theta
        angle of the straight line with respect to horizontal-outward, in radians!!
        
    coord_in:  str ['rho_pol', 'rho_tor' ,'rho_V', 'r_V', 'Psi','r_a']
        input coordinate label

    Output:
    ----------
    R ,  z: 3d+ array size(nt, n_theta, nr,...)
    """

    if t_in is None:
        t_in = eqsf.time

    tarr = np.atleast_1d(t_in)

    nt_in = len(tarr)

    rho  = np.atleast_1d(rho)
    if rho.ndim == 1:
        rho = np.tile(rho, (nt_in, 1))

    theta_in = np.atleast_1d(theta_in)[:, None]
    ntheta = len(theta_in)

    unique_idx, idx = get_nearest_index(eqsf.time, tarr)

#        n_line = 201 <=> 5 mm, but then there's interpolation!

    line_r = np.empty((len(unique_idx), ntheta, n_line))
    line_z = np.empty((len(unique_idx), ntheta, n_line))

    line_m = .9 # line length: 0.9 m
    t = np.linspace(0, 1, n_line)**.5*line_m
    c, s = np.cos(theta_in), np.sin(theta_in)
   
    tmpc = c*t
    tmps = s*t
    for i, ii in enumerate(unique_idx):
        line_r[i] = tmpc + eqsf.Rmag[ii]
        line_z[i] = tmps + eqsf.Zmag[ii]
 
    rho_line = rz2rho(eqsf, line_r, line_z, eqsf.time[unique_idx], \
                           coord_out=coord_in , extrapolate=True)

    R = np.empty((nt_in, ntheta) + rho.shape[1:], dtype=np.float32)
    z = np.empty((nt_in, ntheta) + rho.shape[1:], dtype=np.float32)

    if coord_in == 'Psi':
        rho_line[:,:,0] = eqsf.psi0[unique_idx][:,None]
        rho_line *= eqsf.orientation
        rho      *= eqsf.orientation
    else:
        #solve some issues very close to the core
        rho_line[:,:,0] = 0

    for i, ii in enumerate(unique_idx):
        jt = idx == ii
        for k in range(ntheta):
            rho_lin = rho_line[i, k]
            (tmp, ) = np.where(np.diff(rho_lin) > 0)
            imax = tmp[-1] + 1
            rspl = InterpolatedUnivariateSpline(rho_lin[:imax], \
                   line_r[i, k, :imax], k=2) 
            
            R[jt, k] = rspl(rho[jt].flatten()).reshape(rho[jt].shape)

            zspl = InterpolatedUnivariateSpline( \
                   rho_line[i, k, :imax], line_z[i, k, :imax], k=2)
            z[jt, k] = zspl(rho[jt].flatten()).reshape(rho[jt].shape)

    return R, z


def mag_theta_star(eqsf, t_in, n_rho=400, n_theta=200, rz_grid=False ):
    
    """
    Computes theta star 

    Input:
    ----------
    t_in: float 
        time point for the evaluation
    n_rho: int
        number of flux surfaces equaly spaced from 0 to 1 of rho_pol
    n_theta: int
        number of poloidal points 
    rz_grid: bool
        evaluate theta star on the grid

    Output:
    ----------
    R, z, theta: 3d arrays size(n_rho, n_theta)
    """

    rho = np.linspace(0, 1, n_rho+1)[1:]
    theta = np.linspace(0, 2*np.pi, n_theta, endpoint=False)

    magr, magz = rhoTheta2rz(eqsf, rho, theta, t_in=t_in, coord_in='rho_pol')
    magr, magz = magr[0].T, magz[0].T
    
    r0 = np.interp(t_in, eqsf.time, eqsf.Rmag)
    z0 = np.interp(t_in, eqsf.time, eqsf.Zmag)

    drdrho, drtheta = np.gradient(magr)
    dzdrho, dztheta = np.gradient(magz)
    dpsidrho, dpsitheta = np.gradient(np.tile(rho**2, (n_theta, 1)).T )

    grad_rho = np.dstack((drdrho, dzdrho, dpsidrho ))
    grad_theta = np.dstack((drtheta, dztheta, dpsitheta))
    normal = np.cross(grad_rho, grad_theta, axis=-1)

    dpsi_dr = -normal[:, :, 0]/(normal[:, :, 2] + 1e-8) #Bz
    dpsi_dz = -normal[:, :, 1]/(normal[:, :, 2] + 1e-8) #Br

#WARNING not defined on the magnetics axis

    dtheta_star = ((magr - r0)**2 + (magz - z0)**2)/(dpsi_dz*(magz - z0) + dpsi_dr*(magr - r0))/magr
    theta = np.arctan2(magz - z0, - magr + r0)
    
    theta = np.unwrap(theta - theta[:, (0, )], axis=1)
    
    from scipy.integrate import cumtrapz

# Definition of the theta star by integral
    theta_star = cumtrapz(dtheta_star, theta, axis=1, initial=0)
    correction = (n_theta - 1.)/n_theta

    theta_star/= theta_star[:, (-1, )]/(2*np.pi)/correction  #normalize to 2pi

    if not rz_grid:
        return magr, magz, theta_star

# Interpolate theta star on a regular grid 
    cos_th, sin_th = np.cos(theta_star), np.sin(theta_star)
    Linterp = LinearNDInterpolator(np.c_[magr.ravel(),magz.ravel()], cos_th.ravel(),0)
         
    nx = 100
    ny = 150

    rgrid = np.linspace(magr.min(), magr.max(), nx)
    zgrid = np.linspace(magz.min(), magz.max(), ny)

    R,Z = np.meshgrid(rgrid, zgrid)
    cos_grid = Linterp(np.c_[R.ravel(), Z.ravel()]).reshape(R.shape)
    Linterp.values[:, 0] = sin_th.ravel() #trick save a some  computing time
    sin_grid = Linterp(np.c_[R.ravel(), Z.ravel()]).reshape(R.shape)  

    theta_star = np.arctan2(sin_grid, cos_grid)

    return rgrid, zgrid, theta_star
