from flask import *

app = Flask(__name__)
username = 'Guest'


@app.route('/')
def index():
    return render_template('index.html', username=username)

@app.route('/calculator', methods=["GET", "POST"])
def calculator():

    answer =  0
    
    if request.method == "POST":
      x = float(request.form.get('x'))
      y = float(request.form.get('y'))
      op = request.form.get('operation')
      if op == '+':
         answer = x + y
      elif op == "-":
         answer = x - y
        
        
        
    return render_template('calc.html', answer=answer)

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