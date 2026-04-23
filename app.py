from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    attendance = float(request.form['attendance'])

    # Simple fake logic (you can improve later with ML)
    if hours >= 5 and attendance >= 75:
        result = "Excellent performance ⭐"
    elif hours >= 3:
        result = "Average performance 🙂"
    else:
        result = "Needs improvement ⚠️"

    return render_template('form.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)