from flask import Flask, request, jsonify
from models.product import Product

app = Flask(__name__)

products = []

id_control = 1

@app.route("/products", methods=['POST'])
def create_product():
    global id_control
    data = request.get_json()

    if products:
        for p in products:
            if data.get("name") == p.name:
                return jsonify({"message": f"product {p.name} already exists"}), 400

            new_product = Product(id_control, data.get("name"), data.get("quantity", 0), data.get("price"), data.get("description", ""), data.get("currency", "$"))

            products.append(new_product)

            id_control += 1
            return jsonify({"message": f"product '{new_product.name}' created"}), 200

    new_product = Product(id_control, data.get("name"), data.get("quantity", 0), data.get("price"), data.get("description", ""), data.get("currency", "$"))

    products.append(new_product)

    id_control += 1

    return jsonify({"message": f"product '{new_product.name}' created"}), 200


@app.route("/products", methods=['GET'])
def get_products():
    return jsonify([p.to_dict() for p in products]), 200


@app.route("/products/<int:id_product>", methods=['GET'])
def get_product(id_product):
    if products:
        for p in products:
            if p.id == id_product:
                return jsonify(p.to_dict()), 200
        
        return jsonify({"message": f"product '{id_product}' not found"}), 404

    return jsonify({"message": "No products available"}), 400


@app.route("/products/<int:id_product>", methods=['PUT'])
def update_product(id_product):
    if products:
        data = request.get_json()
        
        for p in products:
            if p.id == id_product:
                p.name, p.quantity, p.price, p.description, p.currency = data.get("name"), data.get("quantity"), data.get("price"), data.get("description"), data.get("currency")
                return jsonify({"message": f"product {p.id} updated"}), 200

        return jsonify({"message": f"product '{id_product}' not found"}), 404
    
    return jsonify({"message": "No products available"}), 400




if __name__ == "__main__":
    app.run(debug=True)