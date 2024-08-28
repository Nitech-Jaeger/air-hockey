import torch
import cv2
import os
import shutil

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

application_path = '/app'
img_path = application_path + '/image3.jpg'
output_dir = application_path + '/output'
img = cv2.imread(img_path)

if img is None:
    print(f"Failed to load image {img_path}")
    exit()

# 推論の実行
results = model(img)

# YOLOv5のデフォルト出力先ディレクトリ
default_output_dir = 'runs/detect/exp'

# 推論結果を一時ディレクトリに保存
results.save()
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'yolo_output.jpg')
source_image = os.path.join(default_output_dir, 'image0.jpg')

# ファイルの移動とリネーム
shutil.move(source_image, output_path)

# 不要なディレクトリを削除
shutil.rmtree(default_output_dir)

print(f"YOLOv5 inference completed. Results saved as {output_path}.")
