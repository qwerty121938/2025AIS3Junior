# Flask API 專案

這是一個完整的 Flask API 專案，包含後端 API 服務和前端測試頁面。

## 專案結構

```
apache-rev-proxy-test/
├── backend/           # Flask API 後端
│   ├── app.py        # 主要 Flask 應用程式
│   ├── requirements.txt
│   └── README.md
├── frontend/         # 前端測試頁面
│   ├── index.html   # API 測試頁面
│   └── README.md
└── README.md        # 專案說明
```

## API 端點

- **GET /api/text** - 回應 "hello world"
- **GET /api/google** - 回應一張 Google 風格的圖片
- **GET /api/time** - 回應當前時間

## 快速開始

### 1. 啟動後端服務

```bash
cd backend
pip install -r requirements.txt
python app.py
```

後端服務將在 `http://localhost:8080` 啟動

### 2. 測試 API

您可以使用以下方式測試 API：

#### 使用前端測試頁面
在瀏覽器中打開 `frontend/index.html` 檔案，或者：

```bash
cd frontend
python -m http.server 3000
```

然後訪問 `http://localhost:3000`

#### 使用 curl 命令

```bash
# 測試文字端點
curl http://localhost:8080/api/text

# 測試圖片端點
curl http://localhost:8080/api/google --output image.png

# 測試時間端點
curl http://localhost:8080/api/time
```

## 功能特色

- 響應式網頁界面
- 完整的錯誤處理
- 圖片即時預覽
- JSON 格式化顯示
- 一鍵測試所有 API
