import numpy as np


def smooth(array, num=7, method='mean'):
    methods = {'mean': np.mean, 'median': np.median}
    func = methods.get(method, None)
    if isinstance(array, np.ndarray) and (func is not None):
        new_array = np.zeros_like(array)
        wid = int(num)//2
        for i in range(array.shape[0]):
            s0 = np.max([0, i-wid]).astype(int)
            s1 = np.min([i+wid+1, array.shape[0]]).astype(int)
            new_array[i] = func(array[s0:s1])
        return new_array
    else:
        raise TypeError


def smooth_sphere(array, longitude, latitude, dphi=np.deg2rad(5), method='mean'):
    dlon, dlat = (longitude[1] - longitude[0]) / 2, (latitude[1] - latitude[0]) / 2
    longitude_, latitude_ = np.meshgrid(longitude[:-1] + dlon,
                                        latitude[:-1] + dlat)
    
    ptsx = (np.cos(longitude_) * np.cos(latitude_)).flatten()
    ptsy = (np.sin(longitude_) * np.cos(latitude_)).flatten()
    ptsz = np.sin(latitude_).flatten()
    array_ = array.flatten()
    result = np.zeros_like(array_)

    methods = {'mean': np.mean, 'median': np.median}
    func = methods.get(method, None)
    if isinstance(array, np.ndarray) and (func is not None):
        for i, X in enumerate(zip(ptsx, ptsy, ptsz)):
            # Compute angle between (x, y, z) and each point in the grid
            AdotB = ptsx * X[0] + ptsy * X[1] + ptsz * X[2]
            AdotB[AdotB > 1] = 1
            AdotB[AdotB < -1] = -1
            phi = np.arccos(AdotB)
            use = phi < dphi
            result[i] = func(array_[use])
    else:
        raise TypeError

    return result.reshape(array.shape)


