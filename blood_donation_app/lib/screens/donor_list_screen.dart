import 'package:flutter/material.dart';
import 'donor_detail_screen.dart';
import 'add_donor_screen.dart';
import '../models/donor.dart';

class DonorListScreen extends StatefulWidget {
  const DonorListScreen({super.key});

  @override
  State<DonorListScreen> createState() => _DonorListScreenState();
}

class _DonorListScreenState extends State<DonorListScreen> {
  final List<Donor> donors = [
    Donor(name: "Ahmet Yılmaz", blood: "A+", city: "İstanbul"),
    Donor(name: "Ayşe Demir", blood: "0-", city: "Ankara"),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.add),
        onPressed: () async {
          final newDonor = await Navigator.push<Donor>(
            context,
            MaterialPageRoute(builder: (_) => const AddDonorScreen()),
          );

          if (newDonor != null) {
            setState(() {
              donors.add(newDonor);
            });
          }
        },
      ),
      body: ListView.builder(
        itemCount: donors.length,
        itemBuilder: (context, index) {
          final donor = donors[index];

          return Card(
            child: ListTile(
               title: Text(donor.name),
    subtitle: Text("${donor.blood} • ${donor.city}"),

    // 👉 DONÖR DETAY
    onTap: () {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (_) => DonorDetailScreen(
            name: donor.name,
            blood: donor.blood,
            city: donor.city,
          ),
        ),
      );
    },

    // 👉 SİLME (LONG PRESS)
    onLongPress: () {
      setState(() {
        donors.removeAt(index);
      });

      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Donör silindi")),
      );
    },

    // 👉 DÜZENLEME BUTONU
    trailing: IconButton(
      icon: const Icon(Icons.edit),
      onPressed: () async {
        final updatedDonor = await Navigator.push<Donor>(
          context,
          MaterialPageRoute(
            builder: (_) => AddDonorScreen(donor: donor),
          ),
        );

        if (updatedDonor != null) {
          setState(() {
            donors[index] = updatedDonor;
          });
        }
      },
    ),
            ),
          );
        },
      ),
    );
  }
}
