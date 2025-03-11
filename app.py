from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "PASTE_YOUR_API_KEY_HERE"

@app.route("/")
def home():
    return """<form action='/generate'>
                <input name='topic' placeholder='Topic likho...'>
                <button type='submit'>Generate</button>
              </form>"""

@app.route("/generate")
def generate():
    topic = request.args.get("topic", "")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    data = {
        "contents": [{
            "parts": [{"text": f"Ek detailed blog likho: {topic}"}]
        }]
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=data, headers=headers)
        res_json = response.json()
        output = res_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Kuch galat ho gaya!")
        return output
    except Exception as e:
        return jsonify({"error": "API request failed", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
