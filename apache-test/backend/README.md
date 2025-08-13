# Flask API 後端

這是一個簡單的 Flask API 後端，提供以下端點：

## API 端點

- **GET /api/text** - 回應 "hello world"
- **GET /api/google** - 回應一張 Google 風格的圖片
- **GET /api/time** - 回應當前時間

## 安裝與執行

1. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

2. 執行應用程式：
```bash
python app.py
```

3. 應用程式將在 http://localhost:5000 上運行

## 測試 API

您可以使用以下方式測試 API：

```bash
# 測試文字端點
curl http://localhost:5000/api/text

# 測試圖片端點
curl http://localhost:5000/api/google --output image.png

# 測試時間端點
curl http://localhost:5000/api/time
```

或者直接在瀏覽器中訪問：
- http://localhost:5000/api/text
- http://localhost:5000/api/google
- http://localhost:5000/api/time
