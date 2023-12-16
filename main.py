from flask import *
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(16)



@app.route("/")
def index():
    return render_template("index.html", username=username)


@app.route('/stock')
def stock():
    if not session.get("stocks"):
        session["stocks"] = []
    return render_template('add_stock.html')

@app.route('/calculator', methods=["GET", "POST"])
    my_stock = {
       "name": request.form.get("name"),
       "symbol": request.form.get("symbol"),
       "price": request.form.get("price"),
    }
    session["stocks"].append(my_stock)

    return render_template("add_stock.html", stocks=session.get("stocks"))
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