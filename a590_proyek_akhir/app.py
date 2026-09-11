import os
import streamlit as st
import pandas as pd
import joblib

# Load models using absolute path relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'model', 'random_forest_model.joblib'))
scaler = joblib.load(os.path.join(BASE_DIR, 'model', 'scaler.joblib'))

st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa - Jaya Jaya Institut",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Sistem Prediksi Dropout Mahasiswa")
st.subheader("Jaya Jaya Institut — Early Warning System")
st.markdown("""
Aplikasi ini memprediksi apakah seorang mahasiswa berpotensi untuk **Dropout** atau **Graduate**
berdasarkan data akademik dan demografis mereka. Model dilatih menggunakan data historis mahasiswa
dengan algoritma **Random Forest Classifier**.

> ⚠️ Data mahasiswa yang saat ini berstatus **Enrolled** dapat diinputkan di sini untuk mendapatkan
> prediksi apakah mereka berpotensi dropout atau lulus di masa mendatang.
""")

st.divider()

# --- 1. KAMUS TERJEMAHAN (DICTIONARIES) ---
marital_dict = {
    "Single / Belum Menikah": 1,
    "Married / Menikah": 2,
    "Widower / Cerai Mati": 3,
    "Divorced / Cerai Hidup": 4,
    "Facto Union": 5,
    "Legally Separated": 6
}

nacionality_dict = {
    "Portuguese": 1, "German": 2, "Spanish": 6, "Italian": 11, "Dutch": 17,
    "English": 21, "Lithuanian": 22, "Angolan": 24, "Cape Verdean": 25,
    "Guinean": 26, "Mozambican": 32, "Santomean": 41, "Turkish": 62,
    "Brazilian": 100, "Romanian": 101, "Moldovan": 103, "Mexican": 105,
    "Ukrainian": 108, "Russian": 109
}

# --- 2. ANTARMUKA PENGGUNA (UI) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Data Demografi & Ekonomi")

    marital_input = st.selectbox("Marital Status", list(marital_dict.keys()))
    nacionality_input = st.selectbox("Nacionality", list(nacionality_dict.keys()))
    displaced_input = st.selectbox("Displaced (Pindah tempat tinggal?)", ["No", "Yes"])
    debtor_input = st.selectbox("Debtor (Punya Tunggakan Biaya?)", ["No", "Yes"])
    tuition_input = st.selectbox("Tuition Fees Up To Date (Biaya Kuliah Lunas?)", ["No", "Yes"])
    gender_input = st.selectbox("Gender", ["Female", "Male"])
    scholarship_input = st.selectbox("Scholarship Holder (Penerima Beasiswa?)", ["No", "Yes"])
    age_at_enrollment = st.number_input("Age at Enrollment", min_value=15, max_value=80, value=20)

    # Terjemahkan ke angka
    marital_status = marital_dict[marital_input]
    nacionality = nacionality_dict[nacionality_input]
    displaced = 1 if displaced_input == "Yes" else 0
    debtor = 1 if debtor_input == "Yes" else 0
    tuition_fees_up_to_date = 1 if tuition_input == "Yes" else 0
    gender = 1 if gender_input == "Male" else 0
    scholarship_holder = 1 if scholarship_input == "Yes" else 0

with col2:
    st.subheader("📚 Performa Akademik")
    admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=120.0)
    cu_1st_sem_enrolled = st.number_input("1st Sem Enrolled Units", min_value=0, max_value=30, value=6)
    cu_1st_sem_approved = st.number_input("1st Sem Approved Units", min_value=0, max_value=30, value=5)
    cu_1st_sem_grade = st.number_input("1st Sem Grade (0–20)", min_value=0.0, max_value=20.0, value=12.0)
    cu_2nd_sem_enrolled = st.number_input("2nd Sem Enrolled Units", min_value=0, max_value=30, value=6)
    cu_2nd_sem_approved = st.number_input("2nd Sem Approved Units", min_value=0, max_value=30, value=5)
    cu_2nd_sem_grade = st.number_input("2nd Sem Grade (0–20)", min_value=0.0, max_value=20.0, value=12.0)

# Default features dictionary (nilai default = median/modus dataset)
input_features = {
    'Marital_status': marital_status,
    'Application_mode': 1,
    'Application_order': 1,
    'Course': 9238,
    'Daytime_evening_attendance': 1,
    'Previous_qualification': 1,
    'Previous_qualification_grade': 122.0,
    'Nacionality': nacionality,
    'Mothers_qualification': 1,
    'Fathers_qualification': 1,
    'Mothers_occupation': 5,
    'Fathers_occupation': 5,
    'Admission_grade': admission_grade,
    'Displaced': displaced,
    'Educational_special_needs': 0,
    'Debtor': debtor,
    'Tuition_fees_up_to_date': tuition_fees_up_to_date,
    'Gender': gender,
    'Scholarship_holder': scholarship_holder,
    'Age_at_enrollment': age_at_enrollment,
    'International': 0,
    'Curricular_units_1st_sem_credited': 0,
    'Curricular_units_1st_sem_enrolled': cu_1st_sem_enrolled,
    'Curricular_units_1st_sem_evaluations': 6,
    'Curricular_units_1st_sem_approved': cu_1st_sem_approved,
    'Curricular_units_1st_sem_grade': cu_1st_sem_grade,
    'Curricular_units_1st_sem_without_evaluations': 0,
    'Curricular_units_2nd_sem_credited': 0,
    'Curricular_units_2nd_sem_enrolled': cu_2nd_sem_enrolled,
    'Curricular_units_2nd_sem_evaluations': 6,
    'Curricular_units_2nd_sem_approved': cu_2nd_sem_approved,
    'Curricular_units_2nd_sem_grade': cu_2nd_sem_grade,
    'Curricular_units_2nd_sem_without_evaluations': 0,
    'Unemployment_rate': 10.8,
    'Inflation_rate': 1.4,
    'GDP': 1.74
}

st.divider()

# --- 3. PROSES PREDIKSI ---
if st.button("🔍 Prediksi Status Mahasiswa", use_container_width=True, type="primary"):
    input_df = pd.DataFrame([input_features])

    # Scale features
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0]

    # prediction: 1 = Dropout, 0 = Graduate
    dropout_proba = proba[1]
    graduate_proba = proba[0]

    st.markdown("### 📊 Hasil Prediksi")

    col_res1, col_res2 = st.columns(2)
    with col_res1:
        if prediction == 1:
            st.error("⚠️ **Prediksi: DROPOUT**\n\nMahasiswa ini **berisiko tinggi** untuk dropout. Segera lakukan intervensi akademik.")
        else:
            st.success("🎓 **Prediksi: GRADUATE**\n\nMahasiswa ini diprediksi akan **berhasil lulus**.")

    with col_res2:
        st.metric("Probabilitas Dropout", f"{dropout_proba*100:.1f}%")
        st.metric("Probabilitas Graduate", f"{graduate_proba*100:.1f}%")
        st.progress(float(dropout_proba), text=f"Risiko Dropout: {dropout_proba*100:.1f}%")

    if prediction == 1 and dropout_proba > 0.7:
        st.warning("""
        💡 **Rekomendasi Tindakan:**
        - Jadwalkan sesi konseling akademik segera
        - Periksa status pembayaran biaya kuliah
        - Tawarkan program bimbingan belajar intensif
        - Pertimbangkan bantuan finansial jika diperlukan
        """)