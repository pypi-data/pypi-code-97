# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceShapeConfig(object):
    """
    The shape configuration for an instance. The shape configuration determines
    the resources allocated to an instance.
    """

    #: A constant which can be used with the baseline_ocpu_utilization property of a InstanceShapeConfig.
    #: This constant has a value of "BASELINE_1_8"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_8 = "BASELINE_1_8"

    #: A constant which can be used with the baseline_ocpu_utilization property of a InstanceShapeConfig.
    #: This constant has a value of "BASELINE_1_2"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_2 = "BASELINE_1_2"

    #: A constant which can be used with the baseline_ocpu_utilization property of a InstanceShapeConfig.
    #: This constant has a value of "BASELINE_1_1"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_1 = "BASELINE_1_1"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceShapeConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this InstanceShapeConfig.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this InstanceShapeConfig.
        :type memory_in_gbs: float

        :param baseline_ocpu_utilization:
            The value to assign to the baseline_ocpu_utilization property of this InstanceShapeConfig.
            Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type baseline_ocpu_utilization: str

        :param processor_description:
            The value to assign to the processor_description property of this InstanceShapeConfig.
        :type processor_description: str

        :param networking_bandwidth_in_gbps:
            The value to assign to the networking_bandwidth_in_gbps property of this InstanceShapeConfig.
        :type networking_bandwidth_in_gbps: float

        :param max_vnic_attachments:
            The value to assign to the max_vnic_attachments property of this InstanceShapeConfig.
        :type max_vnic_attachments: int

        :param gpus:
            The value to assign to the gpus property of this InstanceShapeConfig.
        :type gpus: int

        :param gpu_description:
            The value to assign to the gpu_description property of this InstanceShapeConfig.
        :type gpu_description: str

        :param local_disks:
            The value to assign to the local_disks property of this InstanceShapeConfig.
        :type local_disks: int

        :param local_disks_total_size_in_gbs:
            The value to assign to the local_disks_total_size_in_gbs property of this InstanceShapeConfig.
        :type local_disks_total_size_in_gbs: float

        :param local_disk_description:
            The value to assign to the local_disk_description property of this InstanceShapeConfig.
        :type local_disk_description: str

        """
        self.swagger_types = {
            'ocpus': 'float',
            'memory_in_gbs': 'float',
            'baseline_ocpu_utilization': 'str',
            'processor_description': 'str',
            'networking_bandwidth_in_gbps': 'float',
            'max_vnic_attachments': 'int',
            'gpus': 'int',
            'gpu_description': 'str',
            'local_disks': 'int',
            'local_disks_total_size_in_gbs': 'float',
            'local_disk_description': 'str'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'baseline_ocpu_utilization': 'baselineOcpuUtilization',
            'processor_description': 'processorDescription',
            'networking_bandwidth_in_gbps': 'networkingBandwidthInGbps',
            'max_vnic_attachments': 'maxVnicAttachments',
            'gpus': 'gpus',
            'gpu_description': 'gpuDescription',
            'local_disks': 'localDisks',
            'local_disks_total_size_in_gbs': 'localDisksTotalSizeInGBs',
            'local_disk_description': 'localDiskDescription'
        }

        self._ocpus = None
        self._memory_in_gbs = None
        self._baseline_ocpu_utilization = None
        self._processor_description = None
        self._networking_bandwidth_in_gbps = None
        self._max_vnic_attachments = None
        self._gpus = None
        self._gpu_description = None
        self._local_disks = None
        self._local_disks_total_size_in_gbs = None
        self._local_disk_description = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this InstanceShapeConfig.
        The total number of OCPUs available to the instance.


        :return: The ocpus of this InstanceShapeConfig.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this InstanceShapeConfig.
        The total number of OCPUs available to the instance.


        :param ocpus: The ocpus of this InstanceShapeConfig.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this InstanceShapeConfig.
        The total amount of memory available to the instance, in gigabytes.


        :return: The memory_in_gbs of this InstanceShapeConfig.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this InstanceShapeConfig.
        The total amount of memory available to the instance, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this InstanceShapeConfig.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def baseline_ocpu_utilization(self):
        """
        Gets the baseline_ocpu_utilization of this InstanceShapeConfig.
        The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
        non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance.

        Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The baseline_ocpu_utilization of this InstanceShapeConfig.
        :rtype: str
        """
        return self._baseline_ocpu_utilization

    @baseline_ocpu_utilization.setter
    def baseline_ocpu_utilization(self, baseline_ocpu_utilization):
        """
        Sets the baseline_ocpu_utilization of this InstanceShapeConfig.
        The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
        non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is the entire OCPU. This represents a non-burstable instance.


        :param baseline_ocpu_utilization: The baseline_ocpu_utilization of this InstanceShapeConfig.
        :type: str
        """
        allowed_values = ["BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"]
        if not value_allowed_none_or_none_sentinel(baseline_ocpu_utilization, allowed_values):
            baseline_ocpu_utilization = 'UNKNOWN_ENUM_VALUE'
        self._baseline_ocpu_utilization = baseline_ocpu_utilization

    @property
    def processor_description(self):
        """
        Gets the processor_description of this InstanceShapeConfig.
        A short description of the instance's processor (CPU).


        :return: The processor_description of this InstanceShapeConfig.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this InstanceShapeConfig.
        A short description of the instance's processor (CPU).


        :param processor_description: The processor_description of this InstanceShapeConfig.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def networking_bandwidth_in_gbps(self):
        """
        Gets the networking_bandwidth_in_gbps of this InstanceShapeConfig.
        The networking bandwidth available to the instance, in gigabits per second.


        :return: The networking_bandwidth_in_gbps of this InstanceShapeConfig.
        :rtype: float
        """
        return self._networking_bandwidth_in_gbps

    @networking_bandwidth_in_gbps.setter
    def networking_bandwidth_in_gbps(self, networking_bandwidth_in_gbps):
        """
        Sets the networking_bandwidth_in_gbps of this InstanceShapeConfig.
        The networking bandwidth available to the instance, in gigabits per second.


        :param networking_bandwidth_in_gbps: The networking_bandwidth_in_gbps of this InstanceShapeConfig.
        :type: float
        """
        self._networking_bandwidth_in_gbps = networking_bandwidth_in_gbps

    @property
    def max_vnic_attachments(self):
        """
        Gets the max_vnic_attachments of this InstanceShapeConfig.
        The maximum number of VNIC attachments for the instance.


        :return: The max_vnic_attachments of this InstanceShapeConfig.
        :rtype: int
        """
        return self._max_vnic_attachments

    @max_vnic_attachments.setter
    def max_vnic_attachments(self, max_vnic_attachments):
        """
        Sets the max_vnic_attachments of this InstanceShapeConfig.
        The maximum number of VNIC attachments for the instance.


        :param max_vnic_attachments: The max_vnic_attachments of this InstanceShapeConfig.
        :type: int
        """
        self._max_vnic_attachments = max_vnic_attachments

    @property
    def gpus(self):
        """
        Gets the gpus of this InstanceShapeConfig.
        The number of GPUs available to the instance.


        :return: The gpus of this InstanceShapeConfig.
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """
        Sets the gpus of this InstanceShapeConfig.
        The number of GPUs available to the instance.


        :param gpus: The gpus of this InstanceShapeConfig.
        :type: int
        """
        self._gpus = gpus

    @property
    def gpu_description(self):
        """
        Gets the gpu_description of this InstanceShapeConfig.
        A short description of the instance's graphics processing unit (GPU).

        If the instance does not have any GPUs, this field is `null`.


        :return: The gpu_description of this InstanceShapeConfig.
        :rtype: str
        """
        return self._gpu_description

    @gpu_description.setter
    def gpu_description(self, gpu_description):
        """
        Sets the gpu_description of this InstanceShapeConfig.
        A short description of the instance's graphics processing unit (GPU).

        If the instance does not have any GPUs, this field is `null`.


        :param gpu_description: The gpu_description of this InstanceShapeConfig.
        :type: str
        """
        self._gpu_description = gpu_description

    @property
    def local_disks(self):
        """
        Gets the local_disks of this InstanceShapeConfig.
        The number of local disks available to the instance.


        :return: The local_disks of this InstanceShapeConfig.
        :rtype: int
        """
        return self._local_disks

    @local_disks.setter
    def local_disks(self, local_disks):
        """
        Sets the local_disks of this InstanceShapeConfig.
        The number of local disks available to the instance.


        :param local_disks: The local_disks of this InstanceShapeConfig.
        :type: int
        """
        self._local_disks = local_disks

    @property
    def local_disks_total_size_in_gbs(self):
        """
        Gets the local_disks_total_size_in_gbs of this InstanceShapeConfig.
        The aggregate size of all local disks, in gigabytes.

        If the instance does not have any local disks, this field is `null`.


        :return: The local_disks_total_size_in_gbs of this InstanceShapeConfig.
        :rtype: float
        """
        return self._local_disks_total_size_in_gbs

    @local_disks_total_size_in_gbs.setter
    def local_disks_total_size_in_gbs(self, local_disks_total_size_in_gbs):
        """
        Sets the local_disks_total_size_in_gbs of this InstanceShapeConfig.
        The aggregate size of all local disks, in gigabytes.

        If the instance does not have any local disks, this field is `null`.


        :param local_disks_total_size_in_gbs: The local_disks_total_size_in_gbs of this InstanceShapeConfig.
        :type: float
        """
        self._local_disks_total_size_in_gbs = local_disks_total_size_in_gbs

    @property
    def local_disk_description(self):
        """
        Gets the local_disk_description of this InstanceShapeConfig.
        A short description of the local disks available to this instance.

        If the instance does not have any local disks, this field is `null`.


        :return: The local_disk_description of this InstanceShapeConfig.
        :rtype: str
        """
        return self._local_disk_description

    @local_disk_description.setter
    def local_disk_description(self, local_disk_description):
        """
        Sets the local_disk_description of this InstanceShapeConfig.
        A short description of the local disks available to this instance.

        If the instance does not have any local disks, this field is `null`.


        :param local_disk_description: The local_disk_description of this InstanceShapeConfig.
        :type: str
        """
        self._local_disk_description = local_disk_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
