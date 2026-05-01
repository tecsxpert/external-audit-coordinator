from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
# from services.sanitize import sanitize_input

import re

BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"bypass security",
    r"drop\s+table",
    r"or\s+1=1",
    r"<script.*?>"
]

def sanitize_input(user_input):

    # Empty input check
    if not user_input or not user_input.strip():
        return False, "Input cannot be empty"

    # HTML detection (strip/block)
    if re.search(r"<[^>]+>", user_input):
        return False, "HTML content is not allowed"

    # Prompt injection detection
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False, "Potential malicious input detected"

    return True, "Valid input"

# from services.rate_limiting import setup_rate_limiting

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

# Setup rate limiting
# limiter = setup_rate_limiting(app)

@app.route('/test', methods=['GET'])
def test():
    return "OK"

@app.route('/describe', methods=['POST'])
def describe_endpoint():
    data = request.get_json()
    prompt = data.get("prompt", "")

    # 👇 YOUR CODE GOES HERE
    valid, message = sanitize_input(prompt)

    if not valid:
        return jsonify({
            "error": message
        }), 400

    # continue normal AI logic
    return jsonify({"message": "Prompt processed successfully"}), 200

@app.route('/generate-report', methods=['POST'])
# @limiter.limit("10 per minute")
def generate_report():
    # Placeholder for generate report logic
    return {"message": "Report generated"}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)