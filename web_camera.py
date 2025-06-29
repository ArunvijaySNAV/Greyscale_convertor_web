import streamlit as st
from PIL import Image

st.title("Auto Grey-scale image")
st.subheader("Converts original image to grey-scale image")

st.write("<b>To access camera:</b>", unsafe_allow_html=True)
with st.expander("Start camera"):
     cam_img = st.camera_input("Devices web.camera")
     st.write("Camera is active now!")

if cam_img:
    img = Image.open(cam_img)
    grey_scale = img.convert("L")
    st.image(grey_scale)

st.write("<b>To access files:pip</b>", unsafe_allow_html=True)
with st.expander("Upload image"):
    img_doc = st.file_uploader("Devices files")
    st.write("Devices files are active now!")

if img_doc:
    img = Image.open(img_doc)
    grey_scale = img.convert("L")
    st.image(grey_scale)