from flask import Flask, Response, abort
import subprocess

app = Flask(__name__)

@app.route('/<path:upstream_url>')
def get_video_frame(upstream_url):
    # Reconstruct the Azure blob URL from the Nginx proxy pass
    target_url = f"https://{upstream_url}"

    # FFmpeg extracts exactly 1 frame and outputs it directly as a JPEG stream
    command = [
        'ffmpeg',
        '-hide_banner', '-loglevel', 'error',
        '-protocol_whitelist', 'file,http,https,tcp,tls,crypto',
        '-i', target_url,
        '-vframes', '1',
        '-f', 'image2pipe',
        '-c:v', 'mjpeg',
        '-'
    ]

    try:
        # Execute FFmpeg and capture the image binary
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        if process.returncode != 0:
            return abort(500, description="FFmpeg processing failed")

        return Response(process.stdout, mimetype='image/jpeg')
    except Exception as e:
        return abort(500, description=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
