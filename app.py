import streamlit as st
from crew import process_file
import pypandoc
import os

# Function to save uploaded file
def save_uploaded_file(uploaded_file):
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("tempDir", uploaded_file.name)

# Function to convert markdown to DOCX
def convert_markdown_to_docx(markdown_content, output_path):
    pypandoc.convert_text(markdown_content, 'docx', format='md', outputfile=output_path)
    return output_path

# Streamlit app
st.title("Markdown to DOCX Converter")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=['pdf'])

if uploaded_file is not None:
    # Save uploaded file
    file_path = save_uploaded_file(uploaded_file)

    # Process file
    markdown_content = process_file(file_path)

    # Convert to DOCX
    output_path = "output.docx"
    convert_markdown_to_docx(markdown_content, output_path)

    # Read DOCX file
    with open(output_path, "rb") as f:
        docx_file = f.read()

    # Download button
    st.download_button(
        label="Download DOCX",
        data=docx_file,
        file_name="output.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Ensure tempDir exists
if not os.path.exists("tempDir"):
    os.makedirs("tempDir")
