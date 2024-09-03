# 画像処理
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 手のひら部分に対応するランドマークのインデックス
PALM_LANDMARK_INDICES = [0, 1, 5, 9, 13, 17]


def get_palm_landmarks_average(hand_landmarks, image_shape):
    """手のひらのランドマークの座標の平均値を計算する関数"""
    x_coords = []
    y_coords = []

    # 各手のひらのランドマークを取得し、その座標をリストに追加
    for index in PALM_LANDMARK_INDICES:
        landmark = hand_landmarks.landmark[index]
        x_coords.append(landmark.x)  # 横方向の座標
        y_coords.append(landmark.y)  # 縦方向の座標

    # x座標とy座標の平均を計算
    avg_x = np.mean(x_coords)
    avg_y = np.mean(y_coords)

    return avg_x, avg_y


# game.pyに座標を渡す
def image_process():
    print("ここに画像処理の処理を実装")
    # Webカメラから入力
    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
            model_complexity=0,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        hand_id = 0
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                hand_id = 0
                for hand_landmarks in results.multi_hand_landmarks:
                    # 手のひら部分のランドマークのみを描画
                    for index in PALM_LANDMARK_INDICES:
                        landmark = hand_landmarks.landmark[index]
                        cx, cy = int(
                            landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
                        cv2.circle(image, (cx, cy), 5,
                                   (0, 255, 0), -1)  # 緑色のドットで描画
                    avg_x, avg_y = get_palm_landmarks_average(
                        hand_landmarks, image.shape)
                    print(f"手 ID: {results.multi_handedness[hand_id].classification[0].index}, 手のひらの平均座標: ({
                        avg_x:.2f}, {avg_y:.2f})")
                    cv2.circle(image, (int(avg_x * image.shape[1]),
                                       int(avg_y * image.shape[0])), 5,
                               (0, 255, 0), -1)  # 緑色のドットで描画
                    hand_id += 1  # 手のIDを更新

            cv2.imshow('MediaPipe Palm Only', cv2.flip(image, 1))
            # escキーで終了
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    return [["一人目の", "xy座標"], ["二人目の", "xy座標"]]
