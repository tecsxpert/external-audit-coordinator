from flask import request, jsonify
from services.sanitize import sanitize_input

def describe():

    data = request.get_json()
    prompt = data.get("prompt", "")

    # 👇 YOUR CODE GOES HERE
    valid, message = sanitize_input(prompt)

    if not valid:
        return jsonify({
            "error": message
        }), 400

    # continue normal AI logic