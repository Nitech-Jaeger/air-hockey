import warnings
import torch
import cv2

warnings.filterwarnings("ignore", category=FutureWarning)

print(torch.cuda.is_available())  # TrueならGPUが利用可能
print(torch.cuda.device_count())  # 利用可能なGPUの数
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))  # GPUの名前を表示

# CUDAが利用可能かチェック
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using {device} device')

# YOLOv5の事前学習済みモデルをロードし、GPUへ移動
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device)

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

# リサイズ倍率を指定
resize_factor = 1.7  # ここで倍率を指定（例えば2.0で2倍）

while True:
    # フレームをキャプチャ
    ret, frame = cap.read()
    if not ret:
        break

    # フレームをRGBに変換 (YOLOv5が期待するフォーマット)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # フレームをテンソルに変換してGPUに転送
    results = model(frame_rgb)

    # 検出された物体を処理
    for *box, conf, cls in results.xyxy[0]:
        x1, y1, x2, y2 = map(int, box)
        label = model.names[int(cls)]
        confidence = f'{conf:.2f}'

        # 検出された物体のラベルと信頼度を表示
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f'{label} {confidence}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # フレームを指定した倍率でリサイズ
    frame_resized = cv2.resize(frame, None, fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_LINEAR)

    # 結果を表示
    cv2.imshow('YOLOv5 Camera Detection', frame_resized)

    # 'q'キーを押すとループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラとウィンドウを解放
cap.release()
cv2.destroyAllWindows()
