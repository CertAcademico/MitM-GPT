from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

USER = {"username": "admin", "password": "1234"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == USER["username"] and password == USER["password"]:
        resp = make_response(redirect('/chat'))
        resp.set_cookie("session_id", "fake-session-id")  # No Secure, HttpOnly, SameSite
        return resp
    return "Login failed", 401

@app.route('/chat')
def chat():
    session = request.cookies.get("session_id")
    if not session:
        return redirect('/')
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form.get('message')
    return f"Usuario dijo: {message}<br>Respuesta de ChatGPT local: Hola, soy ChatGPT local"

if __name__ == '__main__':
    app.run(ssl_context=('certs/cert.pem', 'certs/key.pem'), debug=True)
