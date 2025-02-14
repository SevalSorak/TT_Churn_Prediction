## 📊 Türk Telekom Müşteri Churn Analizi: Guardians of Churn

Bu proje, telekom sektöründe müşteri kaybını (churn) tahmin etmek ve bu kaybın önüne geçmek amacıyla geliştirilmiştir. Proje kapsamında, müşteri verileri üzerinde analizler yapılmış ve bir makine öğrenmesi modeli kullanılarak churn tahmini gerçekleştirilmiştir. Ayrıca, kullanıcı dostu bir Streamlit arayüzü ile sonuçlar görselleştirilmiştir.

### 📂 Proje Yapısı

*   **Model Eğitimi:** `xgb_model.pkl` dosyası, XGBoost algoritması kullanılarak eğitilmiş bir modeli içerir.
*   **Streamlit Arayüzü:** `streamlit_app.py` dosyası, kullanıcıların veri girişi yapabileceği ve churn tahmini alabileceği bir arayüz sağlar.
*   **Görselleştirmeler:** Çeşitli grafikler (pasta grafiği, yaş dağılımı, memnuniyet skoru dağılımı) ile churn oranları ve müşteri özellikleri görselleştirilmiştir.

### 🚀 Nasıl Çalıştırılır?

1.  **Gereksinimlerin Yüklenmesi:**

    ```bash
    pip install streamlit joblib pandas numpy matplotlib seaborn plotly altair pillow
    ```

2.  **Streamlit Uygulamasını Çalıştırma:**

    ```bash
    streamlit run streamlit_app.py
    ```

3.  **Arayüz Kullanımı:**

    *   Uygulama başlatıldığında, yan menüden "📊 Görselleştirme" veya "🤖 Anlık Tahmin" seçeneklerinden birini seçebilirsiniz.
    *   **Görselleştirme:** Churn oranı, yaş dağılımı ve memnuniyet skoru gibi çeşitli grafikleri görüntüleyebilirsiniz.
    *   **Anlık Tahmin:** Müşteri bilgilerini girerek, churn tahmini yapabilirsiniz.

### 📝 Capstone: Guardians of Churn

Bu capstone görevinde hedefimiz, olası müşteri göçlerinin (churn) önüne geçmek. Toplamda 10 milyon müşterimize ait veri üzerinde çalışıldı.

### 📸 Ekran Görüntüleri ve Video

*   **Streamlit Arayüzü Görseli:** [Görsel Bağlantısı](assets/Ekran görüntüsü 2025-02-14 171910.png)(assets/Ekran görüntüsü 2025-02-14 172507.png)
*   **Streamlit Arayüzü Videosu:** [Video Bağlantısı](assets/app.webm)
