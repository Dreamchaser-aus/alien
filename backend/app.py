from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 假数据（以后可以换数据库）
products = [
    {"id": 1, "name": "Space Jacket", "price": 99},
    {"id": 2, "name": "Galaxy Hoodie", "price": 120}
]

# ===== 前台API =====
@app.route("/api/products")
def get_products():
    return jsonify(products)

# ===== 后台页面 =====
@app.route("/admin")
def admin():
    return render_template("admin.html", products=products)

# ===== 添加产品 =====
@app.route("/api/add", methods=["POST"])
def add_product():
    data = request.json
    products.append({
        "id": len(products)+1,
        "name": data["name"],
        "price": data["price"]
    })
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
