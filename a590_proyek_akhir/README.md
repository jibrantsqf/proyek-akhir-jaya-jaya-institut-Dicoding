# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan yang berdiri sejak tahun 2000 dan memiliki reputasi baik. Namun, mereka menghadapi masalah tingginya angka *dropout* mahasiswa, yang berdampak buruk pada performa institusi secara keseluruhan. 

### Permasalahan Bisnis
Institusi kesulitan mengidentifikasi mahasiswa yang memiliki risiko *dropout* sejak dini. Akibatnya, mahasiswa yang rentan tidak mendapatkan bimbingan khusus atau intervensi akademik yang tepat pada waktunya.

### Cakupan Proyek
Proyek ini mencakup:
1. **Analisis Eksploratif Data (EDA)**: Menemukan faktor-faktor utama yang berkorelasi dengan angka *dropout*.
2. **Pembuatan Business Dashboard**: Memvisualisasikan metrik kinerja akademik dan status mahasiswa untuk dipantau secara langsung oleh pihak manajemen institusi.
3. **Membangun Model Machine Learning**: Membuat model prediktif (Random Forest Classifier) yang dapat memprediksi risiko *dropout* mahasiswa berdasarkan data historis.
4. **Deploy Prototype**: Mengemas model Machine Learning dalam antarmuka berbasis web menggunakan Streamlit.

### Persiapan

Sumber data: Data historis kinerja akademik mahasiswa dan profil demografi dari Dicoding.

Setup environment:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Business Dashboard
Visualisasi performa akademik dan faktor risiko mahasiswa disajikan dalam Business Dashboard interaktif menggunakan Looker Studio:

- **Tautan Dashboard Looker Studio**: [Dashboard Pemantauan Mahasiswa - Jaya Jaya Institut](https://datastudio.google.com/reporting/8c134ae4-5ed8-4487-b928-411857cdcec6)

Berikut adalah tangkapan layar dari dashboard yang telah dibuat:

![Business Dashboard](dashboard.png)

## Menjalankan Sistem Machine Learning
Prototype sistem Machine Learning dibangun menggunakan Streamlit. Untuk menjalankannya secara lokal:

```bash
streamlit run app.py
```
Aplikasi akan otomatis terbuka di browser Anda (biasanya di `http://localhost:8501`). Anda dapat memasukkan data profil mahasiswa dan melihat prediksi apakah mahasiswa tersebut akan *Dropout*, *Enrolled*, atau *Graduate*.

Tautan Streamlit Community Cloud: (Tolong masukkan link aplikasi Streamlit Anda jika sudah di-deploy)

## Conclusion
Dari hasil Exploratory Data Analysis dan pemodelan Machine Learning:
- **Performa Akademik (Nilai Semester 1 & 2)** adalah prediktor yang sangat kuat terhadap kelulusan mahasiswa. Mahasiswa dengan *Curricular_units_1st_sem_grade* atau *2nd_sem_grade* yang rendah memiliki risiko sangat tinggi untuk *dropout*.
- **Tunggakan Biaya Kuliah (Tuition Fees Up To Date)** juga merupakan faktor penting. Mahasiswa yang tidak membayar biaya kuliah tepat waktu banyak yang akhirnya putus sekolah.
- **Beasiswa (Scholarship Holder)**: Mahasiswa penerima beasiswa cenderung memiliki tingkat kelulusan yang jauh lebih baik.
- Model *Random Forest* yang dibangun mampu memprediksi status mahasiswa dengan akurasi di atas 75%.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- **Sistem Peringatan Dini Akademik (Early Warning System)**: Gunakan model prediksi ini saat nilai ujian tengah semester 1 mulai keluar. Jika nilai sangat rendah, berikan konseling akademik secara intensif kepada mahasiswa yang berisiko.
- **Bantuan Finansial / Fleksibilitas Pembayaran**: Karena tunggakan uang kuliah sangat berkorelasi dengan dropout, pertimbangkan untuk memberikan skema cicilan biaya kuliah yang lebih fleksibel kepada mahasiswa yang kesulitan secara finansial agar mereka tetap *Enrolled*.
- **Peningkatan Program Beasiswa**: Mengingat penerima beasiswa memiliki tingkat kelulusan tinggi, penambahan kuota beasiswa bisa membantu menekan angka *dropout* di institusi.
