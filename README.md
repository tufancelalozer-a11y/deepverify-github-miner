# 💎 DeepVerify GitHub Gold Miner

**GitHub'da gizli hazineleri keşfedin!** Az bilinen ama çok değerli projeleri otomatik olarak bulun, filtreleyin ve indirin.

---

## 🎯 Özellikler

### ✨ Akıllı Arama
- Çoklu anahtar kelime kombinasyonları
- Gelişmiş filtreleme (yıldız, dil, tarih, vb.)
- Kategori bazlı hızlı arama (Trading Bots, YouTube, AI Agents, vb.)

### 💎 Gem Score Algoritması
Her repository için 0-100 arası "değer skoru" hesaplar:
- **Dokümantasyon Kalitesi** (0-25): README, wiki, açıklama
- **Aktivite Skoru** (0-25): Son güncelleme, commit sıklığı
- **Topluluk Etkileşimi** (0-25): Fork oranı, issue yönetimi
- **Gizli Mücevher Bonusu** (0-25): Yüksek kalite + düşük yıldız = altın madeni!

### 📥 Otomatik İndirme
- Tek tıkla repository klonlama
- Toplu indirme (tüm sonuçları bir anda)
- Otomatik kategori organizasyonu
- İndirme geçmişi ve istatistikler

### 🎨 Premium Arayüz
- Modern karanlık tema (madenci estetiği)
- Glassmorphism efektleri
- Smooth animasyonlar
- Responsive tasarım

---

## 🚀 Kurulum ve Kullanım

### Gereksinimler
- Python 3.7+
- Git (repository klonlama için)
- Modern web tarayıcı

### Hızlı Başlangıç

1. **Uygulamayı Başlatın**
   ```bash
   START_DEEPVERIFY.bat
   ```
   Bu komut:
   - Gerekli Python paketlerini yükler (flask, flask-cors)
   - Local server'ı başlatır (http://localhost:5000)
   - Web arayüzünü otomatik açar

2. **Hazine Avına Başlayın!**
   - Arama kutusuna anahtar kelimeler girin
   - Veya kategori butonlarından birini seçin
   - Sonuçları inceleyin, gem score'lara bakın
   - İstediğiniz repoları indirin!

### Manuel Başlatma

Eğer batch dosyası çalışmazsa:

```bash
# 1. Server'ı başlat
python deepverify_server.py

# 2. Web arayüzünü aç
# deepverify-github-miner.html dosyasını tarayıcıda açın
```

---

## 📁 Dosya Yapısı

```
C:\Google Antigravity\
├── deepverify-github-miner.html    # Web arayüzü (ana dosya)
├── deepverify_server.py             # Flask server (clone işlemleri için)
├── clone_helper.py                  # Git clone helper script
├── START_DEEPVERIFY.bat             # Hızlı başlatma scripti
└── C:\GitHub-Treasures\             # İndirilen repolar (otomatik oluşur)
    ├── trading\                     # Trading bot repoları
    ├── youtube\                     # YouTube automation repoları
    ├── ai\                          # AI agent repoları
    ├── dashboard\                   # Dashboard template'leri
    ├── scraping\                    # Web scraping araçları
    ├── visualization\               # Veri görselleştirme kütüphaneleri
    ├── other\                       # Diğer projeler
    └── clone_log.json               # İndirme geçmişi
```

---

## 🎯 Kullanım Örnekleri

### 1. Trading Bot Arama
```
Arama: "crypto trading bot"
Filtre: Python, Min 100 yıldız
Sonuç: En iyi trading bot'ları gem score'a göre sıralanır
```

### 2. YouTube Automation Araçları
```
Kategori: 🎥 YouTube Otomasyon
Filtre: Son 30 gün güncellenmiş
Sonuç: Aktif YouTube automation projeleri
```

### 3. Gizli Mücevherler
```
Sıralama: 💎 Gem Score
Filtre: Max 1000 yıldız
Sonuç: Az bilinen ama kaliteli projeler (hidden gems)
```

---

## 🔧 API Endpoints

Server aşağıdaki endpoint'leri sağlar:

### `POST /api/clone`
Tek bir repository klonlar
```json
{
  "clone_url": "https://github.com/user/repo.git",
  "full_name": "user/repo",
  "description": "Repository açıklaması"
}
```

### `POST /api/clone-batch`
Birden fazla repository klonlar
```json
{
  "repos": [
    {
      "clone_url": "...",
      "full_name": "...",
      "description": "..."
    }
  ]
}
```

### `GET /api/stats`
İndirme istatistiklerini getirir

### `GET /api/health`
Server sağlık kontrolü

---

## 💡 İpuçları

1. **Gem Score Nasıl Yorumlanır?**
   - 🔴 0-50: Ortalama kalite
   - 🟡 50-75: İyi kalite
   - 🟢 75-100: Mükemmel kalite (altın madeni!)

2. **En İyi Sonuçlar İçin**
   - Spesifik anahtar kelimeler kullanın
   - Filtreleri birleştirin (dil + yıldız + tarih)
   - Gem score'a göre sıralayın

3. **Toplu İndirme**
   - Önce filtreleri ayarlayın
   - Sonuçları inceleyin
   - "Tümünü İndir" butonuna tıklayın
   - Server otomatik olarak kategorilere ayırır

4. **GitHub API Rate Limit**
   - Token ile: 5000 istek/saat
   - Token olmadan: 60 istek/saat
   - Uygulama otomatik olarak token kullanır

---

## 🐛 Sorun Giderme

### "Server çalışmıyor" hatası
```bash
# Server'ı manuel başlatın
python deepverify_server.py
```

### "Git bulunamadı" hatası
```bash
# Git kurulumunu kontrol edin
git --version

# Eğer yüklü değilse: https://git-scm.com/downloads
```

### "Flask modülü bulunamadı" hatası
```bash
pip install flask flask-cors
```

---

## 📊 Kategori Sistemi

Repolar otomatik olarak kategorilere ayrılır:

| Kategori | Anahtar Kelimeler |
|----------|-------------------|
| **trading** | crypto, trading, bot, arbitrage, binance, ccxt |
| **youtube** | youtube, video, automation, yt |
| **ai** | ai, agent, langchain, gpt, llm, autonomous |
| **dashboard** | dashboard, admin, template, react |
| **scraping** | scraping, crawler, spider, selenium |
| **visualization** | chart, graph, visualization, d3 |
| **other** | Diğer tüm projeler |

---

## 🔐 Güvenlik

- GitHub token güvenli şekilde saklanır
- Sadece okuma izinleri kullanılır (`public_repo`)
- Local server sadece localhost'ta çalışır
- Tüm veriler local'de saklanır

---

## 🎨 Ekran Görüntüleri

Uygulama şunları içerir:
- 🎯 Akıllı arama ve filtreleme
- 💎 Gem score görselleştirmesi
- 📊 İstatistik dashboard'u
- 🎨 Premium dark theme
- 📥 Tek tıkla indirme

---

## 📝 Lisans

Bu proje kişisel kullanım içindir. GitHub API kullanım koşullarına uygun şekilde kullanın.

---

## 🙏 Teşekkürler

**DeepVerify GitHub Gold Miner** ile GitHub'da değerli projeleri keşfetmenin tadını çıkarın! 💎⛏️

---

**İyi madencilikler!** 🚀
