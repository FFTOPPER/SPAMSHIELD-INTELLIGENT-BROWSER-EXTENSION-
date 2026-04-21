from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Dashboard stats
stats = {
    "total": 0,
    "safe": 0,
    "spam": 0,
    "suspicious": 0,
    "phishing": 0,
    "last_result": "None"
}

@app.route("/")
def home():
    return "SpamShield API Running"


@app.route("/dashboard")
def dashboard():

    html = f"""
    <html>
    <head>
        <title>SpamShield Dashboard</title>

        <meta http-equiv="refresh" content="2">

        <style>
            body {{
                margin:0;
                padding:30px;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg,#0f172a,#1e293b);
                color:white;
                text-align:center;
            }}

            h1 {{
                margin-bottom:30px;
                font-size:42px;
            }}

            .container {{
                display:flex;
                flex-wrap:wrap;
                justify-content:center;
                gap:20px;
            }}

            .card {{
                width:220px;
                padding:25px;
                border-radius:18px;
                font-size:24px;
                font-weight:bold;
                box-shadow:0 10px 25px rgba(0,0,0,0.25);
            }}

            .blue {{background:linear-gradient(135deg,#007bff,#00c6ff);}}
            .green {{background:linear-gradient(135deg,#16a34a,#22c55e);}}
            .red {{background:linear-gradient(135deg,#dc2626,#ef4444);}}
            .orange {{background:linear-gradient(135deg,#ea580c,#f59e0b);}}
            .purple {{background:linear-gradient(135deg,#7c3aed,#a855f7);}}

            .label {{
                font-size:18px;
                margin-bottom:10px;
                opacity:0.9;
            }}

            .value {{
                font-size:38px;
            }}

            .footer {{
                margin-top:40px;
                font-size:26px;
                font-weight:bold;
            }}
        </style>
    </head>

    <body>

        <h1>🛡 SpamShield Dashboard</h1>

        <div class="container">

            <div class="card blue">
                <div class="label">Total Scanned</div>
                <div class="value">{stats["total"]}</div>
            </div>

            <div class="card green">
                <div class="label">Safe</div>
                <div class="value">{stats["safe"]}</div>
            </div>

            <div class="card red">
                <div class="label">Spam</div>
                <div class="value">{stats["spam"]}</div>
            </div>

            <div class="card orange">
                <div class="label">Suspicious</div>
                <div class="value">{stats["suspicious"]}</div>
            </div>

            <div class="card purple">
                <div class="label">Phishing</div>
                <div class="value">{stats["phishing"]}</div>
            </div>

        </div>

        <div class="footer">
            Last Result: {stats["last_result"]}
        </div>

    </body>
    </html>
    """

    return render_template_string(html)


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    text = data.get("text", "").lower()

    vec = vectorizer.transform([text])
    prob = model.predict_proba(vec)[0]

    spam_score = prob[1] * 100
    reasons = []

    # Spam keywords
    spam_words = [
        "won", "reward", "claim", "offer",
        "free", "lottery", "$", "urgent"
    ]

    for word in spam_words:
        if word in text:
            spam_score += 8
            reasons.append(f"Contains '{word}'")

    # Phishing keywords
    phishing_words = [
        "verify account",
        "reset password",
        "login now",
        "click link",
        "bank account",
        "security alert",
        "confirm identity",
        "update payment",
        "suspended account",
        "unauthorized login"
    ]

    phishing_found = False

    for word in phishing_words:
        if word in text:
            phishing_found = True
            spam_score += 15
            reasons.append(f"Contains '{word}'")

    if spam_score > 100:
        spam_score = 100

    if spam_score >= 70:
        reasons.append("High spam probability")
    elif spam_score >= 35:
        reasons.append("Moderate risk detected")

    # Final result
    if phishing_found:
        result = "Phishing"
    elif spam_score >= 65:
        result = "Spam"
    elif spam_score >= 35:
        result = "Suspicious"
    else:
        result = "Safe"

    stats["total"] += 1
    stats[result.lower()] += 1
    stats["last_result"] = result

    return jsonify({
        "prediction": result,
        "spam_score": round(spam_score, 2),
        "reasons": reasons[:4]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)