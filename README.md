Analisis Sentimen Ulasan Produk Tokopedia (NLP Project)
Repositori ini berisi proyek UTS untuk mata kuliah Natural Language Processing (NLP). Proyek ini bertujuan untuk membangun model Machine Learning yang mampu mendeteksi sentimen (positif atau negatif) dari ulasan produk di platform Tokopedia menggunakan berbagai teknik ekstraksi fitur dan algoritma klasifikasi.

📌 Deskripsi Proyek
Proyek ini mengimplementasikan end-to-end NLP pipeline, mulai dari pembersihan data teks hingga deployment aplikasi sederhana menggunakan Gradio. Masalah utama yang diselesaikan adalah ketidakseimbangan data ulasan e-commerce, di mana ulasan positif jauh lebih banyak daripada negatif.

📊 Dataset
Dataset yang digunakan adalah ulasan produk Tokopedia tahun 2019.

Jumlah Data: >10.000 ulasan (setelah diseimbangkan 50:50 antara positif dan negatif).

Sumber Dataset: https://drive.google.com/file/d/1mehsF-MzTYVnTKnk3AmOUpCydCC19lbu/view?usp=sharing

🛠️ NLP Pipeline
Pipeline yang diimplementasikan meliputi:

Preprocessing:

Case Folding (Lowercase).

Cleaning (Menghapus URL, Mention, Hashtag, angka, dan tanda baca).

Tokenization (NLTK).

Stopword Removal (Sastrawi).

Stemming (Sastrawi untuk bahasa Indonesia).

Feature Extraction:

TF-IDF (Term Frequency-Inverse Document Frequency).

Word Embedding (Word2Vec - Average Vector).

Modeling:

Naive Bayes.

Logistic Regression (dengan class_weight='balanced').

Support Vector Machine (SVM).

📈 Hasil Evaluasi
Berdasarkan perbandingan, model terbaik yang dihasilkan adalah Logistic Regression dengan TF-IDF, mencapai performa yang seimbang untuk kedua kelas:

Accuracy: [0.78]

F1-Score (Negatif): [0.78]

F1-Score (Positif): [0.77]

🚀 App Deployment
Aplikasi telah di-deploy menggunakan Gradio dan dijalankan di Hugging Face. Kamu bisa mencoba model ini secara interaktif melalui tautan berikut:
https://huggingface.co/spaces/elw354/sentimen-tokopedia
