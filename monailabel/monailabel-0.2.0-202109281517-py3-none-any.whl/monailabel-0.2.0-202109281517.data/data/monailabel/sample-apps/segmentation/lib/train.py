# Copyright 2020 - 2021 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

import torch
from monai.inferers import SlidingWindowInferer
from monai.losses import DiceLoss
from monai.transforms import (
    Activationsd,
    AddChanneld,
    AsDiscreted,
    CropForegroundd,
    LoadImaged,
    RandCropByPosNegLabeld,
    RandShiftIntensityd,
    ScaleIntensityRanged,
    Spacingd,
    ToTensord,
)

from monailabel.tasks.train.basic_train import BasicTrainTask

logger = logging.getLogger(__name__)


class MyTrain(BasicTrainTask):
    def __init__(
        self,
        model_dir,
        network,
        description="Train generic Segmentation model",
        **kwargs,
    ):
        self._network = network
        super().__init__(model_dir, description, **kwargs)

    def network(self):
        return self._network

    def optimizer(self):
        return torch.optim.Adam(self._network.parameters(), lr=0.0001)

    def loss_function(self):
        return DiceLoss(to_onehot_y=True, softmax=True)

    def train_pre_transforms(self):
        return [
            LoadImaged(keys=("image", "label")),
            AddChanneld(keys=("image", "label")),
            Spacingd(
                keys=("image", "label"),
                pixdim=(1.0, 1.0, 1.0),
                mode=("bilinear", "nearest"),
            ),
            ScaleIntensityRanged(keys="image", a_min=-57, a_max=164, b_min=0.0, b_max=1.0, clip=True),
            CropForegroundd(keys=("image", "label"), source_key="image"),
            RandCropByPosNegLabeld(
                keys=("image", "label"),
                label_key="label",
                spatial_size=(96, 96, 96),
                pos=1,
                neg=1,
                num_samples=4,
                image_key="image",
                image_threshold=0,
            ),
            RandShiftIntensityd(keys="image", offsets=0.1, prob=0.5),
            ToTensord(keys=("image", "label")),
        ]

    def train_post_transforms(self):
        return [
            ToTensord(keys=("pred", "label")),
            Activationsd(keys="pred", softmax=True),
            AsDiscreted(
                keys=("pred", "label"),
                argmax=(True, False),
                to_onehot=True,
                n_classes=2,
            ),
        ]

    def val_pre_transforms(self):
        return [
            LoadImaged(keys=("image", "label")),
            AddChanneld(keys=("image", "label")),
            Spacingd(
                keys=("image", "label"),
                pixdim=(1.0, 1.0, 1.0),
                mode=("bilinear", "nearest"),
            ),
            ScaleIntensityRanged(keys="image", a_min=-57, a_max=164, b_min=0.0, b_max=1.0, clip=True),
            CropForegroundd(keys=("image", "label"), source_key="image"),
            ToTensord(keys=("image", "label")),
        ]

    def val_inferer(self):
        return SlidingWindowInferer(roi_size=(160, 160, 160), sw_batch_size=1, overlap=0.25)
