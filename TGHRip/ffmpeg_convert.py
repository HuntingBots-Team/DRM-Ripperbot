import os
import subprocess
import uuid

def rip_stream(url: str, key: str, out_format: str = "mp4", save_dir="downloads") -> str:
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    base_name = f"rip_{uuid.uuid4().hex[:8]}"
    decrypted_path = os.path.join(save_dir, f"{base_name}.ts")
    final_path = os.path.join(save_dir, f"{base_name}.{out_format}")

    print(f"[INFO] Ripping stream from: {url}")

    streamlink_command = [
        "streamlink-drm", url,
        "best",
        "--stream-url",
        "--key", key
    ]

    try:
        result = subprocess.run(streamlink_command, capture_output=True, text=True, check=True)
        decrypted_url = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(f"Streamlink DRM failed: {e.stderr}")

    ffmpeg_command = [
        "ffmpeg", "-i", decrypted_url,
        "-c:v", "copy", "-c:a", "copy",
        final_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"FFmpeg conversion failed: {e.stderr}")

    return final_path
