import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // Android Emülatör için: http://10.0.2.2:8000
  // Gerçek Telefon için: Bilgisayarın IP'si (örn: http://192.168.1.35:8000)
  static const String baseUrl = "http://10.0.2.2:8000";

  // 1. Giriş Yap (Login)
  Future<String?> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/login'),
        body: {'username': email, 'password': password},
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data['access_token'];
      } else {
        return null;
      }
    } catch (e) {
      print("Login Hatası: $e");
      return null;
    }
  }

  // 2. Kayıt Ol (Register)
  Future<bool> register(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/register'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password, 'role_id': 1}),
      );

      return response.statusCode == 201;
    } catch (e) {
      print("Kayıt Hatası: $e");
      return false;
    }
  }

  // 3. Kan Taleplerini Getir (İŞTE EKSİK OLAN KISIM BURASIYDI)
  Future<List<dynamic>> getBloodRequests() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/blood-requests'));

      if (response.statusCode == 200) {
        // Gelen JSON verisini listeye çevirip döndür
        return jsonDecode(response.body);
      } else {
        return []; // Hata varsa boş liste dön
      }
    } catch (e) {
      print("Veri Çekme Hatası: $e");
      return [];
    }
  }
}
