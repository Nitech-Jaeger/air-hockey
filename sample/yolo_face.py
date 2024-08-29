import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

while True:
    # フレームをキャプチャ
    ret, frame = cap.read()
    if not ret:
        break

    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顔を検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 検出された顔の座標を出力
    for (x, y, w, h) in faces:
        print(f"顔の座標: x={x}, y={y}, w={w}, h={h}")
        # 顔の周りに矩形を描画
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 結果を表示
    cv2.imshow('YOLOv5 Camera Detection', frame)

    # 'q'キーを押すとループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラとウィンドウを解放
cap.release()
cv2.destroyAllWindows()
