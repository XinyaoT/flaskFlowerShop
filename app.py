import os

from flask import Flask
from blueprint.clientOrders import bp as orders_client_bp
from blueprint.clientAddress import bp as address_client_bp
from blueprint.clientShoppingcart import bp as shoppingcart_client_bp
from blueprint.client import bp as client_bp
from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  #为了讲解用随机数

app.register_blueprint(orders_client_bp)
app.register_blueprint(address_client_bp)
app.register_blueprint(shoppingcart_client_bp)
app.register_blueprint(client_bp)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
