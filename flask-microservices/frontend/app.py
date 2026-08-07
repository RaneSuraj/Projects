from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# Service discovery via environment variable
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5001')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            # Send data to the backend API
            try:
                requests.post(f'{BACKEND_URL}/api/messages', json={'content': content})
            except requests.exceptions.RequestException as e:
                print(f"Backend connection error: {e}")
        return redirect(url_for('index'))

    # GET request: Fetch data from the backend API
    try:
        response = requests.get(f'{BACKEND_URL}/api/messages')
        messages = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        messages = [{'content': '⚠️ Error: Could not connect to the backend service.'}]

    return render_template('index.html', messages=messages)

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == '__main__':
    # Frontend runs on port 5000
    app.run(host='0.0.0.0', port=5000)
