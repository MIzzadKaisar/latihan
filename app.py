import os
import datetime
from flask import Flask, render_template,request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
client = MongoClient(os.getenv("MONGODB_URI"))
app.db = client.Latihan



@app.route("/", methods=["GET","POST"])
def index():
    if request.method ==  "GET":
        myquery = {"alamat":"Jalan Persatuan"}
        
        app.db.latihan.delete_one(myquery)
        
        return render_template("index.html") 
        
        
        
        
        #Untuk mengupdate
        # myquery = { "alamat": "Jalan Bunga"}
        # newvalues = {"$set": {"alamat": "Jalan Mawar" } } 
        # app.db.latihan.update_one(myquery, newvalues)
        
        # for x in app.db.latihan.find():
        #     print(x)
        
        
        
        
        
        #untuk mensortir
        # hasil = app.db.latihan.find().sort("nama", -1)
        
        # for x in hasil:
        #     print(x)
        
        #Untuk mencari
    #     pencarian ={"NIS" : "123"}
    #     hasil = app.db.latihan.find(pencarian)
    
    #     hasil_pencarian = []
        
    #     for x in hasil:
    #         hasil_pencarian.append(x)
    #         print(x)
        
    #untuk memasukkan data
    #     nama = request.form.get("nama")
    #     kelas = request.form.get("kelas")
        
    #     app.db.latihan.insert_one({"nama": nama, "kelas":kelas})

    
    # mydict ={"name": "Izzad", "address": "Sinjai"}
    # mydict2 ={"NIS": "123", "asal sekolah": "SDN"}
    
    # app.db.latihan.insert_one(mydict2)
    
    

