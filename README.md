A **FastAPI-powered news application** with a simple, responsive frontend.
It fetches news from an API, stores it in a database, and allows users to:

* **Browse news** by category (`Business`, `Technology`, `Sports`, `Health`)
* **Search news** from the database and API
* **Automatically store and update articles**
* **Serve results via a clean frontend interface**

---

## 🚀 Features

* **FastAPI backend** for handling routes and API calls
* **SQLite (or PostgreSQL)** for storing fetched news articles
* **Category-based browsing** (`/news/{category}`)
* **Search feature** that:

  1. Checks the database first
  2. Falls back to an external API if no results are found
* **Automatic storage** of API results into the DB
* **Responsive frontend** styled with **TailwindCSS**
* **JSON API responses** for easy frontend integration

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
j
```bash
git clone https://github.com/yourusername/news-aggregator.git
cd news-aggregator
```

### 2️⃣ Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file in the project root:

```
NEWS_API_KEY=your_newsapi_key_here
BASE_URL=https://newsapi.org/v2
DATABASE_URL=sqlite:///./news.db
```

### 4️⃣ Run the App

```bash
uvicorn main:app --reload
```

The app will be available at:
🔗 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🖥️ Usage

### Browse News by Category

```
GET /news/{category}
Example: /news/technology
```

### Search News

```
GET /news/search/{query}
Example: /news/search/bitcoin
```

If no results are found in the DB, the app will fetch from the API and save the results.

---

## 💾 Database Reset (Development Only)

To clear all data and reset tables:

```python
from database import engine
from models import Base
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
```

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, SQLAlchemy
* **Frontend:** HTML, TailwindCSS, JavaScript
* **Database:** SQLite
* **External API:** NewsAPI.org

---

## 📌 Future Improvements

* [ ] Recommendation system for personalized news
* [ ] Improved search relevance ranking
* [ ] User authentication and saved articles
* [ ] Pagination for large result sets

---

## 📜 License

MIT License © 2025 Ekwenye Joseph
