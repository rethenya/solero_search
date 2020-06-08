from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
app.config["DEBUG"] = True
client = MongoClient(
    'mongodb+srv://rethenya:rethenya@solerasearch-w3fp2.mongodb.net/solero?retryWrites=true&w=majority')  # mongodb atlas connection
db = client.get_database('solero')  # database connectivity
records = db.KeyWord  # connecting collection called KeyWord


@app.route('/', methods=['GET'])  # method to get all the records from the collection in the database
def search():
    output = []
    for q in records.find():
        output.append(
            {'medName': q['medName'], 'saltName': q['saltName'], 'manufacturer': q['manufacturer'], 'mrp': q['mrp'],
             'best price': q['bestPrice'], 'pack size': q['packSize']})

    return jsonify({'result': output})  # returns all the records as result for the request


@app.route('/<medname>', methods=['GET'])  # method to get the specified the record from the collection in the
# database by providing the medName
def find(medname):
    q = records.find_one({"medName": medname})
    output = {'medName': q['medName'], 'saltname': q['saltName'], 'manufacturer': q['manufacturer'], 'mrp': q['mrp'],
              'best price': q['bestPrice'], 'pack size': q['packSize']}
    return jsonify({'result': output})  # returns the specified record as result for the request


@app.route('/', methods=['POST'])  # method to post a new record to the collection in the database
def add_data():
    medname = request.json['medName']
    saltname = request.json['saltName']
    manufacturer = request.json['manufacturer']
    mrp = request.json['mrp']
    bestprice = request.json['bestPrice']
    packsize = request.json['packSize']

    record_id = records.insert(
        {'medName': medname, 'saltName': saltname, 'manufacturer': manufacturer, 'mrp': mrp, 'bestPrice': bestprice,
         'packSize': packsize})

    new_recrd = records.find_one({'_id': record_id})

    output = {'medName': new_recrd['medName']}
    return jsonify({'result': output})   # returns the  medName of the record inserted into the mongodb atlas


app.run()
