import streamlit as st
from PIL import Image
from deep_translator import GoogleTranslator

# Mostrar imagen
image = Image.open("fbdc6506-559e-4796-b769-2fa123b0e827.jpg")
st.image(image, width=200)

# Título estilizado
st.markdown("<h1 style='color:#d36b7b;'>🌐 Traductor Encantado 💬</h1>", unsafe_allow_html=True)

# Descripción
st.markdown("Traduce tus pensamientos al idioma que desees con un solo clic. Ideal para tus cartas, ideas o secretos globales. ✨")

# Entradas del usuario
text = st.text_area("✍️ Escribe el texto que deseas traducir:")
source_lang = st.selectbox("🌎 Idioma original:", ["auto", "en", "es", "fr", "de", "it", "ko", "ja"])
target_lang = st.selectbox("🎯 Idioma destino:", ["en", "es", "fr", "de", "it", "ko", "ja"])

# Botón para traducir
if st.button("🔁 Traducir"):
    if text.strip() != "":
        translation = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.markdown("### ✨ Traducción:")
        st.success(translation)
    else:
        st.warning("Por favor escribe algo para traducir.")

# Footer personalizado
st.markdown("---")
st.markdown("<small style='color: gray;'>Hecho con ❤️ por miminsouls</small>", unsafe_allow_html=True)
