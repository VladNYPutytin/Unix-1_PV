from flask import Flask, request, jsonify,render_template
import random
import string

app = Flask(__name__)

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, symbols=True):
    charset = ""
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if symbols:
        charset += string.punctuation
    return ''.join(random.choice(charset) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['GET'])
def generate_password_route():
    length = int(request.args.get('length', 12))
    uppercase = request.args.get('uppercase', 'true').lower() == 'true'
    lowercase = request.args.get('lowercase', 'true').lower() == 'true'
    numbers = request.args.get('numbers', 'true').lower() == 'true'
    symbols = request.args.get('symbols', 'true').lower() == 'true'
    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)