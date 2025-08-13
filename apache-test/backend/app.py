from flask import Flask, jsonify, send_file
from datetime import datetime
import io
import requests
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# 添加 CORS 支援
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/api/text')
def get_text():
    """回應 hello world"""
    return jsonify({"message": "hello world"})

@app.route('/api/google')
def get_google_image():
    """回應一張圖片"""
    try:
        # 創建一個簡單的圖片（因為直接從 Google 下載圖片可能有版權問題）
        # 這裡我們創建一個帶有 Google 標誌顏色的簡單圖片
        img = Image.new('RGB', (400, 200), color='white')
        draw = ImageDraw.Draw(img)
        
        # 畫一個簡單的 Google 風格的圖
        colors = ['#4285F4', '#EA4335', '#FBBC05', '#34A853']
        for i, color in enumerate(colors):
            x = 50 + i * 80
            draw.rectangle([x, 75, x + 60, 125], fill=color)
        
        # 添加文字
        try:
            # 嘗試使用系統字體
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 20)
        except:
            # 如果找不到字體，使用默認字體
            font = ImageFont.load_default()
        
        draw.text((150, 140), "Google Style Image", fill='black', font=font)
        
        # 將圖片轉換為字節流
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    except Exception as e:
        return jsonify({"error": f"無法生成圖片: {str(e)}"}), 500

@app.route('/api/time')
def get_current_time():
    """回應現在時間"""
    current_time = datetime.now()
    return jsonify({
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": current_time.timestamp(),
        "timezone": str(current_time.astimezone().tzinfo)
    })

@app.route('/')
def home():
    """首頁，顯示可用的 API 端點"""
    return jsonify({
        "message": "Flask API 後端",
        "endpoints": {
            "/api/text": "回應 hello world",
            "/api/google": "回應一張圖片",
            "/api/time": "回應現在時間"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
