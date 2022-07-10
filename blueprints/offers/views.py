from flask import Blueprint, jsonify, request, json
from models import Offer
from database import Database

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route("/offers", methods=['GET', 'POST'])
def page_offers():
    if request.method == 'GET':
        result = []
        offers = Offer.query.all()
        for item in offers:
            result.append(item.create_dict())
        return jsonify(result)

    elif request.method == 'POST':
        offer_info = json.loads(request.data)
        Database().add_offer(offer_info)
        return ""


@offers_blueprint.route("/offers/<pk>", methods=['GET', 'PUT', 'DELETE'])
def page_offers_by_id(pk):
    if request.method == 'GET':
        order = Offer.query.get(pk)
        result = Offer.create_dict(order)
        return jsonify(result)

    elif request.method == 'PUT':
        offer_info = json.loads(request.data)
        Database().update_offer(offer_info, pk)
        return ""

    elif request.method == 'DELETE':
        Database().delete_offer(pk)
        return ""
