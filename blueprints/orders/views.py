from flask import Blueprint, jsonify, json, request
from models import Order
from database import Database

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route("/orders", methods=['GET', 'POST'])
def page_orders():
    if request.method == 'GET':
        result = []
        orders = Order.query.all()
        for item in orders:
            result.append(item.create_dict())
        return jsonify(result)

    elif request.method == 'POST':
        order_info = json.loads(request.data)
        Database().add_order(order_info)
        return ""


@orders_blueprint.route("/orders/<pk>", methods=['GET', 'PUT', 'DELETE'])
def page_orders_by_id(pk):
    if request.method == 'GET':
        order = Order.query.get(pk)
        result = Order.create_dict(order)
        return jsonify(result)

    elif request.method == 'PUT':
        order_info = json.loads(request.data)
        Database().update_order(order_info, pk)
        return ""

    elif request.method == 'DELETE':
        Database().delete_order(pk)
        return ""
