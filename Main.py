import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import io

# Streamlit sayfa ayarları
st.set_page_config(
    page_title="Python ile Veri Görselleştirme",
    page_icon="🍍",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()
    return all_page_text

# Sidebar başlığı ve menü
st.sidebar.title('Numeroloji Hesaplama Uygulaması')
menu = ["Ana Sayfa", "Doğum Tarihi Hesaplama", "İsim Hesaplama", "Sentez Hesaplama"]
choice = st.sidebar.selectbox("Menü", menu)

if choice == "Ana Sayfa":
    st.subheader("Ana Sayfa")
    image_file = st.file_uploader("Yüklenmiş Görsel", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        file_details = {
            "filename": image_file.name,
            "file_type": image_file.type,
            "file_size": image_file.size
        }
        st.write(file_details)
        st.image(load_image(image_file), caption="Yüklenen Görsel")

elif choice == "Doğum Tarihi Hesaplama":
    st.subheader("Doğum Tarihi Hesaplama")
    # Buraya Doğum Tarihi Hesaplama ile ilgili kodlar eklenecek

elif choice == "İsim Hesaplama":
    st.subheader("İsim Hesaplama")
    # Buraya İsim Hesaplama ile ilgili kodlar eklenecek

elif choice == "Sentez Hesaplama":
    st.subheader("Sentez Hesaplama")
    # Buraya Sentez Hesaplama ile ilgili kodlar eklenecek

# Streamlit uygulamasını başlatma
if __name__ == "__main__":
    st.set_option('server.runOnSave', True)
    st.write("Uygulama Başlatıldı")

