Here’s the **full set of commands to set up a FastAPI environment on your MacBook**, from scratch to running your first endpoint. ✅

---

## ✅ **1. Open Terminal & Create Project Folder**

```bash
mkdir fastapi-news-app
cd fastapi-news-app
```

---

## ✅ **2. Create & Activate Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

(You’ll see `(venv)` in your terminal now.)

---

## ✅ **3. Install FastAPI & Uvicorn**

```bash
pip install fastapi uvicorn
```

*(Later we’ll install SQLAlchemy, Requests, etc.)*

---

## ✅ **4. Create the FastAPI App**

Create a file named **`main.py`**:

```bash
touch main.py
```

Then open and edit it (you can use VS Code or Nano):

```bash
nano main.py
```

Paste this inside:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI News App!"}
```

Save in nano:
`CTRL + O` → Enter → `CTRL + X`

---

## ✅ **5. Run the FastAPI Server**

```bash
uvicorn main:app --reload
```

* Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000) →

```json
{"message": "Hello, FastAPI News App!"}
```

* Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → Swagger Docs.

---

## ✅ **6. Save Dependencies (Optional but Recommended)**

When done:

```bash
pip freeze > requirements.txt
```

---

## ✅ **Next Step Options**

Do you want me to now give you:
✅ **A)** All the commands to **set up database support (FastAPI + SQLAlchemy + SQLite/Postgres)**
✅ **B)** All the commands to **fetch news from an API (MVP News Fetcher)**
✅ **C)** Full **project folder structure for the news app** before coding

Which should we do next?
