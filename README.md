# 🩸 Blood Donation App

Kan bağışçıları ile kan ihtiyacı olan kurumları ve bireyleri güvenli, hızlı ve etkili bir şekilde buluşturan **mobil tabanlı bir kan bağışı platformu**.

Bu proje **Flutter** ile geliştirilmiş olup **Android (Google Play Store)** ve **iOS (App Store)** üzerinde yayınlanmak üzere tasarlanmıştır. Akademik, teknik ve sosyal fayda açısından güçlü bir örnek projedir.

---

## 📌 Projenin Amacı

Blood Donation App’in temel amacı:

* Kan bağışçılarını
* Kan ihtiyacı olan hastaneleri / bireyleri

**dijital ortamda eşleştirerek** acil ve hayati bir problemi çözmektir.

Bu proje yalnızca bir yazılım geliştirme çalışması değil, aynı zamanda **toplumsal fayda** sağlayan gerçek hayat odaklı bir çözümdür.

---

## 🎯 Neden Doğru Bir Proje?

Bu uygulama aynı anda aşağıdaki IT yetkinliklerini kapsar:

* Mobil uygulama geliştirme (Flutter)
* REST API kullanımı
* Veritabanı tasarımı ve ilişkiler
* Kullanıcı yönetimi
* Rol bazlı yetkilendirme
* İş kuralları (business logic)
* Veri güvenliği bilinci

Bu kombinasyon, **bir IT öğrencisinin veya junior developer’ın sahip olması gereken temel yetkinliklerin tamamını** temsil eder.

---

## 🧩 Uygulama Mimarisi

**Mobil Uygulama (Flutter)**
⬇️ REST API
**Backend (FastAPI)**
⬇️ ORM
**PostgreSQL Veritabanı**

---

## 👥 Kullanıcı Rolleri

Uygulama rol bazlı çalışır:

### 🧑‍⚕️ Donor (Bağışçı)

* Profil oluşturma
* Kan grubu bilgisi
* Son bağış tarihi
* Lokasyon bilgisi
* Uygunluk durumu
* Kendi bilgilerini güncelleme

### 🏥 Requester / Hospital (Talep Eden)

* Kan talebi oluşturma
* Talep durumu takibi
* Kendi taleplerini yönetme

### 🛡️ Admin

* Tüm kullanıcıları görüntüleme
* Tüm bağış ve talepleri yönetme
* Sistem denetimi

---

## 🔐 Kullanıcı Sistemi

* Kayıt / Giriş sistemi
* Şifrelerin **hash’lenmesi**
* JWT tabanlı kimlik doğrulama
* Rol bazlı yetkilendirme

Bu yapı **güvenli yazılım geliştirme** prensiplerine uygundur.

---

## 🧬 Donor (Bağışçı) Yönetimi

Her bağışçı için aşağıdaki bilgiler tutulur:

* Kan grubu
* Son bağış tarihi
* Şehir / ilçe
* Uygunluk durumu

Bu kısım:

* Veritabanı tasarımını
* Normalizasyonu
* İlişkisel veri yapısını

açıkça gösterir.

---

## 🩸 Kan Talep Sistemi

Kan ihtiyacı olan kullanıcılar için:

* İstenen kan grubu
* Aciliyet durumu
* Lokasyon
* Talep tarihi

bilgileri tutulur.

---

## 🔄 Eşleştirme Mantığı (En Kritik Kısım)

Sistem aşağıdaki kriterlere göre bağışçı – talep eşleştirmesi yapar:

1. **Kan grubu uyumu**
2. **Lokasyon yakınlığı**
3. **Son bağış tarihine göre uygunluk**

Bu bölüm:

* Algoritmik düşünme
* İş kuralları (business logic)
* Gerçek dünya senaryoları

konularını net şekilde ortaya koyar.

---

## 🗄️ Veritabanı Tasarımı

Temel tablolar:

* `users`
* `roles`
* `donor_profiles`
* `blood_requests`
* `donations`

🔗 **Foreign Key ilişkileri** aktif olarak kullanılmıştır.
İlişkiler olmadan proje **eksik kabul edilir**.

---

## 🛠️ Kullanılan Teknolojiler

### 📱 Frontend (Mobil)

* Flutter
* Dart
* Material Design
* REST API entegrasyonu

### ⚙️ Backend

* Python
* FastAPI
* SQLAlchemy
* JWT Authentication

### 🗃️ Veritabanı

* PostgreSQL

---

## 🚀 İleri Seviye Özellikler

Zorunlu olmamakla birlikte projeyi üst seviyeye taşıyan ekler:

* Lokasyon bazlı filtreleme
* E-posta bildirim sistemi
* Admin panel
* Swagger API dokümantasyonu
* Soft delete
* Audit log

---

## 📦 Platform Desteği

* ✅ Android (Google Play Store)
* ✅ iOS (App Store)

Tek kod tabanı ile **çapraz platform** desteği sağlanır.

---

## 🎓 Akademik ve CV Değeri

Bu proje:

* Sosyal fayda sağlar
* Teknik olarak güçlüdür
* Mülakatlarda rahatlıkla anlatılabilir
* Sadece CRUD değildir
* Gerçek hayat problemini çözer

Özellikle:

* Mobil geliştirici
* Backend developer
* Full-stack adayları

için **çok değerli bir portföy projesidir**.

---

## 📄 Lisans

Bu proje eğitim ve geliştirme amaçlıdır.

---

## 🤝 Katkı

Katkılar ve geri bildirimler memnuniyetle karşılanır.
