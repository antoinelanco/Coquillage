#! /usr/bin/env python3

from flask import Flask, json, request, Response

app = Flask(__name__)

@app.route('/')
def api_root():
    bc = open("bc",'r')
    print(bc)

    dico = {"Bonjour":"Moi"}
    js = json.dumps(dico)
    resp = Response(js, status=200 , mimetype='application/json')
    return resp

if __name__ == '__main__':
	app.run("192.168.1.43")
