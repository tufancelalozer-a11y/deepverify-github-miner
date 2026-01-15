"""
DeepVerify GitHub Miner - Local Server
Web arayüzü ile clone_helper.py arasında köprü görevi görür.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import json
from clone_helper import clone_repository, get_clone_stats

app = Flask(__name__)
CORS(app)  # Web arayüzünden erişim için

@app.route('/api/clone', methods=['POST'])
def clone_repo():
    """Tek bir repository klonla"""
    try:
        data = request.json
        clone_url = data.get('clone_url')
        full_name = data.get('full_name')
        description = data.get('description', '')
        
        if not clone_url or not full_name:
            return jsonify({
                'success': False,
                'error': 'clone_url ve full_name gerekli'
            }), 400
        
        success, result = clone_repository(clone_url, full_name, description)
        
        return jsonify({
            'success': success,
            'message': result if success else f'Hata: {result}',
            'path': result if success else None
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/clone-batch', methods=['POST'])
def clone_batch():
    """Birden fazla repository klonla"""
    try:
        data = request.json
        repos = data.get('repos', [])
        
        if not repos:
            return jsonify({
                'success': False,
                'error': 'repos listesi boş'
            }), 400
        
        results = []
        success_count = 0
        fail_count = 0
        
        for repo in repos:
            success, result = clone_repository(
                repo['clone_url'],
                repo['full_name'],
                repo.get('description', '')
            )
            
            results.append({
                'full_name': repo['full_name'],
                'success': success,
                'message': result if not success else 'Başarılı'
            })
            
            if success:
                success_count += 1
            else:
                fail_count += 1
        
        return jsonify({
            'success': True,
            'results': results,
            'summary': {
                'total': len(repos),
                'success': success_count,
                'failed': fail_count
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    """Clone istatistiklerini getir"""
    try:
        stats = get_clone_stats()
        return jsonify({
            'success': True,
            'stats': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Server sağlık kontrolü"""
    return jsonify({
        'status': 'healthy',
        'message': 'DeepVerify Clone Server çalışıyor'
    })

if __name__ == '__main__':
    print("🚀 DeepVerify Clone Server başlatılıyor...")
    print("📍 Server adresi: http://localhost:5000")
    print("💡 Web arayüzünü açın: C:\\Google Antigravity\\deepverify-github-miner.html")
    print("\n⚠️  Server'ı durdurmak için Ctrl+C")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
