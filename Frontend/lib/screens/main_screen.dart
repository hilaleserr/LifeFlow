import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../utils/app_texts.dart';

class MainScreen extends StatefulWidget {
  final VoidCallback onToggleTheme;
  final Function(String) onChangeLanguage; // DİL DEĞİŞTİRİCİ
  final String currentLang;

  const MainScreen({
    super.key,
    required this.onToggleTheme,
    required this.onChangeLanguage,
    required this.currentLang,
  });

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  final ApiService _apiService = ApiService();
  late Future<List<dynamic>> _requestsFuture;

  String t(String key) {
    return AppTexts.data[widget.currentLang]?[key] ??
        AppTexts.data['en']?[key] ??
        key;
  }

  @override
  void initState() {
    super.initState();
    _requestsFuture = _apiService.getBloodRequests();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(t('list_title')),
        actions: [
          IconButton(
            icon: const Icon(Icons.brightness_6),
            onPressed: widget.onToggleTheme,
          ),
          // DİL MENÜSÜ
          PopupMenuButton<String>(
            icon: const Icon(Icons.language),
            onSelected: widget.onChangeLanguage,
            itemBuilder: (BuildContext context) {
              return AppTexts.languages.entries.map((entry) {
                return PopupMenuItem<String>(
                  value: entry.key,
                  child: Text(entry.value),
                );
              }).toList();
            },
          ),
        ],
      ),
      body: FutureBuilder<List<dynamic>>(
        future: _requestsFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: Text(t('loading')));
          } else if (snapshot.hasError) {
            return Center(child: Text("${t('error')}: ${snapshot.error}"));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text(t('no_data')));
          } else {
            final requests = snapshot.data!;
            return ListView.builder(
              itemCount: requests.length,
              itemBuilder: (context, index) {
                final item = requests[index];
                final isUrgent = item['urgency'] == true;

                return Card(
                  margin: const EdgeInsets.symmetric(
                    horizontal: 10,
                    vertical: 5,
                  ),
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: isUrgent ? Colors.red : Colors.green,
                      child: Text(
                        item['blood_group'] ?? '?',
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    title: Text(item['location'] ?? t('location_unknown')),
                    subtitle: Text(
                      isUrgent ? t('urgent') : t('normal'),
                      style: TextStyle(
                        color: isUrgent ? Colors.red : Colors.grey,
                        fontWeight: isUrgent
                            ? FontWeight.bold
                            : FontWeight.normal,
                      ),
                    ),
                  ),
                );
              },
            );
          }
        },
      ),
    );
  }
}
