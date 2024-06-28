import streamlit as st
import os

# Title of the app
st.title('Hello Streamlit!')

# Displaying text
st.text("I like Python and Streamlit")

# Displaying an image with a caption
image_path = "Image.jpg"  # Ensure the image file is in the same directory or provide the correct path
if os.path.exists(image_path):
    st.image(image_path, caption="Nature's View", use_column_width=True)
else:
    st.error(f"Image file '{image_path}' not found.")

# Button widget
if st.button("Click Me"):
    st.write("Button clicked!")

# Slider widget
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, " years old")
