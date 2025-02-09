from flask import Flask, request, jsonify
from zoho_services import fetch_data_from_zoho

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello, World!"
@app.route("/properties", methods=["POST"])
def get_properties():
    """Fetches properties based on user-provided filters."""
    data = request.get_json()
    filters = data.get("filters", {})

    response = fetch_data_from_zoho(filters)
    
    return jsonify({"result": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
