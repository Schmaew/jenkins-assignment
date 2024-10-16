from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/is_prime/<int:x>")
def is_prime(x):
    if x < 2:
        return jsonify(False)
    
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return jsonify(False)
        
    return jsonify(True)

if __name__ == "__main__":
    app.run(debug=True, port=5001)