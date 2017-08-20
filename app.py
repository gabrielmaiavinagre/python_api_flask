#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:05:47 2017

@author: gabrielvinagre
"""

#EXECUTE THE CODE ON TERMINAL TYPE: python3.6 app.py

from flask import Flask, jsonify, request
#class start with capital case - Flask and package with lowercase flask

app = Flask(__name__)

stores = [{
                'name':'My Wonderful Store',
                'items':[{'name': 'My Item', 'price': 15.99 }]
                }]

#@app.route('/')#http://www.google.com/

#def home():
#    return "Hello, world!"

#POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
            'name': request_data['name'],
            'items':[]
            }
    stores.append(new_store)
    
#    retorno para o brownser saber que foi criado a store
    return jsonify(new_store)

#GET /store<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:500/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    
    for store in stores:
        if request_data['name'] == name:
            new_item = {'name': request_data['name'],'price':request_data['price']}   
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})
    


app.run(port=5000)






