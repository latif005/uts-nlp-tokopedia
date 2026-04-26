import gradio as gr
import joblib
import re
import nltk
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# --- BARIS INI WAJIB DITAMBAHKAN UNTUK SERVER ---
nltk.download('punkt')
nltk.download('punkt_tab')
# ------------------------------------------------

# 1. Load Model dan Vectorizer
model = joblib.load('best_model_tfidf.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# 2. Siapkan fungsi Preprocessing (Sastrawi)
factory_stem = StemmerFactory()
stemmer = factory_stem.create_stemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|@\w+|#\w+|[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    # Catatan: Di deployment kita skip stopword agar ringan, langsung stemming
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# 3. Fungsi Prediksis
def predict(review):
    cleaned_review = clean_text(review)
    vectorized = vectorizer.transform([cleaned_review])
    prediction = model.predict(vectorized)[0]
    
    return "Positif 🟢" if prediction == 1 else "Negatif 🔴", cleaned_review

# 4. Bangun UI Gradio
interface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=3, placeholder="Masukkan ulasan produk..."),
    outputs=[
        gr.Textbox(label="Hasil Prediksi Sentimen"),
        gr.Textbox(label="Teks Setelah Preprocessing")
    ],
    title="Sentimen Analisis Ulasan Tokopedia"
)

if __name__ == "__main__":
    interface.launch()