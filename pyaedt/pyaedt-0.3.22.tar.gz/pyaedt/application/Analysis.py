"""
This module contains the ``analysis`` class.

It includes common classes for file management and messaging and all
calls to AEDT modules like the modeler, mesh, postprocessing, and setup.
"""
from __future__ import absolute_import

import os
import shutil
import threading
import warnings
from collections import OrderedDict

from .. import is_ironpython
from ..generic.general_methods import aedt_exception_handler
from ..modeler.modeler_constants import CoordinateSystemAxis, CoordinateSystemPlane, GravityDirection, Plane
from ..modules.Boundary import NativeComponentObject
from ..modules.DesignXPloration import (
    DOESetups,
    DXSetups,
    OptimizationSetups,
    ParametericsSetups,
    SensitivitySetups,
    StatisticalSetups,
)
from ..modules.MaterialLib import Materials
from ..modules.SetupTemplates import SetupKeys
from ..modules.SolutionType import SetupTypes, SolutionType
from ..modules.SolveSetup import Setup
from .Design import Design

if is_ironpython:
    from ..modules.PostProcessor import PostProcessor
else:
    from ..modules.AdvancedPostProcessing import PostProcessor


class Analysis(Design, object):
    """Contains all common analysis functions.

    This class is inherited in the caller application and is accessible through it ( eg. ``hfss.method_name``).


    It is automatically initialized by a call from an application, such as HFSS or Q3D.
    See the application function for its parameter descriptions.

    Parameters
    ----------
    application : str
        Application that is to initialize the call.
    projectname : str
        Name of the project to select or the full path to the project
        or AEDTZ archive to open.
    designname : str
        Name of the design to select.
    solution_type : str
        Solution type to apply to the design.
    setup_name : str
        Name of the setup to use as the nominal.
    specified_version : str
        Version of AEDT  to use.
    NG : bool
        Whether to run AEDT in the non-graphical mode.
    new_desktop_session : bool
        Whether to launch an instance of AEDT in a new thread, even if
        another instance of the ``specified_version`` is active on the
        machine.
    close_on_exit : bool
        Whether to release  AEDT on exit.
    student_version : bool
        Whether to enable the student version of AEDT.

    """

    def __init__(
        self,
        application,
        projectname,
        designname,
        solution_type,
        setup_name,
        specified_version,
        non_graphical,
        new_desktop_session,
        close_on_exit,
        student_version,
    ):
        self.setups = []
        Design.__init__(
            self,
            application,
            projectname,
            designname,
            solution_type,
            specified_version,
            non_graphical,
            new_desktop_session,
            close_on_exit,
            student_version,
        )
        self.logger.info("Design Loaded")
        self._setup = None
        if setup_name:
            self.analysis_setup = setup_name
        self.solution_type = solution_type
        self._materials = Materials(self)
        self.logger.info("Materials Loaded")
        self._post = PostProcessor(self)
        self._available_variations = self.AvailableVariations(self)
        self.setups = [self.get_setup(setup_name) for setup_name in self.setup_names]
        self.opti_parametric = ParametericsSetups(self)
        self.opti_optimization = OptimizationSetups(self)
        self.opti_doe = DOESetups(self)
        self.opti_designxplorer = DXSetups(self)
        self.opti_sensitivity = SensitivitySetups(self)
        self.opti_statistical = StatisticalSetups(self)
        self.native_components = self._get_native_data()

    @property
    def materials(self):
        """Manages materials in the project.

        Returns
        -------
        :class:`pyaedt.modules.MaterialLib.Materials`
            Manages materials in the project.

        """
        return self._materials

    @property
    def Position(self):
        """Position of the object.

        Returns
        -------
        type
            Position object.

        """
        return self.modeler.Position

    @property
    def available_variations(self):
        """Available variation object.

        Returns
        -------
        :class:`pyaedt.application.Analysis.Analysis.AvailableVariations`
            Available variation object.

        """
        return self._available_variations

    @property
    def CoordinateSystemAxis(self):
        """Coordinate system axis constant.

        Returns
        -------
        tuple
            Coordinate system axis constants tuple (.X, .Y, .Z).

        """
        return CoordinateSystemAxis()

    @property
    def CoordinateSystemPlane(self):
        """Coordinate system plane constants.

        Returns
        -------
        tuple
            Coordinate system plane constants tuple (.XY, .YZ, .XZ).

        """
        return CoordinateSystemPlane()

    @property
    def View(self):
        """Planes. (To check if redundant to CoordinateSystemPlane.)


        Returns
        -------
        tuple
            Coordinate system plane string tuple ("XY", "YZ", "XZ").

        """
        return Plane()

    @property
    def GravityDirection(self):
        """Gravity direction. (To check if redundant.)

        Returns
        -------
        tuple
            Gravity direction tuple (XNeg, YNeg, ZNeg, XPos, YPos, ZPos).

        """
        return GravityDirection()

    @property
    def modeler(self):
        """Modeler.

        Returns
        -------
        :class:`pyaedt.modeler.Modeler.Modeler`
            Modeler object.
        """
        return self._modeler

    @property
    def mesh(self):
        """Mesh.

        Returns
        -------
        :class:`pyaedt.modules.Mesh.Mesh`
            Mesh object.
        """
        return self._mesh

    @property
    def post(self):
        """PostProcessor.

        Returns
        -------
        :class:`pyaedt.modules.PostProcessor.PostProcessor`
            PostProcessor object.
        """
        return self._post

    @property
    def osolution(self):
        """Solution.

        Returns
        -------
        AEDT object
            Solution module.

        """
        return self.odesign.GetModule("Solutions")

    @property
    def oanalysis(self):
        """Analysis."""
        return self.odesign.GetModule("AnalysisSetup")

    @property
    def analysis_setup(self):
        """Analysis setup.

        Returns
        -------
        str
            Name of the active or first analysis setup.

        """
        if self._setup:
            return self._setup
        elif self.existing_analysis_setups:
            return self.existing_analysis_setups[0]
        else:
            self._setup = None
            return self._setup

    @analysis_setup.setter
    def analysis_setup(self, setup_name):
        setup_list = self.existing_analysis_setups
        if setup_list:
            assert setup_name in setup_list, "Invalid setup name {}".format(setup_name)
            self._setup = setup_name
        else:
            self._setup = setup_list[0]
        # return self._setup

    @property
    def existing_analysis_sweeps(self):
        """Existing analysis sweeps.

        Returns
        -------
        list
            List of all analysis sweeps in the design.

        """
        setup_list = self.existing_analysis_setups
        sweep_list = []
        if self.solution_type == "HFSS3DLayout" or self.solution_type == "HFSS 3D Layout Design":
            sweep_list = self.oanalysis.GetAllSolutionNames()
            sweep_list = [i for i in sweep_list if "Adaptive Pass" not in i]
            sweep_list.reverse()
        else:
            for el in setup_list:
                if self.solution_type == "HFSS3DLayout" or self.solution_type == "HFSS 3D Layout Design":
                    sweeps = self.oanalysis.GelAllSolutionNames()
                elif self.solution_type in SetupKeys.defaultAdaptive.keys():
                    setuptype = SetupKeys.defaultAdaptive[self.solution_type]
                    if setuptype:
                        sweep_list.append(el + " : " + setuptype)
                try:
                    sweeps = list(self.oanalysis.GetSweeps(el))
                except:
                    sweeps = []
                for sw in sweeps:
                    sweep_list.append(el + " : " + sw)
        return sweep_list

    @property
    def nominal_adaptive(self):
        """Nominal adaptive sweep.

        Returns
        -------
        str
            Name of the nominal adaptive sweep.

        """
        if len(self.existing_analysis_sweeps) > 0:
            return self.existing_analysis_sweeps[0]
        else:
            return ""

    @property
    def nominal_sweep(self):
        """Nominal sweep.

        Returns
        -------
        str
            Name of the last adaptive sweep if a sweep is available or
            the name of the nominal adaptive sweep if present.
        """

        if len(self.existing_analysis_sweeps) > 1:
            return self.existing_analysis_sweeps[1]
        else:
            return self.nominal_adaptive

    @property
    def existing_analysis_setups(self):
        """Existing analysis setups.

        Returns
        -------
        list
            List of all analysis setups in the design.

        """
        setups = list(self.oanalysis.GetSetups())
        return setups

    @property
    def output_variables(self):
        """Output variables.

        Returns
        -------
        list
            List of output variables.

        """
        oModule = self.odesign.GetModule("OutputVariable")
        return oModule.GetOutputVariables()

    @property
    def setup_names(self):
        """Setup names.

        Returns
        -------
        list
            List of names of all analysis setups in the design.

        """
        return self.oanalysis.GetSetups()

    @property
    def ooptimetrics(self):
        """Optimetrics.

        Returns
        -------
        AEDT object
            Optimetrics module object.

        """
        return self.odesign.GetModule("Optimetrics")

    @property
    def ooutput_variable(self):
        """Output variable.

        Returns
        -------
        AEDT object
            Output variable module object.

        """
        return self.odesign.GetModule("OutputVariable")

    @property
    def SimulationSetupTypes(self):
        """Simulation setup types.

        Returns
        -------
        SetupTypes
            List of all simulation setup types categorized by application.
        """
        return SetupTypes()

    @property
    def SolutionTypes(self):
        """Solution types.

        Returns
        -------
        SolutionType
            List of all solution type categorized by application.
        """
        return SolutionType()

    @aedt_exception_handler
    def _get_native_data(self):
        """Retrieve Native Components data."""
        boundaries = []
        try:
            data_vals = self.design_properties["ModelSetup"]["GeometryCore"]["GeometryOperations"][
                "SubModelDefinitions"
            ]["NativeComponentDefinition"]
            if not isinstance(data_vals, list) and type(data_vals) is OrderedDict:
                boundaries.append(
                    NativeComponentObject(
                        self,
                        data_vals["NativeComponentDefinitionProvider"]["Type"],
                        data_vals["BasicComponentInfo"]["ComponentName"],
                        data_vals,
                    )
                )
            for ds in data_vals:
                try:
                    if type(ds) is OrderedDict:
                        boundaries.append(
                            NativeComponentObject(
                                self,
                                ds["NativeComponentDefinitionProvider"]["Type"],
                                ds["BasicComponentInfo"]["ComponentName"],
                                ds,
                            )
                        )
                except:
                    pass
        except:
            pass
        return boundaries

    class AvailableVariations(object):
        def __init__(self, parent):
            """Contains available variations.

            Parameters
            ----------
            parent :
                Inherited parent object.

            Returns
            -------
            object
                Parent object.

            """
            self._parent = parent

        @property
        def variables(self):
            """Variables.

            Returns
            -------
            list
                List of names of independent variables.
            """
            return [i for i in self._parent.variable_manager.independent_variables]

        @aedt_exception_handler
        def variations(self, setup_sweep=None):
            """Variations.

            Parameters
            ----------
            setup_sweep : str, optional
                Setup name with the sweep to search for variations on. The default is ``None``.

            Returns
            -------
            list
                List of variation families.

            """
            if not setup_sweep:
                setup_sweep = self._parent.existing_analysis_sweeps[0]
            vs = self._parent.osolution.GetAvailableVariations(setup_sweep)
            families = []
            for v in vs:
                variations = v.split(" ")
                family = []
                for el in self.variables:
                    family.append(el + ":=")
                    i = 0
                    while i < len(variations):
                        if variations[i][0 : len(el)] == el:
                            family.append([variations[i][len(el) + 2 : -1]])
                        i += 1
                families.append(family)
            return families

        @property
        def nominal(self):
            """Nominal."""
            families = []
            for el in self.variables:
                families.append(el + ":=")
                families.append(["Nominal"])
            return families

        @property
        def nominal_w_values(self):
            """Nominal with values."""
            families = []
            if self._parent.design_type == "HFSS 3D Layout Design":
                listvar = list(self._parent.odesign.GetVariables())
                for el in listvar:
                    families.append(el + ":=")
                    families.append([self._parent.odesign.GetVariableValue(el)])
            else:
                variation = self._parent.odesign.GetNominalVariation()
                for el in self.variables:
                    families.append(el + ":=")
                    families.append([self._parent.odesign.GetVariationVariableValue(variation, el)])
            return families

        @property
        def nominal_w_values_dict(self):
            """Nominal with values in a dictionary."""
            families = {}
            if self._parent.design_type == "HFSS 3D Layout Design":
                listvar = list(self._parent.odesign.GetVariables())
                for el in listvar:
                    families[el] = self._parent.odesign.GetVariableValue(el)
            else:
                variation = self._parent.odesign.GetNominalVariation()
                for el in self.variables:
                    families[el] = self._parent.odesign.GetVariationVariableValue(variation, el)
            return families

        @property
        def all(self):
            """All."""
            families = []
            for el in self.variables:
                families.append(el + ":=")
                families.append(["All"])
            return families

    class AxisDir(object):
        """Contains constants for the axis directions."""

        (XNeg, YNeg, ZNeg, XPos, YPos, ZPos) = range(0, 6)

    @aedt_exception_handler
    def get_setups(self):
        """Retrieve setups.

        Returns
        -------
        list
            List of names of all setups.

        """
        setups = self.oanalysis.GetSetups()
        return list(setups)

    @aedt_exception_handler
    def get_nominal_variation(self):
        """Retrieve the nominal variation.

        Returns
        -------
        list
            List of nominal variations.
        """
        return self.available_variations.nominal

    @aedt_exception_handler
    def get_sweeps(self, name):
        """Retrieve all sweep for a setup.

        Parameters
        ----------
        name : str
            Name of the setup.

        Returns
        -------
        list
            List of names of all sweeps for the setup.

        """
        sweeps = self.oanalysis.GetSweeps(name)
        return list(sweeps)

    @aedt_exception_handler
    def export_parametric_results(self, sweepname, filename, exportunits=True):
        """Export a list of all parametric variations solved for a sweep to a CSV file.

        Parameters
        ----------
        sweepname : str
            Name of the optimetrics sweep.
        filename : str
            Full path and name for the CSV file.
        exportunits : bool, optional
            Whether to export units with the value. The default is ``True``. When ``False``,
            only the value is exported.

        Returns
        -------
        bool
            ``True`` when successful, ``False`` when failed.
        """

        self.ooptimetrics.ExportParametricResults(sweepname, filename, exportunits)
        return True

    @aedt_exception_handler
    def analyze_from_initial_mesh(self):
        """Revert the solution to the initial mesh and re-run the solve.

        Returns
        -------
        bool
           ``True`` when successful, ``False`` when failed.
        """
        self.oanalysis.RevertSetupToInitial(self._setup)
        self.analyze_nominal()
        return True

    @aedt_exception_handler
    def analyse_nominal(self):
        """Solve the nominal design.

        .. deprecated:: 0.4.0
           Use :func:`Analysis.analyze_nominal` instead.
        """
        warnings.warn("`analyse_nominal` is deprecated. Use `analyze_nominal` instead.", DeprecationWarning)
        self.analyze_nominal()

    @aedt_exception_handler
    def analyze_nominal(self):
        """Solve the nominal design.

        Returns
        -------
        bool
            ``True`` when successful, ``False`` when failed.
        """
        self.odesign.Analyze(self.analysis_setup)
        return True

    @aedt_exception_handler
    def generate_unique_setup_name(self, setup_name=None):
        """Generate a new setup with an unique name.

        Parameters
        ----------
        setup_name : str, optional
            Name of the setup. The default is ``None``.

        Returns
        -------
        str
            Name of the setup.

        """
        if not setup_name:
            setup_name = "Setup"
        index = 2
        while setup_name in self.existing_analysis_setups:
            setup_name = setup_name + "_{}".format(index)
            index += 1
        return setup_name

    @aedt_exception_handler
    def create_setup(self, setupname="MySetupAuto", setuptype=None, props={}):
        """Create a setup.

        Parameters
        ----------
        setupname : str, optional
            Name of the setup. The default is ``"MySetupAuto"``.
        setuptype : optional
            Type of the setup. The default is ``None``, in which case
            the default type is applied.
        props : dict, optional
            Dictionary of analysis properties appropriate for the design and analysis.
            If no values are passed, default values will be used.

        Returns
        -------
        :class:`pyaedt.modules.SolveSetup.Setup`

        Examples
        --------
        Create a setup for SBR+ setup using advanced Doppler
        processing for automotive radar.

        >>> import pyaedt
        >>> hfss = pyaedt.Hfss(solution_type='SBR+')
        >>> setup1 = hfss.create_setup(setupname='Setup1')
        >>> setup1.props["IsSbrRangeDoppler"] = True
        >>> setup1.props["SbrRangeDopplerTimeVariable"] = "time_var"
        >>> setup1.props["SbrRangeDopplerCenterFreq"] = "76.5GHz"
        >>> setup1.props["SbrRangeDopplerRangeResolution"] = "0.15meter"
        >>> setup1.props["SbrRangeDopplerRangePeriod"] = "100meter"
        >>> setup1.props["SbrRangeDopplerVelocityResolution"] = "0.2m_per_sec"
        >>> setup1.props["SbrRangeDopplerVelocityMin"] = "-30m_per_sec"
        >>> setup1.props["SbrRangeDopplerVelocityMax"] = "30m_per_sec"
        >>> setup1.props["DopplerRayDensityPerWavelength"] = "0.2"
        >>> setup1.props["MaxNumberOfBounces"] = "3"
        >>> setup1.update()
        ...
        pyaedt Info: Sweep was created correctly.
        """
        if setuptype is None:
            if self.design_type == "Icepak" and self.solution_type == "Transient":
                setuptype = SetupKeys.defaultSetups["TransientTemperatureAndFlow"]
            else:
                setuptype = SetupKeys.defaultSetups[self.solution_type]
        name = self.generate_unique_setup_name(setupname)
        setup = Setup(self, setuptype, name)
        setup.create()
        if props:
            for el in props:
                setup.props[el] = props[el]
            setup.update()

        self.analysis_setup = name
        self.setups.append(setup)
        return setup

    @aedt_exception_handler
    def delete_setup(self, setupname):
        """Delete a setup.

        Parameters
        ----------
        setupname : str
            Name of the setup.

        Returns
        -------
        bool
            ``True`` when successful, ``False`` when failed.

        Examples
        --------
        Create a setup and then delete it.

        >>> import pyaedt
        >>> hfss = pyaedt.Hfss()
        >>> setup1 = hfss.create_setup(setupname='Setup1')
        >>> hfss.delete_setup(setupname='Setup1')
        ...
        pyaedt Info: Sweep was deleted correctly.
        """
        if setupname in self.existing_analysis_setups:
            self.oanalysis.DeleteSetups([setupname])
            for s in self.setups:
                if s.name == setupname:
                    self.setups.remove(s)
            return True
        return False

    @aedt_exception_handler
    def edit_setup(self, setupname, properties_dict):
        """Modify a setup.

        Parameters
        ----------
        setupname : str
            Name of the setup.
        properties_dict : dict
            Dictionary containing the property to update with the value.

        Returns
        -------
        :class:`pyaedt.modules.SolveSetup.Setup`

        """
        setuptype = SetupKeys.defaultSetups[self.solution_type]
        setup = Setup(self, setuptype, setupname, isnewsetup=False)
        setup.update(properties_dict)
        self.analysis_setup = setupname
        return setup

    @aedt_exception_handler
    def get_setup(self, setupname):
        """Get the setup from the current design.

        Parameters
        ----------
        setupname : str
            Name of the setup.

        Returns
        -------
        :class:`pyaedt.modules.SolveSetup.Setup`

        """

        setuptype = SetupKeys.defaultSetups[self.solution_type]
        setup = Setup(self, setuptype, setupname, isnewsetup=False)
        if setup.props:
            self.analysis_setup = setupname
        return setup

    @aedt_exception_handler
    def create_output_variable(self, variable, expression):
        """Create or modify an output variable.

        Parameters
        ----------
        variable : str
            Name of the variable.
        expression :
            Value for the variable.

        Returns
        -------
        bool
           ``True`` when successful, ``False`` when failed.
        """
        oModule = self.odesign.GetModule("OutputVariable")
        if variable in self.output_variables:
            oModule.EditOutputVariable(
                variable, expression, variable, self.existing_analysis_sweeps[0], self.solution_type, []
            )
        else:
            oModule.CreateOutputVariable(variable, expression, self.existing_analysis_sweeps[0], self.solution_type, [])
        return True

    @aedt_exception_handler
    def get_output_variable(self, variable, solution_name=None, report_type_name=None):
        """Retrieve the value of the output variable.

        Parameters
        ----------
        variable : str
            Name of the variable.
        solution_name : str, optional
            Name of the solution. The default is ``None``.
        report_type_name : str, optional
            Name of the report type. The default is ``None``.

        Returns
        -------
        type
            Value of the output variable.
        """
        oModule = self.odesign.GetModule("OutputVariable")
        assert variable in self.output_variables, "Output variable {} does not exist.".format(variable)
        nominal_variation = self.odesign.GetNominalVariation()
        sol_type = self.solution_type
        value = oModule.GetOutputVariableValue(
            variable, nominal_variation, self.existing_analysis_sweeps[0], self.solution_type, []
        )
        return value

    @aedt_exception_handler
    def get_object_material_properties(self, object_list=None, prop_names=None):
        """Retrieve the material properties for a list of given objects and return them in a dictionary.

        This high-level function ignores objects with no defined material properties.

        Parameters
        ----------
        object_list : list, optional
            List of objects for which to get material_properties. The default is ``None``,
            in which case all objects are considered.
        prop_names : str or list
            The property or list of properties to export.  The default is ``None``, in
            which case all properties are exported.

        Returns
        -------
        dict
            Dictionary of objects with material properties.
        """
        if object_list:
            if not isinstance(object_list, list):
                object_list = [object_list]
        else:
            object_list = self.modeler.primitives.object_names

        if prop_names:
            if not isinstance(prop_names, list):
                prop_names = [prop_names]

        dict = {}
        for entry in object_list:
            mat_name = self.modeler.primitives[entry].material_name
            mat_props = self._materials[mat_name]
            if prop_names is None:
                dict[entry] = mat_props._props
            else:
                dict[entry] = {}
                for prop_name in prop_names:
                    dict[entry][prop_name] = mat_props._props[prop_name]
        return dict

    @aedt_exception_handler
    def analyze_setup(self, name):
        """Analyze a specific design setup.

        Parameters
        ----------
        name : str
            Name of the setup, which can be an optimetric setup or a simple setup.

        Returns
        -------
        bool
           ``True`` when successful, ``False`` when failed.
        """
        if name in self.existing_analysis_setups:
            self._messenger.add_info_message("Solving design setup {}".format(name))
            self.odesign.Analyze(name)
        else:
            try:
                self._messenger.add_info_message("Solving Optimetrics")
                self.ooptimetrics.SolveSetup(name)
            except:
                self._messenger.add_error_message("Setup Not found {}".format(name))
                return False
        return True

    @aedt_exception_handler
    def solve_in_batch(self, filename=None, machine="local", run_in_thread=False):
        """Analyze a design setup in batch mode.

        .. note::
           To use this function, the AEDT project must be closed.

        Parameters
        ----------
        filename : str, optional
            Name of the setup. The default is ``None``, which means that the active project
            is to be solved.
        machine : str, optional
            Name of the machine if remote.  The default is ``"local"``.
        run_in_thread : bool, optional
            Whether the batch command is to be submitted as a thread. The default is
            ``False``.

        Returns
        -------
         bool
           ``True`` when successful, ``False`` when failed.
        """
        if not filename:
            filename = self.project_file
            self.close_project()
        if machine == "local":
            # -Monitor option used as workaround for R2 BatchSolve not exiting properly at the end of the Batch job
            options = " -ng -BatchSolve -Monitor "
        else:
            options = " -ng -distribute -machinelist list=" + machine + " -Batchsolve "

        self.add_info_message("Batch Solve Options: " + options)
        if os.name == "posix":
            batch_run = os.path.join(
                self.desktop_install_dir + "/ansysedt" + chr(34) + options + chr(34) + filename + chr(34)
            )
        else:
            batch_run = (
                chr(34) + self.desktop_install_dir + "/ansysedt.exe" + chr(34) + options + chr(34) + filename + chr(34)
            )

        """
        check for existing solution directory and delete if present so we
        dont have old .asol files etc
        """

        self.add_info_message("Solving model in batch mode on " + machine)
        self.add_info_message("Batch Job command:" + batch_run)
        if run_in_thread:

            def thread_run():
                """ """
                os.system(batch_run)

            x = threading.Thread(target=thread_run)
            x.start()
        else:
            os.system(batch_run)
        self.add_info_message("Batch job finished.")
        return True

    @aedt_exception_handler
    def submit_job(
        self, clustername, aedt_full_exe_path=None, numnodes=1, numcores=32, wait_for_license=True, setting_file=None
    ):
        """Submit a job to be solved on a cluster.

        Parameters
        ----------
        clustername : str
            Name of the cluster to submit the job to.
        aedt_full_exe_path : str, optional
            Full path to the AEDT executable file. The default is ``None``, in which
            case ``"/clustername/AnsysEM/AnsysEM2x.x/Win64/ansysedt.exe"`` is used.
        numnodes : int, optional
            Number of nodes. The default is ``1``.
        numcores : int, optional
            Number of cores. The default is ``32``.
        wait_for_license : bool, optional
             Whether to wait for the license to be validated. The default is ``True``.
        setting_file : str, optional
            Name of the file to use as a template. The default value is ``None``.

        Returns
        -------
        type
            ID of the job.

        """
        project_file = self.project_file
        project_path = self.project_path
        if not aedt_full_exe_path:
            version = self.odesktop.GetVersion()[2:6]
            if os.path.exists(r"\\" + clustername + r"\AnsysEM\AnsysEM{}\Win64\ansysedt.exe".format(version)):
                aedt_full_exe_path = (
                    r"\\\\\\\\" + clustername + r"\\\\AnsysEM\\\\AnsysEM{}\\\\Win64\\\\ansysedt.exe".format(version)
                )
            elif os.path.exists(r"\\" + clustername + r"\AnsysEM\AnsysEM{}\Linux64\ansysedt".format(version)):
                aedt_full_exe_path = (
                    r"\\\\\\\\" + clustername + r"\\\\AnsysEM\\\\AnsysEM{}\\\\Linux64\\\\ansysedt".format(version)
                )
            else:
                self._messenger.add_error_message("Aedt Path doesn't exists. Please provide a full path")
                return False
        else:
            if not os.path.exists(aedt_full_exe_path):
                self._messenger.add_error_message("Aedt Path doesn't exists. Please provide a full path")
                return False
            aedt_full_exe_path.replace("\\", "\\\\")

        self.close_project()
        path_file = os.path.dirname(__file__)
        destination_reg = os.path.join(project_path, "Job_settings.areg")
        if not setting_file:
            setting_file = os.path.join(path_file, "..", "misc", "Job_Settings.areg")
        shutil.copy(setting_file, destination_reg)

        f1 = open(destination_reg, "w")
        with open(setting_file) as f:
            lines = f.readlines()
            for line in lines:
                if "\\	$begin" == line[:8]:
                    lin = "\\	$begin \\'{}\\'\\\n".format(clustername)
                    f1.write(lin)
                elif "\\	$end" == line[:6]:
                    lin = "\\	$end \\'{}\\'\\\n".format(clustername)
                    f1.write(lin)
                elif "NumCores" in line:
                    lin = "\\	\\	\\	\\	NumCores={}\\\n".format(numcores)
                    f1.write(lin)
                elif "NumNodes=1" in line:
                    lin = "\\	\\	\\	\\	NumNodes={}\\\n".format(numnodes)
                    f1.write(lin)
                elif "ProductPath" in line:
                    lin = "\\	\\	ProductPath =\\'{}\\'\\\n".format(aedt_full_exe_path)
                    f1.write(lin)
                elif "WaitForLicense" in line:
                    lin = "\\	\\	WaitForLicense={}\\\n".format(str(wait_for_license).lower())
                    f1.write(lin)
                else:
                    f1.write(line)
        f1.close()
        return self.odesktop.SubmitJob(os.path.join(project_path, "Job_settings.areg"), project_file)
