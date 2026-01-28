import 'package:flutter/material.dart';
import 'main_screen.dart'; // Listeye gitmek için
import '../utils/app_texts.dart';

class HomeScreen extends StatelessWidget {
  final VoidCallback onToggleTheme;
  final Function(String) onChangeLanguage; // DİL DEĞİŞTİRİCİ
  final VoidCallback onLogout;
  final String currentLang;

  const HomeScreen({
    super.key,
    required this.onToggleTheme,
    required this.onChangeLanguage,
    required this.onLogout,
    required this.currentLang,
  });

  String t(String key) {
    // Eğer seçilen dil sözlükte yoksa İngilizce göster, o da yoksa key'i göster
    return AppTexts.data[currentLang]?[key] ?? AppTexts.data['en']?[key] ?? key;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(t('home_title')),
        actions: [
          // DİL MENÜSÜ
          PopupMenuButton<String>(
            icon: const Icon(Icons.language),
            onSelected: onChangeLanguage,
            itemBuilder: (BuildContext context) {
              return AppTexts.languages.entries.map((entry) {
                return PopupMenuItem<String>(
                  value: entry.key,
                  child: Text(entry.value),
                );
              }).toList();
            },
          ),
          IconButton(
            onPressed: onToggleTheme,
            icon: const Icon(Icons.brightness_6),
          ),
          IconButton(onPressed: onLogout, icon: const Icon(Icons.logout)),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.favorite, size: 100, color: Colors.red),
            const SizedBox(height: 20),
            Text(
              t('welcome_main'),
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 30),
            ElevatedButton.icon(
              onPressed: () {
                // MainScreen'e tüm ayarları taşıyoruz
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => MainScreen(
                      onToggleTheme: onToggleTheme,
                      onChangeLanguage:
                          onChangeLanguage, // ÖNEMLİ: Fonksiyonu taşıdık
                      currentLang: currentLang,
                    ),
                  ),
                );
              },
              icon: const Icon(Icons.list),
              label: Text(t('see_requests')),
            ),
          ],
        ),
      ),
    );
  }
}
