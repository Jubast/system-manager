#!/usr/bin/python

from flask import Flask, request
app = Flask(__name__)
from handler import handle_switch

@app.route("/switch/linux")
def linux():
    type = request.args.get('type')
    if not type:
        return 400

    handle_switch("linux", type)

    return type, 200

@app.route("/switch/windows")
def windows():
    type = request.args.get('type')
    if not type:
        return 400

    handle_switch("windows", type)

    return type, 200

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port= 45323)
