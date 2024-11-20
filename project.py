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
    # Check if the file is uploaded
    if uploaded_file:
        try:
            # Open the image using PIL
            img = Image.open(uploaded_file)
            img_np = np.array(img)

            # Check if width and height are valid numbers
            if not width.isdigit() or not height.isdigit():
                st.error("Width and Height must be valid numbers.")
            else:
                width = int(width)
                height = int(height)

                # Ensure width and height are greater than 0
                if width <= 0 or height <= 0:
                    st.error("Width and Height must be greater than 0.")
                else:
                    # Resize the image
                    resize_img = cv2.resize(img_np, (width, height), interpolation=INTER_AREA)
                    
                    # Display resized image
                    st.image(resize_img, caption="Resized Image")
        except:
            st.error("something is wrong")
