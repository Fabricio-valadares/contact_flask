from flask import Blueprint, jsonify, request
from .services.logic_services import query_create, create_item_data_base

app_home = Blueprint("app_home", __name__, url_prefix="/home/app")

@app_home.route("/")
def home():
    first_query = """
    SELECT * FROM contacts;
    """
    res = query_create(first_query)

    return jsonify(res), 200

@app_home.route("/create", methods=["POST"])
def create():

    data_body = request.get_json()

    create_items = f"""
        INSERT INTO contacts(name, email, description)
        VALUES ('{data_body.get("name")}', '{data_body.get("email")}', '{data_body.get("description")}');
    """

    res = create_item_data_base(create_items, data_body)

    return jsonify(res), 201
