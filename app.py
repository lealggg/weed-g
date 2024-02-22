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


try:
    os.mkdir("temp")
except:
    pass

st.subheader("texto a audio")
st.write("La marihuana también llamada weed, herb, pot, grass, bud, ganja, Mary Jane y una gran cantidad de otros términos callejeros")
