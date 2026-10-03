from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# Homepage route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"}), 200

# GET /products - Returns all products or filters by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category") if request.args else None
    
    if category:
        filtered = [
            p for p in products 
            if str(p.get("category", "")).lower() == str(category).lower()
        ]
        return jsonify(filtered), 200
        
    return jsonify(products), 200

# GET /products/<id> - Returns product by ID or 404
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p.get("id") == product_id), None)
    
    if not product:
        return jsonify({"error": f"Product with ID {product_id} not found"}), 404
        
    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)