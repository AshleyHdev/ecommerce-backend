📌 電子商務後端 API - Ecommerce Backend API

## 📌 作品介紹  

### 1️⃣ **E-commerce Backend（電商後端系統）**

這個 **Commerce Backend** 不只是一般的後端開發練習，而是真正能幫助小型商家快速搭建購物平台，適用於：

✔ **個人賣家 & 小型電商**（Shopee、Instagram 賣家、獨立品牌）  
   - 可用來管理 **產品目錄、訂單、庫存、客戶資訊**，不用依賴第三方平台。  
   - 適合那些 **不想使用 Shopify 或 SaaS 平台的商家**，自己架設一個輕量級後端管理系統。  

✔ **創業初期的商家（餐廳、手工藝品、獨立書店）**  
   - 想要 **擁有自己的線上商店**，但不想每月花費高額訂閱費，這個後端可以作為 MVP（最小可行產品），快速上線。  

✔ **企業級系統的雛形 & 可客製化擴展**  
   - 如果企業想要 **內部開發專屬電商管理系統**，這個後端可以作為基礎，後續加入 **支付、物流、行銷分析等功能**。  

💡 **總結**：這套後端系統適合 **小型商家、獨立品牌、甚至企業內部開發團隊**，能夠提供 **靈活的電商解決方案**，擺脫昂貴的訂閱制平台！  

---

📌 API 端點

📍 商品管理

| 方法 | 端點 | 描述 |
|------|------|------|
| POST | /products/ | 創建新商品 |
| GET | /products/ | 取得所有商品 |
| GET | /products/{product_id} | 取得特定商品 |
| PUT | /products/{product_id} | 更新商品 |
| DELETE | /products/{product_id} | 刪除商品 |

📍 類別管理

| 方法 | 端點 | 描述 |
|------|------|------|
|POST | /categories/ | 創建新類別
|GET | /categories/ | 取得所有類別
|GET | /categories/{category_id} | 取得特定類別
|PUT | /categories/{category_id} | 更新類別
|DELETE | /categories/{category_id} | 刪除類別

這是一個使用 FastAPI 和 PostgreSQL 建立的電子商務後端 API，提供 商品管理、類別管理、資料庫存取 等功能，並支援 Heroku 雲端部署。開發者可以透過 Swagger UI 測試 API，並將其整合至前端應用程式。

---

📌 目錄
 • 🌟 主要功能
 • 🚀 環境需求
 • 🔧 安裝與設定
 • 🖥️ 啟動專案
 • 📌 API 端點
 • 🛠️ 核心技術
 • 📄 專案結構

🌟 主要功能

✅ 商品管理：支援 CRUD 操作（新增、查詢、更新、刪除）
✅ 分類管理：支援 CRUD 操作（新增、查詢、更新、刪除）
✅ PostgreSQL 整合：使用 SQLAlchemy 進行高效、安全的資料存取
✅ API 文件支援：使用 Swagger UI，方便開發者進行 API 測試
✅ Heroku 雲端部署：支援雲端環境運行 API

🚀 環境需求

請確保您的系統已安裝以下工具：
 • Python 3.10+
 • pip 22.0+
 • Git
 • PostgreSQL（或其他 SQL 資料庫）
 • Heroku CLI（若需部署至 Heroku）

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

1️⃣**設定環境變數**
請在專案根目錄 **創建 .env 檔案**，並填入以下內容：

DATABASE_URL=postgresql://使用者名稱:密碼@localhost:5432/ecommerce_db
SECRET_KEY=your_secret_key

2️⃣ 啟動 FastAPI 伺服器

uvicorn app.main:app --reload

啟動伺服器後，您可以透過以下方式存取 API：
 • Swagger UI（API 文件） 👉 http://127.0.0.1:8000/docs
 • 查看 OpenAPI JSON 👉 http://127.0.0.1:8000/openapi.json


📌 詳細 API 文件 👉 http://127.0.0.1:8000/docs

🛠️ 核心技術

技術 用途
FastAPI 建立高效能 API
PostgreSQL 資料庫管理
SQLAlchemy ORM 操作資料庫
Pydantic 資料驗證與模式定義
Heroku 雲端部署
Swagger UI API 文件與測試
Uvicorn 執行 FastAPI 伺服器

📄 專案結構

ecommerce-backend/
│── app/
│   ├── __init__.py
│   ├── main.py  # FastAPI 入口點
│   ├── database.py  # 資料庫初始化
│   ├── models.py  # SQLAlchemy ORM 模型
│   ├── schemas.py  # Pydantic 資料驗證
│   ├── crud.py  # 資料庫操作
│   ├── routes/  # API 路由
│   │   ├── products.py
│   │   ├── categories.py
│── .gitignore
│── requirements.txt  # 相依套件
│── README.md  # 自述文件（本文件）

🔹 更新內容（2025-02-25）

✅ 修正 schemas.py 和 routes 錯誤，確保 API 正確運行
✅ 優化 .gitignore，忽略 venv/ 目錄，避免不必要的 Git 追蹤
✅ 修復 Heroku 部署問題，確保雲端環境正常運行
✅ 增強 API 文件，讓開發者更容易測試與使用 API

---

## **🔹 其他技術專案**
- **未來即將上傳更多作品，敬請期待！🚀**

📌 E-commerce Backend API

This is an E-commerce Backend API built with FastAPI and PostgreSQL, providing product management, category management, and database access functionalities. It supports Heroku cloud deployment, and developers can test the API using Swagger UI and integrate it with frontend applications.

📌 Table of Contents
 • 🌟 Key Features
 • 🚀 System Requirements
 • 🔧 Installation & Setup
 • 🖥️ Starting the Project
 • 📌 API Endpoints
 • 🛠️ Core Technologies
 • 📄 Project Structure

🌟 Key Features

✅ Product Management: Full CRUD operations (Create, Read, Update, Delete)
✅ Category Management: Full CRUD operations (Create, Read, Update, Delete)
✅ PostgreSQL Integration: Efficient and secure data storage with SQLAlchemy ORM
✅ API Documentation Support: Built-in Swagger UI for easy API exploration
✅ Heroku Cloud Deployment: Supports cloud-based API hosting

🚀 System Requirements

Ensure your system has the following dependencies installed:
 • Python 3.10+
 • pip 22.0+
 • Git
 • PostgreSQL (or any SQL database)
 • Heroku CLI (for cloud deployment, if needed)

🔧 Installation & Setup

1️⃣ Clone the Project

git clone https://github.com/AshleyHdev/ecommerce-backend.git
cd ecommerce-backend

2️⃣ Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

🖥️ Starting the Project

1️⃣ Set Up Environment Variables (.env)

Create a .env file in the project root directory and add the following:

DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
SECRET_KEY=your_secret_key

2️⃣ Start the FastAPI Server

uvicorn app.main:app --reload

After starting the server, you can access the API via:
 • Swagger UI (API Docs) 👉 http://127.0.0.1:8000/docs
 • OpenAPI JSON 👉 http://127.0.0.1:8000/openapi.json

📌 API Endpoints

📍 Product Management

Method Endpoint Description
POST /products/ Create a new product
GET /products/ Retrieve all products
GET /products/{product_id} Retrieve a specific product
PUT /products/{product_id} Update a product
DELETE /products/{product_id} Delete a product

📍 Category Management

Method Endpoint Description
POST /categories/ Create a new category
GET /categories/ Retrieve all categories
GET /categories/{category_id} Retrieve a specific category
PUT /categories/{category_id} Update a category
DELETE /categories/{category_id} Delete a category

📌 API Documentation 👉 http://127.0.0.1:8000/docs

🛠️ Core Technologies

Technology Purpose
FastAPI High-performance API framework
PostgreSQL Database management
SQLAlchemy ORM for database operations
Pydantic Data validation and serialization
Heroku Cloud deployment
Swagger UI API documentation & testing
Uvicorn FastAPI server execution

📄 Project Structure

ecommerce-backend/
│── app/
│   ├── __init__.py
│   ├── main.py  # FastAPI entry point
│   ├── database.py  # Database initialization
│   ├── models.py  # SQLAlchemy ORM models
│   ├── schemas.py  # Pydantic data validation
│   ├── crud.py  # Database operations
│   ├── routes/  # API routes
│   │   ├── products.py
│   │   ├── categories.py
│── .gitignore
│── requirements.txt  # Dependency file
│── README.md  # Project documentation (this file)

🔹 Recent Updates (2025-02-25)

✅ Fixed schemas.py and routes issues to ensure proper API functionality
✅ Updated .gitignore to properly ignore venv/ directory
✅ Resolved Heroku deployment issues to ensure smooth cloud execution
✅ Enhanced API documentation for better usability
