# ゲームクラスの制御
import image_process
import random

def game_controller():
    print("ここにゲームの処理を実装")
    
    while True:
        # image_process.pyから座標を受け取る
        coordinate = image_process.image_process()
        print(coordinate)
        
        # ゲームの処理を実装
        
        # 終わっちゃおうかな～(10%の確率で終了)
        if random.random() < 0.1:
            return
