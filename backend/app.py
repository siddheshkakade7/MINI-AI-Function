from flask import Flask, request, jsonify
from flask_cors import CORS
from recommendation import generate_recommendation

app = Flask(__name__)
CORS(app)  #This enables cross-origin requests

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    summary = data.get("summary", "")
    recommendation = generate_recommendation(summary)
    return jsonify({"recommendation": recommendation})

if __name__ == "__main__":
    app.run(debug=True)
