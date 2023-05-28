import os

from flask import Flask

import config
from blueprint.clientOrders import bp as orders_client_bp
from blueprint.clientAddress import bp as address_client_bp
from blueprint.clientShoppingcart import bp as shoppingcart_client_bp
from blueprint.admin import bp as admin_bp
from blueprint.client import bp as client_bp
from blueprint.scanFlower import bp as scanflower_bp
from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  #为了讲解用随机数

app.register_blueprint(orders_client_bp)
app.register_blueprint(address_client_bp)
app.register_blueprint(shoppingcart_client_bp)
app.register_blueprint(client_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(scanflower_bp)
app.config.from_object(config)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
