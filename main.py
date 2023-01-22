import sys

from video_tools.video_info import VideoInfo
from geometry.geometry import *  
from video_tools.video_info import VideoInfo
from video_tools.sink import *

from ultralytics import YOLO


from detection.detection_tools import Detections, BoxAnnotator
from draw.color import ColorPalette


box_annotator = BoxAnnotator(color=ColorPalette(), thickness=2, text_thickness=2, text_scale=1)

PATH_TO_FRAME = "dataset/1.jpg"
PATH_TO_MODEL = "dataset/best.pt"

model = YOLO(PATH_TO_MODEL)
results = model(PATH_TO_FRAME)
detections = Detections(
            xyxy=results[0].boxes.xyxy.cpu().numpy(),
            confidence=results[0].boxes.conf.cpu().numpy(),
            class_id=results[0].boxes.cls.cpu().numpy().astype(int)
        )
detections.group_racks() 
print(detections) 



def main():
    pass

if __name__ == "__main__":
    main()