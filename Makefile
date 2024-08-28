# Dockerコンテナ名
CONTAINER_NAME=air_hockey_container

# Dockerイメージ名
IMAGE_NAME=murakawatakuya/air_hockey:latest # imageをpullした場合
# IMAGE_NAME=air_hockey # imageをbuildした場合

# ディレクトリ
APP_DIR=app
IMAGE_DIR=image
OUTPUT_DIR=output

# C++ソースファイル名
CPP_FILE=$(APP_DIR)/processImage.cpp

# C++実行ファイル名(バイナリファイル名)
EXECUTABLE=processImage

# Pythonスクリプトファイル名
PYTHON_FILE=$(APP_DIR)/processImage.py

# YOLOおよびMediaPipeのスクリプトファイル
YOLO_FILE=$(APP_DIR)/yolo_sample.py
MEDIAPIPE_FILE=$(APP_DIR)/mediapipe_sample.py

# 画像ディレクトリをコンテナにコピーする
copy-images:
	@echo. && echo Copying all images to the container...
	docker cp $(IMAGE_DIR)/. $(CONTAINER_NAME):/app/
	@echo Images copied successfully.

# ソースファイルをコンテナにコピーする（C++用）
copy-files-cpp:
	@echo. && echo Copying C++ source file to the container...
	docker cp $(CPP_FILE) $(CONTAINER_NAME):/app/$(notdir $(CPP_FILE))
	@echo Files copied successfully.

# ソースファイルをコンテナにコピーする（Python用）
copy-files-python:
	@echo. && echo Copying Python script to the container...
	docker cp $(PYTHON_FILE) $(CONTAINER_NAME):/app/$(notdir $(PYTHON_FILE))
	@echo Files copied successfully.

# YOLOサンプルファイルをコンテナにコピーする
copy-files-yolo:
	@echo. && echo Copying YOLO sample file to the container...
	docker cp $(YOLO_FILE) $(CONTAINER_NAME):/app/$(notdir $(YOLO_FILE))
	@echo YOLO sample file copied successfully.

# MediaPipeサンプルファイルをコンテナにコピーする
copy-files-mediapipe:
	@echo. && echo Copying MediaPipe sample file to the container...
	docker cp $(MEDIAPIPE_FILE) $(CONTAINER_NAME):/app/$(notdir $(MEDIAPIPE_FILE))
	@echo MediaPipe sample file copied successfully.

# 出力ディレクトリを作成する
create-output-dir:
	@echo. && echo Creating output directory inside the container...
	docker exec $(CONTAINER_NAME) bash -c "mkdir -p /app/output"

# イメージをプルする
pull-image:
	@echo. && echo Pulling the image...
	docker pull $(IMAGE_NAME)
	@echo Image pulled successfully.

# コンテナを起動する(前回エラーでコンテナが停止していない場合に再起動する)
run-container:
	@echo. && echo Running the container...
	powershell -Command "if (docker ps -q -f name=$(CONTAINER_NAME)) { docker stop $(CONTAINER_NAME) }"
	docker run -dit --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)
	@echo Container started successfully.
	@echo Creating /app directory inside the container...
	docker exec -it $(CONTAINER_NAME) bash -c "mkdir -p /app"

# C++プログラムをコンパイルする
cpp-compile:
	@echo. && echo Compiling cpp program...
	docker exec -it $(CONTAINER_NAME) bash -c "cd /app && g++ -o $(EXECUTABLE) $(notdir $(CPP_FILE)) -I/usr/local/include/opencv4 -L/usr/local/lib -lopencv_core -lopencv_imgcodecs -lopencv_highgui -lopencv_imgproc"
	@echo Program compiled successfully.

# C++プログラムを実行する
run-cpp:
	@echo. && echo Running cpp program...
	docker exec -it $(CONTAINER_NAME) bash -c "LD_LIBRARY_PATH=/usr/local/lib /app/$(EXECUTABLE)"
	@echo Program finished.

# Pythonスクリプトを実行する
run-python:
	@echo. && echo Running python script...
	docker exec -it $(CONTAINER_NAME) bash -c "PYTHONIOENCODING=utf-8 python3 /app/$(notdir $(PYTHON_FILE))"
	@echo Script finished.

# YOLOサンプルを実行する
run-yolo:
	@echo. && echo Running YOLOv5 sample...
	docker exec $(CONTAINER_NAME) bash -c "python3 /app/$(notdir $(YOLO_FILE))"
	@echo YOLOv5 sample finished.

# MediaPipeサンプルを実行する
run-mediapipe:
	@echo. && echo Running MediaPipe sample...
	docker exec $(CONTAINER_NAME) bash -c "python3 /app/$(notdir $(MEDIAPIPE_FILE))"
	@echo MediaPipe sample finished.

# 結果の画像をホストにコピーする
copy-output:
	@echo. && echo Copying output images to the host...
	docker cp $(CONTAINER_NAME):/app/output/. $(OUTPUT_DIR)
	@echo Output images copied successfully.

# コンテナを停止
stop-container:
	@echo. && echo Cleaning up...
	docker stop $(CONTAINER_NAME)
	@echo Cleaned up successfully.

success-message:
	@echo. && echo All process completed successfully.

init: run-container copy-images create-output-dir

finish: stop-container success-message

# C++版の全てのステップをまとめて実行する
cpp: init \
	copy-files-cpp \
	cpp-compile \
	run-cpp \
	copy-output \
	finish

# Python版の全てのステップをまとめて実行する
python: init \
	copy-files-python \
	run-python \
	copy-output \
	finish

# YOLO版の全てのステップをまとめて実行する
yolo: init \
	copy-files-yolo \
	run-yolo \
	copy-output \
	finish

# MediaPipe版の全てのステップをまとめて実行する
mediapipe: init \
	copy-files-mediapipe \
	run-mediapipe \
	copy-output \
	finish
