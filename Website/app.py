from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    creditNo = request.form['creditNO']
    expo = request.form['expo']
    cvv = request.form['cvv']
    
    # Print data to the server console
    print(f"Received data: Name={name}, Email={email}, Card Number={creditNo}")
    print(f"Expiration Date={expo}, CVV={cvv}")
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)