from operator import truediv
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
from Crypto.PublicKey import RSA
from Crypto import Random
import base64
import json

from Crypto.PublicKey import RSA
from Crypto import Random
import base64
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

app = Flask(__name__)
api = Api(app)


def generate_rsakeys():
    print("hello")
    privatekey = RSA.generate(2048)
    publickey = privatekey.public_key()

    write_keys(privatekey, publickey)

    return privatekey, publickey


def write_keys(privatekey, publickey):
    privateKeyFile = open('private.pem', 'wb')
    privateKeyFile.write(privatekey.export_key('PEM'))

    pulicKeyFile = open('public.pem', 'wb')
    pulicKeyFile.write(publickey.export_key('PEM'))


def encrypt(message):
    encrypted_json = {}
    f = open('public.pem', 'r')
    key = RSA.import_key(f.read())
    encryptor = PKCS1_OAEP.new(key)
    for i in message.keys():
        value = str(message.get(i))
        print(value)
        encrypted_json[i] = str(encryptor.encrypt(bytes(value, 'utf-8')))
    return encrypted_json


# def decrypt(rsa_privatekey, encrypted_text):
#     decryptor = PKCS1_OAEP.new(rsa_privatekey)
#     decrypted = decryptor.decrypt(encrypted_text)
#     print(decrypted)
#     return decrypted

def decrypt(message):
    encrypted_json = {}
    f = open('private.pem', 'r')
    key = RSA.import_key(f.read())
    encryptor = PKCS1_OAEP.new(key)
    for i in message.keys():
        value = str(message.get(i))
        try:
            encrypted_json[i] = eval(encryptor.decrypt(eval(value)))
        except Exception as e:
            encrypted_json[i] = str(encryptor.decrypt(eval(value)), "UTF-8")
    return encrypted_json


def sign(message):
    f = open('private.pem', 'r')
    key = RSA.import_key(f.read())

    hash = SHA256.new(message.strip().encode("utf8"))
    signature = pkcs1_15.new(key).sign(hash)
    result = {}
    result["signature"] = str(signature)
    result["data"] = message
    return jsonify(result)


def verify(message, sign):
    f = open('public.pem', 'r')
    key = RSA.import_key(f.read())

    print(type(key))
    print(type(message))

    hash = SHA256.new(message.encode("utf8"))
    try:
        pkcs1_15.new(key).verify(hash, eval(sign))
        print("The signature is valid.")
        result = {}
        
        result["success"] = True
        return jsonify(result)
    except Exception as e:
        print(str(e))
        print("The signature is not valid.")
        return ("ded")


@app.route("/api2/sign", methods=['POST'])
def sign_rest():
    data = request.data.decode()
    print(data)
    signature = sign(data)
    return signature


@app.route("/api2/verify", methods=['POST'])
def verify_rest():
    data = request.json
    print(data)
    verify_signature = verify(data["data"], data["signature"])
    return verify_signature


@app.route("/api2/encrypt", methods=['POST'])
def encrypt_rest():
    data = request.json
    encrypted_value = encrypt(data)

    return jsonify(encrypted_value)


@app.route("/api2/decrypt", methods=['POST'])
def decrypt_rest():
    data = request.json
    decrypt_value = decrypt(data)
    
    return jsonify(decrypt_value)

# @app.before_first_request
# def before_first_request():
#     generate_rsakeys()

if __name__ == '__main__':
    # rsa_privatekey, rsa_publickey = generate_rsakeys()
    print("hello")
    app.run(debug=True)
