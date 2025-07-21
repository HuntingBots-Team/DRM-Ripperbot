FROM python:3.11-slim

# Install system dependencies: ffmpeg (audio/video), wine (for DRM), wget for yt-dlp, and curl for DRM checks
RUN apt-get update && \
    apt-get install -y ffmpeg wine wget curl && \
    apt-get clean

# Install yt-dlp (used in modules/downloader.py)
RUN wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp && \
    chmod a+rx /usr/local/bin/yt-dlp

# Set working directory
WORKDIR /app

# Copy TGHRip source code and requirements.txt
COPY TGHRip /app/TGHRip
COPY requirements.txt /app/requirements.txt

# Create downloads directory
RUN mkdir -p /app/TGHRip/downloads

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Default command to run the Telegram bot (change to main.py or web-dl.py as needed)
CMD ["python3", "bot.py"]
