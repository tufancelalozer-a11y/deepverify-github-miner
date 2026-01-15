"""
DeepVerify GitHub Miner - Clone Helper
Bu script, web arayüzünden gelen clone isteklerini işler ve repoları indirir.
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Konfigürasyon
CLONE_BASE_DIR = r"C:\GitHub-Treasures"
LOG_FILE = os.path.join(CLONE_BASE_DIR, "clone_log.json")

# Kategoriler
CATEGORIES = {
    "trading": ["crypto", "trading", "bot", "arbitrage", "binance", "ccxt"],
    "youtube": ["youtube", "video", "automation", "yt"],
    "ai": ["ai", "agent", "langchain", "gpt", "llm", "autonomous"],
    "dashboard": ["dashboard", "admin", "template", "react"],
    "scraping": ["scraping", "crawler", "spider", "selenium"],
    "visualization": ["chart", "graph", "visualization", "d3"],
    "other": []
}

def detect_category(repo_name, description=""):
    """Repository'nin kategorisini otomatik tespit et"""
    text = f"{repo_name} {description}".lower()
    
    for category, keywords in CATEGORIES.items():
        if category == "other":
            continue
        for keyword in keywords:
            if keyword in text:
                return category
    
    return "other"

def ensure_directory(path):
    """Klasörü oluştur (yoksa)"""
    Path(path).mkdir(parents=True, exist_ok=True)

def clone_repository(clone_url, full_name, description=""):
    """Repository'yi klonla"""
    try:
        # Kategoriyi tespit et
        category = detect_category(full_name, description)
        
        # Hedef klasörü oluştur
        category_dir = os.path.join(CLONE_BASE_DIR, category)
        ensure_directory(category_dir)
        
        # Repository adını al
        repo_name = full_name.split('/')[-1]
        target_dir = os.path.join(category_dir, repo_name)
        
        # Zaten klonlanmış mı kontrol et
        if os.path.exists(target_dir):
            print(f"⚠️  {full_name} zaten mevcut, güncelleniyor...")
            # Git pull yap
            result = subprocess.run(
                ["git", "pull"],
                cwd=target_dir,
                capture_output=True,
                text=True
            )
            action = "updated"
        else:
            print(f"📥 {full_name} indiriliyor...")
            # Git clone yap
            result = subprocess.run(
                ["git", "clone", clone_url, target_dir],
                capture_output=True,
                text=True
            )
            action = "cloned"
        
        if result.returncode == 0:
            print(f"✅ {full_name} başarıyla {action}!")
            
            # Log kaydet
            log_entry = {
                "full_name": full_name,
                "clone_url": clone_url,
                "category": category,
                "action": action,
                "timestamp": datetime.now().isoformat(),
                "path": target_dir
            }
            save_log(log_entry)
            
            return True, target_dir
        else:
            error_msg = result.stderr
            print(f"❌ Hata: {error_msg}")
            return False, error_msg
            
    except Exception as e:
        print(f"❌ İstisna: {str(e)}")
        return False, str(e)

def save_log(entry):
    """Clone logunu kaydet"""
    ensure_directory(CLONE_BASE_DIR)
    
    # Mevcut logu oku
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            logs = json.load(f)
    else:
        logs = []
    
    # Yeni entry ekle
    logs.append(entry)
    
    # Kaydet
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

def get_clone_stats():
    """Clone istatistiklerini al"""
    if not os.path.exists(LOG_FILE):
        return {"total": 0, "by_category": {}}
    
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        logs = json.load(f)
    
    stats = {
        "total": len(logs),
        "by_category": {}
    }
    
    for log in logs:
        category = log.get("category", "other")
        stats["by_category"][category] = stats["by_category"].get(category, 0) + 1
    
    return stats

def clone_from_list(repos_file):
    """Dosyadan toplu clone"""
    with open(repos_file, 'r', encoding='utf-8') as f:
        repos = json.load(f)
    
    success_count = 0
    fail_count = 0
    
    for repo in repos:
        success, _ = clone_repository(
            repo['clone_url'],
            repo['full_name'],
            repo.get('description', '')
        )
        
        if success:
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n📊 Özet: {success_count} başarılı, {fail_count} başarısız")
    return success_count, fail_count

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Kullanım:")
        print("  python clone_helper.py <clone_url> <full_name> [description]")
        print("  python clone_helper.py --batch <repos.json>")
        print("  python clone_helper.py --stats")
        sys.exit(1)
    
    if sys.argv[1] == "--stats":
        stats = get_clone_stats()
        print(f"\n📊 Clone İstatistikleri:")
        print(f"Toplam: {stats['total']}")
        print("\nKategorilere Göre:")
        for category, count in stats['by_category'].items():
            print(f"  {category}: {count}")
    
    elif sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("❌ Batch dosyası belirtilmedi!")
            sys.exit(1)
        clone_from_list(sys.argv[2])
    
    else:
        clone_url = sys.argv[1]
        full_name = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        
        clone_repository(clone_url, full_name, description)
