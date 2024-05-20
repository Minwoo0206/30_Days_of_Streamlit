import os
import csv
import streamlit as st
from pathlib import Path
from PIL import Image

image_folder = Path("images")
image_files = list(image_folder.glob('*'))
questions = []
for idx, image_dir in enumerate(image_files):   
    image = Image.open(image_dir)
    st.image(image)
    question = st.slider(f"'realism' or 'illustration'?(Q{idx})", 0, 10, 5)
    questions.append(question)

if st.button('submit'):
    with open("./results/result.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([questions])