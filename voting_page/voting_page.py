import os
import csv
import streamlit as st
from PIL import Image

images_dir = "images/"
questions = []
for idx, image_dir in enumerate(os.listdir(images_dir)):   
    image = Image.open(images_dir+image_dir)
    st.image(image)
    question = st.slider(f"'realism' or 'illustration'?(Q{idx})", 0, 10, 5)
    questions.append(question)

if st.button('submit'):
    with open("results/result.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([questions])