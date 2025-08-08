# Bytewash MVP

Bytewash is a minimal Flask web application for uploading CSV/Excel files, cleaning them (removing duplicates, standardizing text), and generating a simple HTML data quality report.

## 📦 Features
- Upload `.csv` or `.xlsx` files
- Automatic duplicate removal
- Missing value counts per column
- Text normalization (title case)
- Downloadable HTML report with a preview of cleaned data

---

## 🛠️ Prerequisites
- Python 3.12+ installed  
- `pip` package manager available in your terminal

---

## 📂 Project Structure
Bytewash/
├── app.py # Flask app code
├── uploads/ # Uploaded files (auto-created)
├── reports/ # Generated reports (auto-created)
├── templates/ # HTML templates
└── README.md

---

## 🚀 Setup & Run Locally

### 1. Clone or download the project
```bash
git clone https://github.com/your-username/bytewash.git
cd bytewash
```

### 2. Install dependencies & run
```bash
pip install flask pandas openpyxl
python app.py
```

### 5. Open the app in your browser
Visit http://127.0.0.1:5000

