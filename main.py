from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        return redirect(url_for('index'))

    return render_template('login.html')