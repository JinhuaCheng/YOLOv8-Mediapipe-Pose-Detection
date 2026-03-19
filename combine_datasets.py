import os
import shutil
import random

# 数据集路径
base_dir = r'd:\bishe\YOLOv8-Mediapipe-Pose-Detection\数据集'
combined_dir = r'd:\bishe\YOLOv8-Mediapipe-Pose-Detection\combined_dataset'

# 类别映射
class_map = {
    'box': 0,
    'nut': 1,
    'screw': 2,
    'washer': 3
}

# 遍历每个类别
for class_name, class_id in class_map.items():
    class_dir = os.path.join(base_dir, class_name)
    
    # 遍历train、valid、test目录
    for split in ['train', 'valid', 'test']:
        src_images_dir = os.path.join(class_dir, split, 'images')
        src_labels_dir = os.path.join(class_dir, split, 'labels')
        
        # 检查目录是否存在
        if not os.path.exists(src_images_dir) or not os.path.exists(src_labels_dir):
            continue
        
        # 目标目录
        dst_images_dir = os.path.join(combined_dir, split, 'images')
        dst_labels_dir = os.path.join(combined_dir, split, 'labels')
        
        # 获取所有图像文件
        image_files = [f for f in os.listdir(src_images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        for image_file in image_files:
            # 图像文件路径
            src_image_path = os.path.join(src_images_dir, image_file)
            
            # 标签文件路径
            label_file = os.path.splitext(image_file)[0] + '.txt'
            src_label_path = os.path.join(src_labels_dir, label_file)
            
            # 检查标签文件是否存在
            if not os.path.exists(src_label_path):
                continue
            
            # 生成新的文件名，确保唯一性
            new_filename = f"{class_name}_{os.path.splitext(image_file)[0]}_{random.randint(1000, 9999)}"
            new_image_file = new_filename + os.path.splitext(image_file)[1]
            new_label_file = new_filename + '.txt'
            
            # 复制图像文件
            dst_image_path = os.path.join(dst_images_dir, new_image_file)
            shutil.copy2(src_image_path, dst_image_path)
            
            # 处理标签文件
            dst_label_path = os.path.join(dst_labels_dir, new_label_file)
            
            with open(src_label_path, 'r') as f:
                lines = f.readlines()
            
            with open(dst_label_path, 'w') as f:
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) >= 5:
                        # 替换类别ID
                        parts[0] = str(class_id)
                        # 写入新的标签行
                        f.write(' '.join(parts) + '\n')

print("数据集合并完成！")
