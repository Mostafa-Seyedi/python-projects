"""
This script demonstrates how to work with Web Modules in Python.

📌 What is an API?
------------------
API stands for Application Programming Interface. It allows different software 
applications to communicate with each other. In web development, APIs are often 
used to send and receive data over the internet. A common type is a REST API, 
which uses HTTP methods like GET and POST to exchange data, often in JSON format.

📌 What is Flask?
------------------
Flask is a lightweight web framework in Python that allows you to build web 
applications and create your own APIs. You can define routes that respond with 
text, HTML, or JSON data — making it easy to expose your own Python code as a 
web service that others can interact with.

Covered Concepts:
-----------------
1. JSON data handling in Python (dumps & loads)
2. Calling public APIs using `requests`
3. Sending data with a POST request
4. Creating a simple REST API using Flask

Useful Libraries:
-----------------
- `requests` : to interact with external APIs
- `json`     : to handle JSON data (convert Python ↔ JSON)
- `flask`    : to create your own API endpoints
"""
""

# ---------- 1. JSON Handling Example ----------
import json

# Python dictionary to JSON
data = {"name": "Alex", "age": 34, "Hobby": "Football", "Coolness": 6}
json_string = json.dumps(data)
print("🔁 JSON Format:", json_string)

# JSON back to Python dictionary
parsed_data = json.loads(json_string)
print("📦 Python Dictionary:", parsed_data)


# ---------- 2. Calling a Public API (GET request) ----------
import requests

# Example: astronauts currently in space
api_url = "http://api.open-notify.org/astros.json"
response = requests.get(api_url)

if response.status_code == 200:
    json_data = response.json()
    print(f"\n🚀 Number of people in space: {json_data['number']}")
    
    print("👨‍🚀 Astronauts:")
    for person in json_data['people']:
        print(f"- {person['name']} ({person['craft']})")
else:
    print(f"❌ Error fetching data: {response.status_code}")


# ---------- 3. Another API Example: Bitcoin Price ----------
btc_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
btc_response = requests.get(btc_url)

if btc_response.status_code == 200:
    btc_data = btc_response.json()
    print(f"\n💰 Current Bitcoin Price (USD): ${btc_data['bitcoin']['usd']}")
else:
    print(f"❌ Error fetching BTC price: {btc_response.status_code}")


# ---------- 4. POST Request Example ----------
post_url = "https://httpbin.org/post"
payload = {
    "name": "Alex",
    "job": "Developer",
    "age": 24,
    "hobby": "sports"
}

post_response = requests.post(post_url, json=payload)

print("\n📨 POST Request Response:")
if post_response.status_code in [200, 201]:
    print("✅ Success:", post_response.json())
else:
    print("❌ Error:", post_response.status_code, post_response.text)


# ---------- 5. Creating Your Own API using Flask ----------
"""
To run the Flask app:
---------------------
1. Save the following code in a separate file, e.g., `my_flask_api.py`
2. Run it using: `python my_flask_api.py`
3. Open browser at: http://127.0.0.1:5000/

This creates a simple API that returns plain text or JSON data.
"""

# === Save this in a separate file if running Flask ===
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/user")
def user():
    return jsonify({
        "name": "Alex",
        "age": 34,
        "hobby": "Football"
    })

if __name__ == "__main__":
    app.run(debug=True)
"""
