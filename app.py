from flask import Flask, request, jsonify
from detector import detect_prompt_injection

app = Flask(__name__)

@app.route("/")
def home():
    return "Prompt Injection Guard is running."

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_input = data.get("input", "")

    result = detect_prompt_injection(user_input)

    return jsonify({
        "input": user_input,
        "risk_level": result["risk"],
        "action": result["action"],
        "details": result["matches"]
    })

if __name__ == "__main__":
    app.run(debug=True)