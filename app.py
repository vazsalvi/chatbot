from flask import Flask, render_template, jsonify, request
from chat import get_response  # Import get_response from your chat logic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Render the main chat page
@app.route("/",methods=["GET"])
def index_get():
    return render_template("base.html")

# Handle the POST request for predictions
@app.post("/predict")
def predict():
    data = request.get_json()  # Get the message from the request
    print("Received data:", data)  # Debug print

    text = data.get("message") if data else None
    if not text:  # Handle the case where no message is provided
        return jsonify({"answer": "Sorry, I didn't get that. Please try again."})

    # Get the response from your chat logic
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)  # Return the message as JSON


if __name__ == "__main__":
    app.run(debug=True)
