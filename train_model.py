from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8m.pt')

# 训练模型
results = model.train(
    data='combined_dataset/data.yaml',
    epochs=100,
    batch=16,
    imgsz=640,
    workers=4,
    project='runs/train',
    name='yolov8m_screw_nut_washer_box'
)

print("模型训练完成！")
