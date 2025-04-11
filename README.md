## 📈 Telco Customer Churn - Feature Engineering & Classification

Bu proje, bir telekomünikasyon şirketinin müşteri kaybını (churn) tahmin etmeye yönelik bir makine öğrenmesi modeli geliştirmeyi amaçlar. Projede öncelikle veri seti üzerinde kapsamlı bir **veri ön işleme ve özellik mühendisliği** süreci uygulanmış, ardından **CatBoostClassifier** ile sınıflandırma gerçekleştirilmiştir.

---

## 📁 Veri Seti Hakkında

Veri seti, müşterilerin hizmet kullanım bilgileri ve demografik özelliklerini içermektedir. Hedef değişken, bir müşterinin hizmeti bırakıp bırakmadığını belirten `Churn` değişkenidir.

- **Toplam Gözlem Sayısı**: 7.043  
- **Bağımsız Değişkenler**: 19+  
- **Hedef Değişken**: `Churn` (1: Hizmeti bırakan, 0: Devam eden)

### 🔍 Bazı Önemli Değişkenler

| Değişken           | Açıklama                                       |
|--------------------|------------------------------------------------|
| `gender`           | Müşterinin cinsiyeti                           |
| `SeniorCitizen`    | Yaşlı vatandaş durumu (1: Evet, 0: Hayır)      |
| `Partner`          | Eşi olup olmadığı                              |
| `Dependents`       | Bakmakla yükümlü olduğu kişi var mı?           |
| `tenure`           | Aylık hizmet süresi                            |
| `MonthlyCharges`   | Aylık ödeme                                    |
| `TotalCharges`     | Toplam ödeme                                   |
| `Churn`            | Müşteri kaybı durumu (hedef değişken)          |

---

## ⚙️ Kullanılan Kütüphaneler

- `pandas`, `numpy` – Veri işleme
- `matplotlib`, `seaborn` – Görselleştirme
- `scikit-learn` – Modelleme, metrikler, preprocessing
- `catboost` – Sınıflandırma modeli
- `warnings` – Uyarıları filtreleme

---

## 🧪 Uygulama Adımları

1. **Veri Keşfi (EDA)**  
   - Değişken tipleri ve eksik veriler incelendi  
   - Sayısal ve kategorik değişkenler ayrıldı  
   - `TotalCharges` numerik formata çevrildi  
   - `Churn` binary forma dönüştürüldü

2. **Özellik Mühendisliği**  
   - Eksik veriler ele alındı  
   - Gerekli dönüşümler yapıldı  
   - Kategorik veriler encode edildi

3. **Modelleme**  
   - Veri eğitim/test olarak bölündü  
   - CatBoostClassifier modeli ile eğitildi  
   - Doğruluk, precision, recall, F1 ve ROC AUC gibi metriklerle değerlendirildi
