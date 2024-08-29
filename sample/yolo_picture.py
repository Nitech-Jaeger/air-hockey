import torch
import cv2
import os

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img_path = 'image/image3.jpg'
output_path = 'output/yolo_output.jpg'

img = cv2.imread(img_path)

if img is None:
    print(f"Failed to load image {img_path}")
    exit()

# 推論の実行
results = model(img)

# 推論結果の描画
annotated_img = results.render()[0]

# 出力ディレクトリが存在しない場合は作成
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# 結果画像を指定のパスに保存
cv2.imwrite(output_path, annotated_img)

print(f"YOLOv5 inference completed. Results saved as {output_path}.")
