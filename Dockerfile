FROM python:3.9-slim-buster

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
    libcanberra-gtk-module libcanberra-gtk3-module tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone, build and install OpenCV for C++
RUN git clone https://github.com/opencv/opencv.git && \
    cd /opencv && mkdir build && cd build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local .. && \
    make -j8 && \
    make install && \
    rm -rf /opencv

# Install Python packages for YOLOv5 and MediaPipe in one command to optimize image layers
RUN pip install --no-cache-dir \
    torch torchvision torchaudio \
    opencv-python-headless mediapipe \
    matplotlib requests yolov5

# Create a directory for your application
WORKDIR /app

# Command to start the container (you can override this in your Makefile or docker run command)
CMD ["bash"]
