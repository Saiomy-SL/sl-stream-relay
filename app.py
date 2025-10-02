from flask import Flask, Response
import requests

app = Flask(__name__)

# Replace this URL with your HTTPS Shoutcast stream
STREAM_URL = "https://s3.free-shoutcast.com/stream/18062"

@app.route("/stream.mp3")
def stream():
    def generate():
        with requests.get(STREAM_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
    return Response(generate(), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
