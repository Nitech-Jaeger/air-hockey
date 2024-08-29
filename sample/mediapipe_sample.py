import cv2
import mediapipe as mp
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

img_path = 'image/image3.jpg'
output_path = 'output/mediapipe_output.jpg'
img = cv2.imread(img_path)

# 画像が読み込めない場合のエラーチェック
if img is None:
    print(f"Failed to load image {img_path}")
    exit()

# BGRからRGBに変換
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 手の検出を実行
results = hands.process(img_rgb)

# 検出された手のランドマークを描画
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# 出力ディレクトリが存在しない場合は作成
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# 検出結果を保存
cv2.imwrite(output_path, img)

print(f"MediaPipe hand detection completed. Results saved as {output_path}.")
