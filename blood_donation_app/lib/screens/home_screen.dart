import 'package:flutter/material.dart';
import 'donor_list_screen.dart';
import 'main_screen.dart';
class HomeScreen extends StatelessWidget {
  final VoidCallback onToggleTheme;

  const HomeScreen({
    super.key,
    required this.onToggleTheme,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Home"),
        actions: [
          IconButton(
            icon: const Icon(Icons.dark_mode),
            onPressed: onToggleTheme,
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                 context,
  MaterialPageRoute(
    builder: (context) => MainScreen( onToggleTheme: onToggleTheme,),
  ),
                );
              },
              child: const Text("Donörleri Gör"),
            ),
          ],
        ),
      ),
    );
  }
}
