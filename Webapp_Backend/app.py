import certifi
from flask import Flask,jsonify, request
from flask_cors import CORS, cross_origin
from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://sirilux:FZjpQCRkkWd6hntm@cluster0.6jtbi56.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client["shop"]
collection = db["products"]
p_in_DB = collection.find()
products=[
{"id":0,"name":"Notebook Acer Swift","price":45900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0147295/A0147295_s.jpg"},
{"id":1,"name":"Notebook Asus Vivo","price":19900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146010/A0146010_s.jpg"},
{"id":2,"name":"Notebook Lenovo Ideapad","price":32900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149009/A0149009_s.jpg"},
{"id":3,"name":"Notebook MSI Prestige","price":54900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149954/A0149954_s.jpg"},
{"id":4,"name":"Notebook DELL XPS","price":99900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146335/A0146335_s.jpg"},
{"id":5,"name":"Notebook HP Envy","price":46900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0145712/A0145712_s.jpg"}
];
for p in p_in_DB:
    products.append(p)
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products",methods=["GET"])
def get_all_products():
    return jsonify(products),200

@app.route("/products",methods=["POST"])
@cross_origin()
def add_product():
    data = request.get_json(products)
    count = 0
    pp = 0
    if products:
        print("it empty!!!!")
    for _ in products :
        count = _   
        pp = pp+1
    # print(oak)
    ttt = 0
    if pp != 0 :
        ttt = count["_id"]+1
    new_product = {
        "_id":ttt,
        "name":data["name"],
        "price":data["price"],
    }
    products.append(new_product)
    collection.insert_one({
        "_id":ttt,
        "name":data["name"],
        "price":data["price"]
    })
    return jsonify(products),200

@app.route("/products/<int:id>",methods=["DELETE"])
def detele_product(id):
    for o in products:
        if(o["_id"] == id):
            products.remove(o)
            collection.delete_one({"_id":id})
            return jsonify(products),200
    return jsonify(products),404

@app.route("/products/<int:id>",methods=["PUT"])
def update_product(id):
    data = request.get_json(products)
    up_p = {
        "_id":{id},
        "name":data["name"],
        "price":data["price"],
    }
    for o in products:
        if(o["_id"] == id):
            o.update(data)
            collection.update_many(
                {"_id":o["_id"]},
                {"$set":{   "name" : data["name"],
                            "price" : data["price"]
                        }
                }
            )
            return jsonify(products),200
    return jsonify("Not found!!"),200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)