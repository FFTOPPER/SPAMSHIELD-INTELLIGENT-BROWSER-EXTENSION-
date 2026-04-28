# 🛡️ SpamShield  
### AI-Powered Gmail Spam, Suspicious & Phishing Detection System

SpamShield is a professional **Machine Learning + Browser Extension cybersecurity solution** that detects harmful emails directly inside Gmail in real time.

It combines:

-  Machine Learning Spam Detection Model  
-  Chrome Extension for Gmail  
-  Flask Backend API  
-  Live Monitoring Dashboard  

This project helps users identify:

✅ Safe Emails  
⚠️ Suspicious Emails  
🚨 Spam Emails  
🎣 Phishing Emails  

---

#  Project Preview

## 🔹 Browser Extension Detection

![Extension](assets/Browser%20Extension%20Version.png)

## 🔹 Main Dashboard

![Dashboard](assets/Main%20Dashboard.png)

## 🔹 Safe Email Detection

![Safe](assets/Safe%20Email.png)

## 🔹 Suspicious Email Detection

![Suspicious](assets/Suspicious%20Email.png)

## 🔹 Spam Email Detection

![Spam](assets/Spam%20Email.png)

## 🔹 Phishing Email Detection

![Phishing](assets/Phishing%20Email.png)

---

#  Features

##  Real-Time Gmail Protection

Scans opened Gmail emails instantly.

##  Machine Learning Detection

Uses trained ML model to classify emails.

##  Multi-Level Classification

- Safe  
- Suspicious  
- Spam  
- Phishing  

##  Live Dashboard

Shows:

- Total Emails Scanned  
- Safe Emails  
- Spam Emails  
- Suspicious Emails  
- Phishing Emails  

##  Fast Detection

Response in seconds.

##  Premium UI Alerts

Floating animated result banner inside Gmail.

---

#  Machine Learning Details

## Dataset Used

Combined 3 public datasets:

- SpamAssassin Dataset  
- Enron Spam Dataset  
- LingSpam Dataset  

### Total Cleaned Rows

17,571+

## Model Used

Multinomial Naive Bayes

## Text Processing

TF-IDF Vectorizer

## Accuracy

96.5%

---

#  Final Project Structure

MLT_PROJECT/

- assets/
  - Browser Extension Version.png
  - Extension.png
  - Main Dashboard.png
  - Phishing Email.png
  - Safe Email.png
  - Spam Email.png
  - Suspicious Email.png

- backend/
  - app.py
  - spam_model.pkl
  - vectorizer.pkl

- SpamShield_Extension/
  - background.js
  - content.js
  - manifest.json
  - style.css

---

#  Technology Stack

| Category | Technology |
|----------|------------|
| Backend | Python Flask |
| Machine Learning | Scikit-learn |
| Model | Multinomial Naive Bayes |
| NLP | TF-IDF |
| Extension | JavaScript |
| Frontend | HTML / CSS |
| Browser | Google Chrome |

---

#  Installation Guide

## 1️ Clone Repository

git clone https://github.com/yourusername/SpamShield.git

cd SpamShield

## 2️ Install Python Dependencies

pip install flask flask-cors scikit-learn joblib

## 3️ Run Backend Server

Go to backend folder:

cd backend

python app.py

Server runs at:

http://localhost:5000

Dashboard:

http://localhost:5000/dashboard

---

#  Load Chrome Extension

## Step 1

Open Chrome browser and go to:

chrome://extensions/

## Step 2

Enable:

Developer Mode

(top-right corner)

## Step 3

Click:

Load Unpacked

## Step 4

Select folder:

SpamShield_Extension

## Step 5

Extension installed successfully 

---

#  How to Use

## Step 1

Keep Flask backend running.

## Step 2

Open Gmail:

https://mail.google.com

## Step 3

Open any email.

## Step 4

SpamShield automatically scans email content.

## Step 5

Result appears as top banner:

- ✅ Safe Email  
- ⚠️ Suspicious Email  
- 🚨 Spam Email  
- 🎣 Phishing Alert  

---

# 📊 Dashboard Monitoring

Visit:

http://localhost:5000/dashboard

Tracks:

- Total Scanned  
- Safe Count  
- Spam Count  
- Suspicious Count  
- Phishing Count  
- Last Detection Result  

---

#  Sample Predictions

| Email Content | Result |
|--------------|--------|
| Meeting at 5 PM tomorrow | Safe |
| Limited offer expires soon | Suspicious |
| Win ₹50,000 now click here | Spam |
| Verify your bank account now | Phishing |

---

#  Security Use Cases

- Personal Gmail Protection  
- Company Email Security  
- Phishing Awareness  
- Educational Cybersecurity Demo  
- Smart Email Filtering  

---

#  Future Enhancements

- Outlook Support  
- Yahoo Mail Support  
- BERT Deep Learning Model  
- Cloud Deployment  
- User Login System  
- Admin Analytics Panel  
- Auto Email Blocking  

---

#  Why This Project Matters

SpamShield demonstrates how AI can be used in real-world cybersecurity systems to protect users from scams, fraud, and malicious emails.

---

# 👨‍💻 Author

**Adheje B**

Machine Learning | Cybersecurity | Full Stack Development

---

#  Support

If you like this project:

- Star ⭐ the repository  
- Fork 🍴 the project  
- Contribute 🚀 improvements  

---

# 📜 License

This project is developed for educational and portfolio purposes.
