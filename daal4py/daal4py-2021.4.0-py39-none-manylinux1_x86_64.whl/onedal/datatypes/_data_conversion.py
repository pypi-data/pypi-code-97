#===============================================================================
# Copyright 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

from onedal import _backend


def from_table(*args):
    if len(args) == 1:
        return _backend.from_table(args[0])
    return (_backend.from_table(item) for item in args)


def to_table(*args):
    if len(args) == 1:
        return _backend.to_table(args[0])
    return (_backend.to_table(item) for item in args)
