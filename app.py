import joblib
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# Modeli yükle
model = joblib.load("xgb_model.pkl")  # Model dosyanı ekle

# 📌 Veri Yükleme
@st.cache_data
def load_data():
    df = pd.read_csv("balanced_data.csv")  # Tek dosyayı yükle
    return df

df = load_data()

# Uygulama başlığı
st.title('📊 Türk Telekom Müşteri Churn Analizi: Guardians of Churn')

st.markdown(""" :dart: Bu Streamlit uygulaması, telekom sektöründe müşteri kaybını tahmin etmek için yapılmıştır. """)

# Yan menüye resim ekleme
image = Image.open('Churn-Prediction-sca.jpg')
st.sidebar.image(image)

# Kullanıcıya seçenek sunma
add_selectbox = st.sidebar.selectbox(
    "🔍 Seçiminizi Yapın:", ("📊 Görselleştirme", "🤖 Anlık Tahmin")
)

# Yan menüye açıklama ekleme
st.sidebar.info('Bu uygulama müşteri kaybını tahmin etmek için yapılmıştır.')


# Anlık tahmin bölümü
if add_selectbox == "🤖 Anlık Tahmin":
    st.info("Lütfen müşteri bilgilerini girin")

    # Kullanıcı giriş alanları
    age = st.number_input('Yaş', min_value=18, max_value=100, value=30)
    tenure = st.number_input('Hizmet süresi (ay)', min_value=0, value=12)
    
    service_types = {'Ön Ödemeli': 'service_type_Prepaid', 'Peşin': 'service_type_Postpaid', 'Geniş Bant': 'service_type_Broadband'}
    selected_service = st.selectbox('Hizmet Türü', list(service_types.keys()))

    avg_call_duration = st.number_input('Ortalama çağrı süresi (dk)', min_value=0.0, value=5.0)
    data_usage = st.number_input('Veri kullanımı (GB)', min_value=0.0, value=2.0)
    roaming_usage = st.number_input('Dolaşım kullanımı (GB)', min_value=0.0, value=0.5)
    monthly_charge = st.number_input('Aylık ücret (TL)', min_value=0.0, value=50.0)
    overdue_payments = st.number_input('Ödenmemiş faturalar (adet)', min_value=0, value=0)
    auto_payment = st.selectbox('Otomatik ödeme var mı?', ('Hayır', 'Evet'))
    avg_top_up_count = st.number_input('Aylık ortalama TL yükleme sayısı', min_value=0, value=2)
    call_drops = st.number_input('Çağrı düşme sayısı', min_value=0, value=1)
    customer_support_calls = st.number_input('Müşteri hizmetleri çağrısı', min_value=0, value=1)
    satisfaction_score = st.slider('Müşteri memnuniyet skoru (1.0 - 10.0)', min_value=1.0, max_value=10.0, value=7.0, step=0.1)

    # Servisleri One-Hot Encode yap
    apps_list = ['RitimGo', 'Konuşalım', 'HızlıPazar', 'İzleGo', 'CüzdanX']
    selected_apps = st.multiselect('Kullandığı servisler', apps_list)

    # **Modelin Beklediği Sütunları Oluştur**
    input_data = {
        'age': age,
        'tenure': tenure,
        'avg_call_duration': avg_call_duration,
        'data_usage': data_usage,
        'roaming_usage': roaming_usage,
        'monthly_charge': monthly_charge,
        'overdue_payments': overdue_payments,
        'auto_payment': 1 if auto_payment == 'Evet' else 0,
        'avg_top_up_count': avg_top_up_count,
        'call_drops': call_drops,
        'customer_support_calls': customer_support_calls,
        'satisfaction_score': satisfaction_score,
        'num_of_apps_used': len(selected_apps),
    }

    # **Hizmet Türü One-Hot Encoding**
    for key in service_types.values():
        input_data[key] = 1 if key == service_types[selected_service] else 0

    # **Uygulamalar için One-Hot Encoding**
    for app in apps_list:
        input_data[f"apps_tuple_{app}"] = 1 if app in selected_apps else 0

    # **Tenure için One-Hot Encoding**
    input_data["tenure_category_New"] = 1 if tenure < 12 else 0
    input_data["tenure_category_Loyal"] = 1 if 12 <= tenure < 36 else 0
    input_data["tenure_category_Very Loyal"] = 1 if tenure >= 36 else 0

    # **Veriyi DataFrame'e Çevir**
    features_df = pd.DataFrame([input_data])

    # Girdi verilerini göster
    st.write('Girdi verilerinin önizlemesi:')
    st.dataframe(features_df)

    # **Tahmin Butonu**
    if st.button('Tahmin Yap'):
        prediction = model.predict(features_df)

        if prediction[0] == 1:
            st.warning('⚠️ Müşteri hizmeti sonlandırma ihtimali yüksek. Önlem alınması önerilir.')
        else:
            st.success('✅ Müşteri hizmetten memnun görünüyor. Şu an için risk bulunmamaktadır.')

elif  add_selectbox == "📊 Görselleştirme":
    chart_option = st.radio(
        "🎨 Görselleştirme Seçin:",
        ("Churn Oranı (Pasta Grafiği)", "Yaş Dağılımı", "Memnuniyet Skoru Dağılımı ve Churn")
    )

    # Seçilen grafik türüne göre görselleştirme
    if chart_option == "Churn Oranı (Pasta Grafiği)":
        st.subheader("📊 Churn Oranı (Pasta Grafiği)")

        churn_data = df['churn'].value_counts().reset_index()
        churn_data.columns = ['Churn Durumu', 'Müşteri Sayısı']

        churn_pie_chart = alt.Chart(churn_data).mark_arc().encode(
            theta=alt.Theta(field="Müşteri Sayısı", type="quantitative"),
            color=alt.Color(field="Churn Durumu", type="nominal"),
            tooltip=["Churn Durumu", "Müşteri Sayısı"]
        ).properties(width=400, height=300)

        st.altair_chart(churn_pie_chart)

    elif chart_option == "Yaş Dağılımı":
        st.subheader("📊 Yaş Dağılımı ve Churn")

        age_churn_distribution = alt.Chart(df).mark_bar().encode(
            alt.X('age:Q', bin=True, title='Yaş'),
            alt.Y('count():Q', title='Müşteri Sayısı'),
            color='churn:N',  # Churn'ü renk olarak ekliyoruz
            tooltip=['age:Q', 'count():Q', 'churn:N']
        ).properties(width=400, height=300)

        st.altair_chart(age_churn_distribution)

    elif chart_option == "Memnuniyet Skoru Dağılımı ve Churn":
        st.subheader("📊 Memnuniyet Skoru Dağılımı ve Churn")
        
        satisfaction_churn = alt.Chart(df).mark_point().encode(
            alt.X('satisfaction_score:Q', title='Memnuniyet Skoru'),
            alt.Y('count():Q', title='Müşteri Sayısı'),
            color='churn:N',
            tooltip=['satisfaction_score:Q', 'count():Q', 'churn:N']
        ).properties(width=400, height=300)

        st.altair_chart(satisfaction_churn)