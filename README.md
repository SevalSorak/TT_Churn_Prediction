📊 Türk Telekom Müşteri Churn Analizi: Guardians of Churn
Bu proje, telekom sektöründe müşteri kaybını (churn) tahmin etmek ve bu kaybın önüne geçmek amacıyla geliştirilmiştir. Proje kapsamında, müşteri verileri üzerinde analizler yapılmış ve bir makine öğrenmesi modeli kullanılarak churn tahmini gerçekleştirilmiştir. Ayrıca, kullanıcı dostu bir Streamlit arayüzü ile sonuçlar görselleştirilmiştir.

📂 Proje Yapısı
Model Eğitimi: xgb_model.pkl dosyası, XGBoost algoritması kullanılarak eğitilmiş bir modeli içerir.

Streamlit Arayüzü: streamlit_app.py dosyası, kullanıcıların veri girişi yapabileceği ve churn tahmini alabileceği bir arayüz sağlar.

Görselleştirmeler: Çeşitli grafikler (pasta grafiği, yaş dağılımı, memnuniyet skoru dağılımı) ile churn oranları ve müşteri özellikleri görselleştirilmiştir.

🚀 Nasıl Çalıştırılır?
Gereksinimlerin Yüklenmesi:

bash
Copy
pip install streamlit joblib pandas numpy matplotlib seaborn plotly altair pillow
Streamlit Uygulamasını Çalıştırma:

bash
Copy
streamlit run streamlit_app.py
Arayüz Kullanımı:

Uygulama başlatıldığında, yan menüden "📊 Görselleştirme" veya "🤖 Anlık Tahmin" seçeneklerinden birini seçebilirsiniz.

Görselleştirme: Churn oranı, yaş dağılımı ve memnuniyet skoru gibi çeşitli grafikleri görüntüleyebilirsiniz.

Anlık Tahmin: Müşteri bilgilerini girerek, churn tahmini yapabilirsiniz.

📝 Capstone: Guardians of Churn
Bu capstone görevinde hedefimiz, olası müşteri göçlerinin (churn) önüne geçmek. Toplamda 10 milyon müşterimize ait veri üzerinde çalışıldı.

📸 Ekran Görüntüleri ve Video
Streamlit Arayüzü Görseli: Görsel Bağlantısı

Streamlit Arayüzü Videosu: Video Bağlantısı
