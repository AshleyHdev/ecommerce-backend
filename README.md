📌 E-commerce Backend API - 電子商務後端 API

這是一個基於 FastAPI 和 PostgreSQL 的 電子商務後端 API，提供 商品管理、分類管理、資料庫存取 等功能，並支援 Heroku 雲端部署。透過 Swagger UI，開發者可以輕鬆測試 API，並與前端應用整合。

📌 目錄
 • 🌟 主要功能
 • 🚀 環境需求
 • 🔧 安裝與設定
 • 🖥️ 啟動專案
 • 📌 API 端點
 • 🛠️ 主要技術
 • 📄 目錄結構

🌟 主要功能

✅ 商品管理：支援 CRUD 操作（建立、查詢、更新、刪除）
✅ 分類管理：支援 CRUD 操作
✅ PostgreSQL 進行資料存取
✅ Heroku 雲端部署
✅ Swagger UI API 文件，方便開發者進行查閱與測試

🚀 環境需求

請確保你的系統已安裝以下環境：
 • Python 3.10+
 • pip 22.0+
 • Git
 • PostgreSQL（或其他 SQL 資料庫）
 • Heroku CLI（若需雲端部署）

🔧 安裝與設定

1️⃣ 克隆專案

git clone https://github.com/AshleyHdev/ecommerce-backend.git
cd ecommerce-backend

2️⃣ 建立虛擬環境

python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ 安裝相依套件

pip install -r requirements.txt

🖥️ 啟動專案

1️⃣ 設定環境變數（.env）

DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
SECRET_KEY=your_secret_key

2️⃣ 啟動 FastAPI 伺服器

uvicorn ecommerce.main:app --reload

啟動後，你可以透過以下方式訪問 API：
 • Swagger UI（API Docs） 👉 http://127.0.0.1:8000/docs
 • 查看 OpenAPI JSON 👉 http://127.0.0.1:8000/openapi.json

📌 API 端點

📍 商品管理

方法 端點 描述
POST /products/products/ 新增 商品
GET /products/products/ 查詢 所有商品
GET /products/products/{product_id} 查詢 單個商品
PUT /products/products/{product_id} 更新 商品
DELETE /products/products/{product_id} 刪除 商品

📍 分類管理

方法 端點 描述
POST /categories/ 新增 分類
GET /categories/ 查詢 所有分類

📌 詳細 API 文件 👉 http://127.0.0.1:8000/docs

🛠️ 主要技術

技術 用途
FastAPI 構建 API 服務
PostgreSQL 資料庫存取
SQLAlchemy ORM 操作資料庫
Pydantic 數據驗證
Heroku 雲端部署
Swagger UI API 文件查閱與測試
Uvicorn 運行 FastAPI 伺服器

📄 目錄結構

ecommerce-backend/
│── ecommerce/
│   ├── __init__.py
│   ├── main.py       # 主應用程式
│   ├── database.py   # 資料庫初始化
│   ├── models.py     # 資料庫模型
│   ├── schemas.py    # Pydantic 數據模型
│   ├── crud.py       # 資料庫操作函數
│   ├── routes/       # API 路由
│── requirements.txt  # 相依套件
│── README.md         # 自述文件（本檔案）

🔹 更新內容（2025-02-05）

✅ 商品與分類管理：支援 CRUD 操作，方便用戶維護電子商務平台商品與分類。
✅ PostgreSQL 整合：提供 SQLAlchemy ORM 模型，確保高效、安全的資料存取。
✅ API 文件強化：透過 Swagger UI，開發者可視化查閱 API 端點，提升開發體驗。
✅ Heroku 雲端部署：專案已成功部署至 Heroku，提供雲端 API 服務。
