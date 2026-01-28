class AppTexts {
  // Dil Listesi (Menüde görünecek)
  static final Map<String, String> languages = {
    'tr': 'Türkçe 🇹🇷',
    'en': 'English 🇺🇸',
    'es': 'Español 🇪🇸',
    'fr': 'Français 🇫🇷',
    'de': 'Deutsch 🇩🇪',
    'zh': '中文 🇨🇳',
    'ru': 'Русский 🇷🇺',
    'ar': 'العربية 🇸🇦',
    'pt': 'Português 🇧🇷',
    'hi': 'हिन्दी 🇮🇳',
  };

  // Kelime Sözlüğü
  static final Map<String, Map<String, String>> data = {
    'tr': {
      'login_title': 'LifeFlow Giriş',
      'email': 'E-posta',
      'password': 'Şifre',
      'login_btn': 'Giriş Yap',
      'login_success': 'Giriş Başarılı!',
      'login_error': 'Hatalı Giriş',
      'no_account': 'Hesabın yok mu? Kayıt Ol',
      'register_title': 'Kayıt Ol',
      'register_btn': 'Hesap Oluştur',
      'register_success': 'Kayıt Başarılı!',
      'register_error': 'Kayıt Başarısız.',
      'home_title': 'Ana Sayfa',
      'welcome_main': 'Hayat Kurtarmaya Hazır mısın?',
      'see_requests': 'Talepleri Gör',
      'list_title': 'Kan Bağışı Talepleri',
      'logout': 'Çıkış',
      'loading': 'Yükleniyor...',
      'no_data': 'Veri yok',
      'urgent': 'ACİL',
      'normal': 'Normal',
      'location_unknown': 'Konum Bilinmiyor',
      'error': 'Hata',
    },
    'en': {
      'login_title': 'LifeFlow Login',
      'email': 'Email',
      'password': 'Password',
      'login_btn': 'Log In',
      'login_success': 'Success!',
      'login_error': 'Login Failed',
      'no_account': 'No account? Sign Up',
      'register_title': 'Register',
      'register_btn': 'Create Account',
      'register_success': 'Success!',
      'register_error': 'Failed.',
      'home_title': 'Home',
      'welcome_main': 'Ready to Save Lives?',
      'see_requests': 'See Requests',
      'list_title': 'Blood Requests',
      'logout': 'Logout',
      'loading': 'Loading...',
      'no_data': 'No data',
      'urgent': 'URGENT',
      'normal': 'Normal',
      'location_unknown': 'Unknown Location',
      'error': 'Error',
    },
    // Diğer diller için varsayılan olarak İngilizce dönecek şekilde ayarlayabiliriz
    // veya önceki uzun listeyi buraya ekleyebilirsin.
    // Şimdilik hata vermemesi için TR ve EN tam, diğerleri için kısa özet:
  };
}
