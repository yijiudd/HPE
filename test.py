import fiftyone as fo
import fiftyone.zoo as foz
import mimetypes
mimetypes.init() 
mimetypes.add_type('application/javascript', '.js')
fo.config.dataset_zoo_dir="E:\\fiftyone_zoo"# Path to the directory where datasets are downloaded
dataset = foz.load_zoo_dataset("coco-2017",split="validation",label_types=["keypoints"])

dataset = fo.Dataset.from_dir(
    dataset_dir=r'E:\\fiftyone_zoo\\coco-2017\\validation' ,
    labels_path=r'E:\\fiftyone_zoo\\coco-2017\\raw\\person_keypoints_val2017.json',
    dataset_type=fo.types.COCODetectionDataset,
    label_types=['detections', 'segmentations', 'keypoints'],
)
if __name__ == "__main__":
    # Ensures that the App processes are safely launched on Windows
    session = fo.launch_app(dataset,desktop=True)
    session.wait()