# preset_status_pb.py/Open GoPro, Version 2.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Wed, Sep  1, 2021  5:05:48 PM

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: preset_status.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class EnumPresetGroup(betterproto.Enum):
    PRESET_GROUP_ID_VIDEO = 1000
    PRESET_GROUP_ID_PHOTO = 1001
    PRESET_GROUP_ID_TIMELAPSE = 1002
    PRESET_GROUP_ID_VIDEO_DUAL_LENS = 1003
    PRESET_GROUP_ID_PHOTO_DUAL_LENS = 1004
    PRESET_GROUP_ID_TIMELAPSE_DUAL_LENS = 1005
    PRESET_GROUP_ID_SPECIAL = 1006


class EnumFlatMode(betterproto.Enum):
    FLAT_MODE_UNKNOWN = -1
    FLAT_MODE_PLAYBACK = 4
    FLAT_MODE_SETUP = 5
    FLAT_MODE_VIDEO = 12
    FLAT_MODE_TIME_LAPSE_VIDEO = 13
    FLAT_MODE_LOOPING = 15
    FLAT_MODE_PHOTO = 17
    FLAT_MODE_PHOTO_NIGHT = 18
    FLAT_MODE_PHOTO_BURST = 19
    FLAT_MODE_TIME_LAPSE_PHOTO = 20
    FLAT_MODE_NIGHT_LAPSE_PHOTO = 21
    FLAT_MODE_BROADCAST_BROADCAST = 23
    FLAT_MODE_TIME_WARP_VIDEO = 24
    FLAT_MODE_LIVE_BURST = 25
    FLAT_MODE_NIGHT_LAPSE_VIDEO = 26
    FLAT_MODE_SLOMO = 27


class EnumPresetTitle(betterproto.Enum):
    PRESET_TITLE_ACTIVITY = 0
    PRESET_TITLE_STANDARD = 1
    PRESET_TITLE_CINEMATIC = 2
    PRESET_TITLE_PHOTO = 3
    PRESET_TITLE_LIVE_BURST = 4
    PRESET_TITLE_BURST = 5
    PRESET_TITLE_NIGHT = 6
    PRESET_TITLE_TIME_WARP = 7
    PRESET_TITLE_TIME_LAPSE = 8
    PRESET_TITLE_NIGHT_LAPSE = 9
    PRESET_TITLE_VIDEO = 10
    PRESET_TITLE_SLOMO = 11
    PRESET_TITLE_360_VIDEO = 12
    PRESET_TITLE_PHOTO_2 = 13
    PRESET_TITLE_PANORAMA = 14
    PRESET_TITLE_360_PHOTO = 15
    PRESET_TITLE_TIME_WARP_2 = 16
    PRESET_TITLE_360_TIME_WARP = 17
    PRESET_TITLE_CUSTOM = 18
    PRESET_TITLE_AIR = 19
    PRESET_TITLE_BIKE = 20
    PRESET_TITLE_EPIC = 21
    PRESET_TITLE_INDOOR = 22
    PRESET_TITLE_MOTOR = 23
    PRESET_TITLE_MOUNTED = 24
    PRESET_TITLE_OUTDOOR = 25
    PRESET_TITLE_POV = 26
    PRESET_TITLE_SELFIE = 27
    PRESET_TITLE_SKATE = 28
    PRESET_TITLE_SNOW = 29
    PRESET_TITLE_TRAIL = 30
    PRESET_TITLE_TRAVEL = 31
    PRESET_TITLE_WATER = 32
    PRESET_TITLE_LOOPING = 33
    # Reserved 34 - 50 for custom presets.
    PRESET_TITLE_360_TIMELAPSE = 51
    PRESET_TITLE_360_NIGHT_LAPSE = 52
    PRESET_TITLE_360_NIGHT_PHOTO = 53
    PRESET_TITLE_PANO_TIME_LAPSE = 54
    PRESET_TITLE_MAX_VIDEO = 55
    PRESET_TITLE_MAX_PHOTO = 56
    PRESET_TITLE_MAX_TIMEWARP = 57
    PRESET_TITLE_MAX = 58


class EnumPresetIcon(betterproto.Enum):
    PRESET_ICON_VIDEO = 0
    PRESET_ICON_ACTIVITY = 1
    PRESET_ICON_CINEMATIC = 2
    PRESET_ICON_PHOTO = 3
    PRESET_ICON_LIVE_BURST = 4
    PRESET_ICON_BURST = 5
    PRESET_ICON_PHOTO_NIGHT = 6
    PRESET_ICON_TIMEWARP = 7
    PRESET_ICON_TIMELAPSE = 8
    PRESET_ICON_NIGHTLAPSE = 9
    PRESET_ICON_SNAIL = 10
    PRESET_ICON_VIDEO_2 = 11
    PRESET_ICON_360_VIDEO = 12
    PRESET_ICON_PHOTO_2 = 13
    PRESET_ICON_PANORAMA = 14
    PRESET_ICON_BURST_2 = 15
    PRESET_ICON_TIMEWARP_2 = 16
    PRESET_ICON_TIMELAPSE_2 = 17
    PRESET_ICON_CUSTOM = 18
    PRESET_ICON_AIR = 19
    PRESET_ICON_BIKE = 20
    PRESET_ICON_EPIC = 21
    PRESET_ICON_INDOOR = 22
    PRESET_ICON_MOTOR = 23
    PRESET_ICON_MOUNTED = 24
    PRESET_ICON_OUTDOOR = 25
    PRESET_ICON_POV = 26
    PRESET_ICON_SELFIE = 27
    PRESET_ICON_SKATE = 28
    PRESET_ICON_SNOW = 29
    PRESET_ICON_TRAIL = 30
    PRESET_ICON_TRAVEL = 31
    PRESET_ICON_WATER = 32
    PRESET_ICON_LOOPING = 33
    # Add icons below for new presets starting from 51
    PRESET_ICON_MAX_VIDEO = 55
    PRESET_ICON_MAX_PHOTO = 56
    PRESET_ICON_MAX_TIMEWARP = 57
    PRESET_ICON_TIMELAPSE_PHOTO = 1000
    PRESET_ICON_NIGHTLAPSE_PHOTO = 1001
    PRESET_ICON_MAX = 1002


@dataclass
class NotifyPresetStatus(betterproto.Message):
    preset_group_array: List["PresetGroup"] = betterproto.message_field(1)


@dataclass
class PresetGroup(betterproto.Message):
    id: "EnumPresetGroup" = betterproto.enum_field(1)
    preset_array: List["Preset"] = betterproto.message_field(2)
    can_add_preset: bool = betterproto.bool_field(3)


@dataclass
class Preset(betterproto.Message):
    id: int = betterproto.int32_field(1)
    mode: "EnumFlatMode" = betterproto.enum_field(2)
    title_id: "EnumPresetTitle" = betterproto.enum_field(3)
    title_number: int = betterproto.int32_field(4)
    user_defined: bool = betterproto.bool_field(5)
    icon: "EnumPresetIcon" = betterproto.enum_field(6)
    setting_array: List["PresetSetting"] = betterproto.message_field(7)
    is_modified: bool = betterproto.bool_field(8)


@dataclass
class PresetSetting(betterproto.Message):
    id: int = betterproto.int32_field(1)
    value: int = betterproto.int32_field(2)
    is_caption: bool = betterproto.bool_field(3)
