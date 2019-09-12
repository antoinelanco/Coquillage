#! /usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return "Welcome"

if __name__ == '__main__':
	app.run("192.168.1.43")
