from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple username/password pair for testing
VALID_USER = "admin"
VALID_PASS = "password123"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == VALID_USER and password == VALID_PASS:
            return "Login successful"
        else:
            return "Invalid credentials"
    return render_template_string('''
        <form method="post">
            Username: <input name="username">
            Password: <input name="password" type="password">
            <input type="submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
