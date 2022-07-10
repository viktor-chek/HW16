from models import User, Offer, Order, db
from all_json import USERS, ORDERS, OFFERS


class Database:
    def load_users_in_base(self):
        """Загружает всех users в базу"""
        for item in USERS:
            user = User(
                id=item["id"],
                first_name=item["first_name"],
                last_name=item["last_name"],
                age=item["age"],
                email=item["email"],
                role=item["role"],
                phone=item["phone"]
            )
            db.session.add(user)
            db.session.commit()


    def load_orders_all(self):
        """Загружает все orders в базу"""
        for item in ORDERS:
            order = Order(
                id=item["id"],
                name=item["name"],
                description=item["description"],
                start_date=item["start_date"],
                end_date=item["end_date"],
                address=item["address"],
                price=item["price"],
                customer_id=item["customer_id"],
                executor_id=item["executor_id"]
            )
            db.session.add(order)
            db.session.commit()


    def load_all_offers(self):
        """Загружает все offers в базу"""
        for item in OFFERS:
            offer = Offer(
                id=item["id"],
                order_id=item["order_id"],
                executor_id=item["executor_id"]
            )
            db.session.add(offer)
            db.session.commit()


    def add_user(self, user_info):
        """Добавляет пользователя в таблицу user"""
        user = User(
            first_name=user_info["first_name"],
            last_name=user_info["last_name"],
            age=user_info["age"],
            email=user_info["email"],
            role=user_info["role"],
            phone=user_info["phone"]
        )
        db.session.add(user)
        db.session.commit()


    def update_user(self, user_info, pk):
        """Обновляет пользователя в таблице user"""
        upd = User.query.get(pk)

        upd.first_name = user_info['first_name']
        upd.last_name = user_info['last_name']
        upd.age = user_info['age']
        upd.email = user_info['email']
        upd.role = user_info['role']
        upd.phone = user_info['phone']

        db.session.add(upd)
        db.session.commit()


    def delete_user(self, pk):
        """Удаляет пользователя в таблице user"""
        dlt_user = User.query.get(pk)

        db.session.delete(dlt_user)
        db.session.commit()


    def add_order(self, order_info):
        """Добавляет заказ в таблицу order"""
        order = Order(
            name=order_info["name"],
            description=order_info["description"],
            start_date=order_info["start_date"],
            end_date=order_info["end_date"],
            address=order_info["address"],
            price=order_info["price"],
            customer_id=order_info["customer_id"],
            executor_id=order_info["executor_id"]
        )
        db.session.add(order)
        db.session.commit()


    def update_order(self, order_info, pk):
        """Обновляет заказ в таблице order"""
        upd_order = Order.query.get(pk)

        upd_order.name = order_info["name"]
        upd_order.description = order_info["description"]
        upd_order.start_date = order_info["start_date"]
        upd_order.end_date = order_info["end_date"]
        upd_order.address = order_info["address"]
        upd_order.price = order_info["price"]
        upd_order.customer_id = order_info["customer_id"]
        upd_order.executor_id = order_info["executor_id"]

        db.session.add(upd_order)
        db.session.commit()


    def delete_order(self, pk):
        """Удаляет заказ в таблице order"""
        delete_element = Order.query.get(pk)

        db.session.delete(delete_element)
        db.session.commit()


    def add_offer(self, offer_info):
        """Добавляет предложение в таблицу offer"""
        offer = Offer(
            order_id=offer_info["order_id"],
            executor_id=offer_info["executor_id"]
        )

        db.session.add(offer)
        db.session.commit()


    def update_offer(self,offer_info, pk):
        """Обновляет предложение в таблице offer"""
        upd_offer = Offer.query.get(pk)

        upd_offer.order_id = offer_info['order_id']
        upd_offer.executor_id = offer_info['executor_id']

        db.session.add(upd_offer)
        db.session.commit()


    def delete_offer(self, pk):
        """Удаляет предложение в таблице offer"""
        dlt_offer = Offer.query.get(pk)

        db.session.delete(dlt_offer)
        db.session.commit()
