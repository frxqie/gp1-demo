from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

# ✅ Web UI
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        result = add_numbers(num1, num2)

    return render_template("index.html", result=result)

# ✅ JSON API
@app.route("/api")
def api():
    return jsonify({"status": "ok", "message": "Hello from gp1-demo!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)