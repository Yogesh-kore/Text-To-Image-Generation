# Text-to-Image Generator

A Flask web application that generates images from text prompts using Stable Diffusion AI model.

## Features

- Text-to-image generation using Stability AI's SD-Turbo model
- Simple and intuitive web interface
- GPU acceleration (when available)
- Error handling for robust operation
- Image download functionality

## Prerequisites

- Python 3.8 or higher
- PyTorch
- Flask
- Diffusers library
- Hugging Face account and API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Yogesh-kore/Text-To-Image-Generation.git
cd Text-To-Image-Generation
```

2. Install the required packages:

```bash
pip install flask torch diffusers transformers accelerate
```

3. Set up your Hugging Face API key:

Replace the API key in `app.py` with your own key from [Hugging Face](https://huggingface.co/settings/tokens).

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and navigate to:
