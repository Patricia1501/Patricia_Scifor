import streamlit as st 


st.title('Hello Streamlit!')
st.text("I like Python and Streamlit")

st.image("Image.jpg")
st.caption("Nature's View")
st.button("Click Me")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")
