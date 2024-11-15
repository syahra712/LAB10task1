from flask import Flask, request, jsonify
import requests
from flask import render_template_string

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "AIzaSyCx13fbPx6FC4nUYkVlWWDKIJAoY9fHR8g"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

def get_ai_response(user_input):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {"parts": [{"text": user_input}]}
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response_json = response.json()
        if "candidates" in response_json:
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "I'm sorry, I couldn't process your request. Please try again."
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chatbot</title>
        <script>
            async function sendMessage() {
                const userInput = document.getElementById("userInput").value;
                const responseContainer = document.getElementById("responseContainer");
                responseContainer.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
                
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: userInput })
                });
                const data = await response.json();
                responseContainer.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
                document.getElementById("userInput").value = '';
            }
        </script>
    </head>
    <body>
        <h1>Chatbot</h1>
        <div id="responseContainer" style="border:1px solid #000; padding: 10px; height: 300px; overflow-y: scroll;">
        </div>
        <input type="text" id="userInput" placeholder="Type your message..." />
        <button onclick="sendMessage()">Send</button>
    </body>
    </html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = get_ai_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
