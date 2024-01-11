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



if __name__ == "__main__":
    app.run(debug=True)