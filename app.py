from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# Homepage route that returns a welcome message
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"}), 200

# GET /products - Returns all products or filters by category query parameter
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    
    if category:
        filtered_products = [
            p for p in products 
            if p["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products), 200
        
    return jsonify(products), 200

# GET /products/<id> - Returns a specific product by ID or 404 if not found
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    
    if not product:
        return jsonify({"error": f"Product with ID {product_id} not found"}), 404
        
    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)