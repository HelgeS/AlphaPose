from .coco_det import Mscoco_det
from .concat_dataset import ConcatDataset
from .custom import CustomDataset
from .mscoco import Mscoco
from .mpii import Mpii
from .halpe_26 import Halpe_26
from .halpe_136 import Halpe_136
from .halpe_136_det import Halpe_136_det
from .halpe_26_det import Halpe_26_det
from .ski2dpose import Ski2dpose, Ski2dposeWithCoG
from .ski2dpose_det import Ski2dpose_det, Ski2dposeWithCoG_det

__all__ = [
    "CustomDataset",
    "Halpe_136",
    "Halpe_26_det",
    "Halpe_136_det",
    "Halpe_26",
    "Mscoco",
    "Mscoco_det",
    "Mpii",
    "ConcatDataset",
    "coco_wholebody",
    "coco_wholebody_det",
    "Ski2dpose",
    "Ski2dpose_det",
    "Ski2dposeWithCoG",
    "Ski2dposeWithCoG_det",
]
