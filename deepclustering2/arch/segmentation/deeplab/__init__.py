"""
This folder is modified based on the deep lab repo of: https://github.com/kazuto1011/deeplab-pytorch
"""

from .deeplabv2 import *
from .deeplabv3 import *
from .deeplabv3plus import *
from .msc import *
from .resnet import *

__all__ = ["DeepLabV3", "DeepLabV3Plus", "DeepLabV2"]


def DeepLabV2_ResNet101_MSC(num_classes):
    return MSC(
        scale=DeepLabV2(
            num_classes=num_classes, n_blocks=[3, 4, 23, 3], pyramids=[6, 12, 18, 24]
        ),
        pyramids=[0.5, 0.75],
    )


def DeepLabV2S_ResNet101_MSC(num_classes):
    return MSC(
        scale=DeepLabV2(
            num_classes=num_classes, n_blocks=[3, 4, 23, 3], pyramids=[3, 6, 9, 12]
        ),
        pyramids=[0.5, 0.75],
    )


def DeepLabV3_ResNet101_MSC(n_classes, output_stride):
    if output_stride == 16:
        pyramids = [6, 12, 18]
    elif output_stride == 8:
        pyramids = [12, 24, 36]
    else:
        NotImplementedError

    return MSC(
        scale=DeepLabV3(
            n_classes=n_classes,
            n_blocks=[3, 4, 23, 3],
            pyramids=pyramids,
            grids=[1, 2, 4],
            output_stride=output_stride,
        ),
        pyramids=[0.5, 0.75],
    )


def DeepLabV3Plus_ResNet101_MSC(n_classes, output_stride):
    if output_stride == 16:
        pyramids = [6, 12, 18]
    elif output_stride == 8:
        pyramids = [12, 24, 36]
    else:
        NotImplementedError

    return MSC(
        scale=DeepLabV3Plus(
            n_classes=n_classes,
            n_blocks=[3, 4, 23, 3],
            pyramids=pyramids,
            grids=[1, 2, 4],
            output_stride=output_stride,
        ),
        pyramids=[0.5, 0.75],
    )
