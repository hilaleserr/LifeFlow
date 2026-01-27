import 'package:flutter/material.dart';
import 'screens/login_screen.dart';
import 'screens/main_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
 bool isDark = false;
  bool isLoggedIn = false;

  void toggleTheme() {
    setState(() {
      isDark = !isDark;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: isDark ? ThemeData.dark() : ThemeData.light(),
      home: isLoggedIn
          ? MainScreen(onToggleTheme: toggleTheme)
          : LoginScreen(
              onLoginSuccess: () {
                setState(() {
                  isLoggedIn = true;
                });
              },
            ),
    );
  }
}
