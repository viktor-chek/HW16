from flask import Flask
from database import Database, db
from blueprints.users.views import users_blueprint
from blueprints.orders.views import orders_blueprint        # Импорт представлений
from blueprints.offers.views import offers_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False                     # Необходимые настройки приложения
app.config['JSON_SORT_KEYS'] = False


app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)        # Регистрация представлений
app.register_blueprint(offers_blueprint)


db.init_app(app)  # Пуш приложения в контекст. На самом деле не понимаю как он работает. Буду признателен за пояснение)
app.app_context().push()


db.create_all()     # Создание таблиц

Database().load_users_in_base()
Database().load_orders_all()        # Заполнение таблиц
Database().load_all_offers()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
