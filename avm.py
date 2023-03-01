from .dota import DOTADataset
from .builder import ROTATED_DATASETS


@ROTATED_DATASETS.register_module()
class AVMDataset(DOTADataset):
    """AVM dataset for detection.

    Args:
        ann_file (str): Annotation file path.
        pipeline (list[dict]): Processing pipeline.
        version (str, optional): Angle representations. Defaults to 'oc'.
        difficulty (bool, optional): The difficulty threshold of GT.
    """
    CLASSES = ('unavailable_parking_lines', 'available_parking_lines')

    PALETTE = [(255, 0, 0), (0, 0, 255)]

    def __init__(self,
                 ann_file,
                 pipeline,
                 version='oc',
                 difficulty=100,
                 **kwargs):

        super(AVMDataset, self).__init__(ann_file, pipeline, version, difficulty, **kwargs)
