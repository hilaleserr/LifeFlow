import 'package:flutter/material.dart';
import 'donation_request_screen.dart';

class DonorDetailScreen extends StatelessWidget {
  final String name;
  final String blood;
  final String city;

  const DonorDetailScreen({
    super.key,
    required this.name,
    required this.blood,
    required this.city,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Donör Detayı")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(name, style: const TextStyle(fontSize: 22)),
            const SizedBox(height: 8),
            Text("Kan Grubu: $blood"),
            Text("Şehir: $city"),
            const Spacer(),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => DonationRequestScreen(donorName: name),
                  ),
                );
              },
              child: const Text("Bağış Talebi Oluştur"),
            )
          ],
        ),
      ),
    );
  }
}
