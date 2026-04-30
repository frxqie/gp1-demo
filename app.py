from flask import Flask, render_template, request

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            result = add_numbers(num1, num2)
        except:
            result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)