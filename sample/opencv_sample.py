import os
import cv2

img1_path = 'image/image1.jpg'
img2_path = 'image/image2.jpg'
output_path = 'output/python_output.jpg'

img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

if img1 is None or img2 is None:
  print("Cannot read image file.")
  exit()

# 差分画像を計算
diff = cv2.absdiff(img1, img2)

# 差分画像を閾値処理 (見やすくするため)
_, thresh = cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY)

# 差分画像を保存
cv2.imwrite(output_path, thresh)

print(f"Image processing is successfully done. Output image is saved as '{output_path}'.")
