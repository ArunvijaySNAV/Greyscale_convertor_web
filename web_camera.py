import streamlit as st
from PIL import Image

st.title("Auto Grey-scale image")
st.subheader("Converts original image to grey-scale image")


with st.expander("Start camera"):
     cam_img = st.camera_input("Devices web.camera")
     st.write("Camera is active now!")

if cam_img:
    img = Image.open(cam_img)
    grey_scale = img.convert("L")
    st.image(grey_scale)

