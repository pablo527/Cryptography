from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from Crypto.Hash import SHA256
from flask import Flask, jsonify, request

app = Flask(__name__)

def generate_keys():
    keyPair = RSA.generate(1024)
    with open('keys/publickey.pem',mode='wb') as file:
        file.write(keyPair.publickey().exportKey())
        file.close()
    with open('keys/privatekey.pem',mode='wb') as file:
        file.write(keyPair.exportKey())
        file.close()

def encrypt(message):
    message = base64.decodebytes(message.encode('utf8'))
    key = RSA.importKey(open('keys/publickey.pem', 'rb').read())
    cifrado = PKCS1_OAEP.new(key)
    mensaje_cifrado = cifrado.encrypt(message,hashAlgo=SHA256)
    return mensaje_cifrado

def decrypt_cryptogram(message):
    message = base64.decodebytes(message.encode('utf8'))
    with open('keys/privatekey.pem', 'r') as f:
        privatekey = f.read()
        f.close()
    key = RSA.importKey(privatekey)
    encryption = PKCS1_OAEP.new(key,hashAlgo=SHA256)    
    mesj_decrypt = encryption.decrypt(message)    
    return mesj_decrypt.decode('utf8')
   
 
@app.route('/decrypt', methods=['POST'])
def decrypt():
    request_data = request.get_json()
    cryptogram = request_data['cryptogram'] 
    decrypted = decrypt_cryptogram(cryptogram)
 
    return jsonify({'message_decrypted':decrypted})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


