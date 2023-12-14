import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

model = genai.GenerativeModel("gemini-pro-vision")

st.set_page_config(layout="wide")
st.title("Gemini Webpage Builder")
st.write("Made with ❄️ from MN.")
secret = st.text_input("Enter your Gemini API key", type="password")
if secret:
    genai.configure(api_key=secret)
    st.subheader("Upload a sketch, wireframe, or webpage. Must be image (.jpg or .png).")

    upload_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
    if upload_file is not None:
        image = Image.open(upload_file)
        try:
            response = model.generate_content([
                "Write both the necessary HTML and CSS to create this webpage design. If the image doesn't appear to be a webpage, you can return 'This is not a webpage'. ",
                "Make sure to provide both the HTML and CSS for the design. Ensure that the output is clean, elegant, well-formatted, well-designed, and markdown/code can be copied easily.",
                image
            ]).text
        except Exception as e:
            response = e
        col1, col2 = st.columns(2)
        col1.image(image, use_column_width=True)
        col2.write(response)