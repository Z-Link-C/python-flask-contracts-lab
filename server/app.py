#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route("/customer/<customer_name>")
def customer_data(customer_name):
    if customer_name.lower() not in customers:
        return make_response("",404)
    return make_response("",204)
@app.route("/contract/<id>")
def contract_data(id):
    #works if i change the response.. but wont return properly
    ##contract=[c for c in contracts if str(c["id"])==str(id)] 
    contract=next((i["contract_information"] for i in contracts if str(i["id"])==str(id)),None) 
    if contract is None:
        return make_response("",404)
    else: 

         #if i add [contract_information] it errors out
        return make_response(contract,200) 
    ## contract[0] on its own returns the info and id..
    ## contract[0].encode() errors..
    ## contract on its own returns the tuple
    
    #contract={contracts["id"]: contracts for contracts in contracts}
    #doesnt work
    #if id in contract:
    #    response=b''.join(str(contract["contract_information"]))
    #    return make_response(response,200)
    #else:
    #    return make_response("",404)

