
import numpy as np
import pandas as pd
import cv2
from cv2 import INTER_AREA
import streamlit as st
from PIL import Image
st.title("Image Resizer by PD")
width=st.text_input("choose width")
height=st.text_input("choose height")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
button=st.button("Resize",icon="📷")
if button:
  if uploaded_file:
     Image = Image.open(uploaded_file)
     img_np = np.array(Image)
     width=int(width)
     height=int(height)
     resize_img=cv2.resize(img_np,(width,height),interpolation=cv2.INTER_AREA)
     st.image(resize_img, caption="Resized Image")
