#! /usr/bin/env python3

from flask import Flask, json, request, Response

app = Flask(__name__)

@app.route('/')
def api_root():
    bc = open("bc",'r')
    js = bc.read()
    resp = Response(js, status=200 , mimetype='application/json')
    return resp

if __name__ == '__main__':
	app.run("192.168.1.43",debug=True)
