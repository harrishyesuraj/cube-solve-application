# 🧩 Rubik’s Cube Solver Backend

This is the backend service for the **Cube Vision** application.
It processes cube color data and returns the optimal solution using the Kociemba algorithm.

---

## 🚀 Features

* 🔍 Accepts cube state from frontend (manual or camera input)
* 🧠 Solves cube using Kociemba algorithm
* ⚡ Fast and efficient API response
* 🌐 REST API built with FastAPI
* 🔓 CORS enabled for frontend integration

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Kociemba Solver
* Uvicorn

---

## 📦 Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

### ✅ Health Check

```
GET /
```

Response:

```json
{
  "status": "API running"
}
```

---

### 🧩 Solve Cube

```
POST /solve
```

#### Request Body:

```json
{
  "faces": {
    "U": [["W","W","W"],["W","W","W"],["W","W","W"]],
    "R": [["R","R","R"],["R","R","R"],["R","R","R"]],
    "F": [["G","G","G"],["G","G","G"],["G","G","G"]],
    "D": [["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]],
    "L": [["O","O","O"],["O","O","O"],["O","O","O"]],
    "B": [["B","B","B"],["B","B","B"],["B","B","B"]]
  }
}
```

---

#### Response:

```json
{
  "solution": ["R", "U", "R'", "U'"]
}
```

---

## ⚠️ Important Notes

* Each color must appear exactly **9 times**
* Cube must be a **valid configuration**
* Input format must follow correct face order:

  ```
  U, R, F, D, L, B
  ```

---

## 🧠 How It Works

1. Frontend sends cube face data
2. Backend converts it into solver string format
3. Kociemba algorithm computes optimal moves
4. Moves are returned as step-by-step solution

---

## ❌ Error Handling

If cube is invalid:

```json
{
  "error": "Invalid cube or unsolvable configuration"
}
```

---

## 🌍 Deployment

You can deploy this backend on:

* Render
* Railway
* Vercel (serverless with adaptation)

---

## 👨‍💻 Author

**Harrish Yesuraj**
Full Stack Developer

---

## 📌 Future Improvements

* Cube validation before solving
* Better error messages
* Performance optimization
* Logging & monitoring

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
