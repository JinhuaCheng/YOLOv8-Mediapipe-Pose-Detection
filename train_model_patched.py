import torch
import torch.serialization

# 保存原始的torch.load函数
original_load = torch.load

# 创建一个新的load函数，默认weights_only=False
def patched_load(f, map_location=None, pickle_module=torch.serialization.pickle, **kwargs):
    if 'weights_only' not in kwargs:
        kwargs['weights_only'] = False
    return original_load(f, map_location=map_location, pickle_module=pickle_module, **kwargs)

# 应用猴子补丁
torch.load = patched_load

# 现在导入ultralytics并训练模型
from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8m.pt')

# 训练模型
results = model.train(
    data='d:\\bishe\\YOLOv8-Mediapipe-Pose-Detection\\combined_dataset\\data.yaml',
    epochs=100,
    batch=16,
    imgsz=640,
    workers=4,
    project='runs/train',
    name='yolov8m_screw_nut_washer_box'
)

print("模型训练完成！")
