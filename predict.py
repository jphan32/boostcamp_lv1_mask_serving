import streamlit as st
from header import config

import io
import torch
from torchvision import transforms
from PIL import Image

@st.experimental_singleton(show_spinner=True)
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.load(config['models'][0]['model_path'])
    model.to(device)
    model.eval()
    return model

def get_prediction(model, image_bytes: bytes):
    device = torch.cuda.current_device()

    transform_image = transforms.Compose([
                                transforms.RandomResizedCrop((350, 350), interpolation=transforms.InterpolationMode.BICUBIC),
                                transforms.ToTensor()
                            ])

    image = Image.open(io.BytesIO(image_bytes))
    image = transform_image(image).to(device).unsqueeze(0)

    outputs = model(image)
    preds = torch.argmax(outputs, dim=-1)

    return preds
