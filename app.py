import steamlit as st 
import os 
import time
import glob
import os 
from gtts import gTTS
from PIL import Image 

st.title("Weed")
image = Image.open("weed.png")

st.image(image, width=200)
