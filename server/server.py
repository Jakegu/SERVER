from flask import Flask, request, abort
from config import me, db
import json

app = Flask("server")






@app.get("/")
def home():
    return "Hello World"

@app.get("/about")
def about_me():
    return "Jake Gulotta"

@app.get("/api/about")
def about_data():
    return json.dumps(me)


@app.get("/api/about/developer")
def developer_name():
    full_name = me["name"] + " " + me["last_name"]
    return json.dumps(full_name)

@app.get("/api/categories")
def categories():
    all_cats = []
    cursor = db.products.find({})
    for product in cursor:
        category = product["category"]
        if category not in all_cats:
            all_cats.append(category)

    return json.dumps(all_cats)


def fix_id(record):
    record["_id"] = str(record["_id"])
    return record


@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find()
    for product in cursor:
        products.append(fix_id(product))
    return json.dumps(products)


@app.post("/api/products")
def save_product():
    product = request.get_json()

    db.products.insert_one(product)

    print(product)

    return json.dumps(product)



@app.get("/api/products/category/<cat>")
def get_by_category(cat):
    products = []
    cursor = db.products.find({"category": cat })
    for product in cursor:
        products.append(fix_id(product))
    return json.dumps(products)


@app.get("/api/reports/total")
def get_prices_sum():
    
    cursor = db.products.find({})
    sum = 0
    for product in cursor:
        price = product["price"]
        sum += price
    return json.dumps(sum)


app.run(debug=True)