
## ⚙️ Setup Guide

### 1️⃣ Create a Virtual Environment

Choose **any one** of the following methods:

```bash
# Option 1: Using Conda
conda create -n feelface python=3.10
conda activate feelface

# Option 2: Using venv
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows

# Option 3: Using uv 
uv init
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r app/requirements.txt
```

---

### 3️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

The API will start at:
 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### 4️⃣ Test the API

You can test using `curl` or any tool like Postman:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -F "file=@face.jpg"
```

Response example:

```json
{"emotion": "happy"}
```
