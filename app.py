
from flask import Flask, render_template, request, send_from_directory
import torch
from diffusers import StableDiffusionPipeline
from uuid import uuid4
from pathlib import Path
import os

app = Flask(__name__)
IMAGE_DIR = Path("static/images")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# Set Hugging Face API token
os.environ["HF_HOME"] = ".cache/huggingface"
os.environ["HF_API_TOKEN"] = "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"

# Detect device
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float32,
    use_auth_token=os.environ["HF_API_TOKEN"]
)
pipe = pipe.to(device)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    try:
        image = pipe(prompt).images[0]
        filename = f"{uuid4().hex}.png"
        filepath = IMAGE_DIR / filename
        image.save(filepath)
        return render_template("index.html", image_url=f"/static/images/{filename}")
    except Exception as e:
        error_message = f"Error generating image: {str(e)}"
        return render_template("index.html", error=error_message)

@app.route("/static/images/<filename>")
def get_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
