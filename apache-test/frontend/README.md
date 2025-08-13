# Frontend 測試頁面

這個目錄包含一個 HTML 測試頁面，用於測試 Flask API 後端的三個端點。

## 檔案說明

- `index.html` - 主要的測試頁面，包含完整的 API 測試功能

## 使用方法

1. 確保 Flask 後端伺服器正在運行：
   ```bash
   cd ../backend
   python app.py
   ```

2. 打開測試頁面的方式有以下幾種：

   **方法 1: 直接在瀏覽器中打開**
   - 在瀏覽器中打開 `file:///path/to/frontend/index.html`
   
   **方法 2: 使用簡單的 HTTP 伺服器**
   ```bash
   cd frontend
   python -m http.server 3000
   ```
   然後在瀏覽器中訪問 `http://localhost:3000`

## 測試功能

這個測試頁面提供以下功能：

1. **測試 /api/text** - 測試文字回應 API
2. **測試 /api/google** - 測試圖片回應 API
3. **測試 /api/time** - 測試時間回應 API
4. **一鍵測試所有 API** - 連續測試所有三個端點

## 功能特色

- 美觀的響應式界面
- 詳細的錯誤處理和狀態顯示
- 圖片回應的即時預覽
- JSON 回應的格式化顯示
- 自動檢測 Flask 伺服器連接狀態

## 注意事項

- 確保 Flask 後端在 `http://localhost:8080` 運行
- 如果後端運行在不同端口，請修改 HTML 中的 `API_BASE_URL` 變數
- 瀏覽器可能會因為 CORS 政策阻止跨域請求，建議使用 HTTP 伺服器來提供前端頁面
