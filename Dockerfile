# Build stage
FROM python:3.9-slim-buster as build

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
    libcanberra-gtk-module libcanberra-gtk3-module tzdata

# Clone, build and install OpenCV for C++
RUN git clone https://github.com/opencv/opencv.git && \
    cd /opencv && mkdir build && cd build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local .. && \
    make -j8 && \
    make install

# Final stage
FROM python:3.9-slim-buster

# Copy the built OpenCV from the build stage
COPY --from=build /usr/local /usr/local

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev \
    libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
    libcanberra-gtk-module libcanberra-gtk3-module tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    torch torchvision torchaudio \
    mediapipe \
    matplotlib requests yolov5

# Create a directory for your application
WORKDIR /app

# Command to start the container (you can override this in your Makefile or docker run command)
CMD ["bash"]

# ビルド用コマンド
# docker build -t air_hockey .
