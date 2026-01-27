import 'package:flutter/material.dart';

class DonationRequestScreen extends StatelessWidget {
  final String donorName;

  const DonationRequestScreen({super.key, required this.donorName});

  @override
  Widget build(BuildContext context) {
    final noteController = TextEditingController();

    return Scaffold(
      appBar: AppBar(title: const Text("Bağış Talebi")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Text("Donör: $donorName"),
            const SizedBox(height: 16),
            TextField(
              controller: noteController,
              decoration: const InputDecoration(
                labelText: "Açıklama",
                border: OutlineInputBorder(),
              ),
              maxLines: 4,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text("Talep gönderildi")),
                );
                Navigator.pop(context);
              },
              child: const Text("Gönder"),
            )
          ],
        ),
      ),
    );
  }
}
