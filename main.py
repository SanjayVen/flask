from flask import *

app = Flask(__name__)
username = 'Guest'


@app.route('/')
def index():
    return render_template('index.html', username=username)

@app.route('/login', methods=["GET", "POST"])
def login():
    global username

    error = ''
    if request.method == "POST":
        u = request.form.get('username')
        p = request.form.get('password')

        if u == 'myuser' and p == 'mypass':
            username = 'myuser'
            return redirect(url_for('index'))
        
        error = 'invalid login'

    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)