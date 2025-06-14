
import streamlit as st
st.set_page_config(page_title="Gerador de Letras Multilingue", layout="centered")

import os
import json
import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.preprocessing.text import Tokenizer

diretorio_usado = "/content/drive/MyDrive/Bossa_Nova"

@st.cache_resource
def load_all_models_and_tokenizers(model_dir=f"{diretorio_usado}/"):
    modelos = {}
    tokenizers = {}

    def sparse_cat_loss(y_true, y_pred):
        return sparse_categorical_crossentropy(y_true, y_pred)

    for arquivo in os.listdir(model_dir):
        if arquivo.endswith(".keras") and arquivo.startswith("bn_"):
            nome = arquivo.replace("bn_", "").replace(".keras", "")
            try:
                modelos[nome] = load_model(
                    os.path.join(model_dir, arquivo),
                    custom_objects={"sparse_cat_loss": sparse_cat_loss}
                )
            except Exception as e:
                st.warning(f"Erro ao carregar modelo {arquivo}: {e}")

        elif arquivo.endswith(".json") and arquivo.startswith("tokenizer_"):
            nome = arquivo.replace("tokenizer_", "").replace(".json", "")
            try:
                with open(os.path.join(model_dir, arquivo), "r", encoding="utf-8") as f:
                    data = json.load(f)
                    tok = Tokenizer()
                    tok.word_index = data["word_index"]
                    tokenizers[nome] = tok
            except Exception as e:
                st.warning(f"Erro ao carregar tokenizer {arquivo}: {e}")

    return modelos, tokenizers

modelos, tokenizers = load_all_models_and_tokenizers()

if not modelos:
    st.error("❌ Nenhum modelo foi carregado. Verifique se os arquivos .keras estão presentes e corretos.")
    st.stop()

if not tokenizers:
    st.error("❌ Nenhum tokenizer foi carregado. Verifique os arquivos tokenizer_*.json.")
    st.stop()

#st.write("🧠 Modelos carregados:", list(modelos.keys()))
#st.write("🧾 Tokenizers carregados:", list(tokenizers.keys()))

st.title("🎶 Gerador de Letras de Música")

idioma = st.selectbox("🌍 Escolha o modelo/idioma", sorted(modelos.keys()))

start_seed = st.text_input("🔤 Palavra/frase inicial", "amor")
gen_size = st.slider("📏 Tamanho da música", 10, 300, 100, step=10)
temp = st.slider("🌡️ Temperatura", 0.1, 1.0, 0.55, step=0.05)

def generate_text(model, tokenizer, start_seed, gen_size=100, temp=1.0):
    if start_seed not in tokenizer.word_index:
        return None  # Palavra não reconhecida

    input_eval = tokenizer.texts_to_sequences([start_seed])[0]
    input_eval = tf.expand_dims(input_eval, 0)
    text_generated = []

    for _ in range(gen_size):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temp
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)

        predicted_word = next((word for word, index in tokenizer.word_index.items() if index == predicted_id), '')
        text_generated.append(predicted_word)

    return start_seed + ' ' + ' '.join(text_generated)

if st.button("🎤 Gerar letra"):
    with st.spinner("Gerando..."):
        modelo_escolhido = modelos[idioma]

        if idioma not in tokenizers:
            st.error(f"❌ Tokenizer para o modelo '{idioma}' não encontrado.")
        else:
            tokenizer_escolhido = tokenizers[idioma]
            letra = generate_text(modelo_escolhido, tokenizer_escolhido, start_seed, gen_size, temp)

            if letra is None:
                st.warning("⚠️ A palavra inicial não está no vocabulário do modelo. Tente outra.")
            else:
                st.success("✅ Letra gerada com sucesso!")
                st.text_area("🎵 Letra", letra, height=300)

