import 'package:flutter/material.dart';
import 'screens/login_screen.dart';
import 'screens/main_screen.dart'; // Eğer ayrı dosyadaysa import et
import 'utils/app_texts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  bool isDark = true; // Varsayılan Koyu Mod olsun
  bool isLoggedIn = false;
  String currentLang = 'tr'; // Varsayılan Türkçe

  void toggleTheme() {
    setState(() {
      isDark = !isDark;
    });
  }

  // Yeni: İstediğimiz dili seçme fonksiyonu
  void changeLanguage(String langCode) {
    setState(() {
      currentLang = langCode;
    });
  }

  void login() {
    setState(() {
      isLoggedIn = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'LifeFlow',
      // KOYU MOD / AÇIK MOD AYARLAMASI
      themeMode: isDark ? ThemeMode.dark : ThemeMode.light,
      theme: ThemeData.light(useMaterial3: true).copyWith(
        primaryColor: Colors.red,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.red),
      ),
      darkTheme: ThemeData.dark(useMaterial3: true).copyWith(
        primaryColor: Colors.redAccent,
        colorScheme: const ColorScheme.dark(
          primary: Colors.redAccent,
          secondary: Colors.red,
        ),
      ),

      home: isLoggedIn
          ? MainScreen(
              currentLang: currentLang,
              onToggleTheme: toggleTheme,
              onChangeLanguage:
                  changeLanguage, // Dil değiştirme yetkisi veriyoruz
            )
          : LoginScreen(
              currentLang: currentLang,
              onLoginSuccess: login,
              onToggleTheme: toggleTheme, // Login ekranında da tema değişsin
              onChangeLanguage:
                  changeLanguage, // Dil değiştirme yetkisi veriyoruz
            ),
    );
  }
}
