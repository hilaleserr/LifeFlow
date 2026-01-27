import 'package:flutter/material.dart';
import '../models/donor.dart';

class AddDonorScreen extends StatelessWidget {
  final Donor? donor;

  const AddDonorScreen({
    super.key,
    this.donor,
  });

  @override
  Widget build(BuildContext context) {
    final nameController = TextEditingController(text: donor?.name ?? "");
    final bloodController = TextEditingController(text: donor?.blood ?? "");
    final cityController = TextEditingController(text: donor?.city ?? "");


    return Scaffold(
      appBar: AppBar(title: const Text("Add Donor")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
         TextField(
  controller: nameController,
  decoration: const InputDecoration(
    labelText: "Name",
    border: OutlineInputBorder(),
  ),
),
const SizedBox(height: 12),
TextField(
  controller: bloodController,
  decoration: const InputDecoration(
    labelText: "Blood Type",
    border: OutlineInputBorder(),
  ),
),
TextField(
  controller: cityController,
  decoration: const InputDecoration(
    labelText: "City",
    border: OutlineInputBorder(),
  ),
),


            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                final donor = Donor(
                  name: nameController.text,
                  blood: bloodController.text,
                  city: cityController.text,
                );
                Navigator.pop(context, donor);
              },
              child:  Text(donor == null ? "Kaydet" : "Güncelle"),
            )
          ],
        ),
      ),
    );
  }
}
