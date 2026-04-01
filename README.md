# 🏏 Cricklytics

## 📌 Project Title
Cricklytics: AI-Powered Real-Time Cricket Score Analysis and Win Prediction System

---

## 📝 Description
Cricklytics is a real-time cricket analytics system that tracks live match data and visualizes score progression. It uses machine learning to predict match outcomes and provide intelligent insights during gameplay.

---

## 🚀 Features
- 📊 Live Cricket Score Tracking
- 📈 Score Progress Graph (Chart.js)
- 🧠 AI-Based Win Prediction
- ⚡ Real-Time Updates (Auto Refresh)
- 🔍 Smart Match Insights
- 🛠️ API Integration (CricAPI)

---

## 🧰 Technologies Used

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Backend
- Python (Flask)
- Flask-CORS

### Machine Learning
- Scikit-learn (Logistic Regression)
- Pandas
- Pickle

---

## 📁 Project Structure


cricklytics/
│
├── backend/
│ ├── app.py
│ └── model/
│ ├── train_model.py
│ └── model.pkl
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone Project

git clone https://github.com/your-username/cricklytics.git

cd cricklytics


---

### 2. Setup Backend


cd backend
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors requests scikit-learn pandas


---

### 3. Run Backend


python app.py


Server runs at:

http://127.0.0.1:5000


---

### 4. Run Frontend

Option 1:
- Open `frontend/index.html`

Option 2:

cd frontend
python -m http.server 5500


Open:

http://localhost:5500


---

## 🔑 API Setup

- Get free API key from CricAPI
- Replace in `app.py`:


API_KEY = "YOUR_API_KEY"


---

## 🧠 Machine Learning Model

- Algorithm: Logistic Regression
- Inputs:
  - Runs
  - Overs
  - Wickets
  - Target
- Output:
  - Win probability (%)

---

## 📊 Output

- Live match score
- Score progression graph
- AI win prediction
- Smart insights

---

## 🏆 Future Enhancements

- Player performance analytics
- Multi-match dashboard
- Mobile responsive UI
- Deep learning prediction model

---




## 👨‍💻 Author
Sarvaji M

---

## 📜 License
This project is for academic and educational purposes.


<img width="1365" height="767" alt="Screenshot 2026-04-01 132631" src="https://github.com/user-attachments/assets/43dcab8f-a1fc-455a-a6bd-792d7cb07eac" />
