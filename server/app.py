
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from Crypto.Hash import SHA256

def generate_keys():
    keyPair = RSA.generate(1024)
    with open('keys/publickey.pem',mode='wb') as file:
        file.write(keyPair.publickey().exportKey())
        file.close()
    with open('keys/privatekey.pem',mode='wb') as file:
        file.write(keyPair.exportKey())
        file.close()

def encrypt():
    mesnaje = b'777'
    key = RSA.importKey(open('keys/publickey.pem', 'rb').read())
    cifrado = PKCS1_OAEP.new(key)
    mensaje_cifrado = cifrado.encrypt(mesnaje)
    return mensaje_cifrado
   
def decrypt():
    with open('text.txt', 'r') as f:
        crypto_msg = f.read()
    crypto_msg = base64.decodebytes(crypto_msg.encode('utf8'))

    with open('keys/privatekey.pem', 'r') as f:
        privatekey = f.read()
        f.close()
    key = RSA.importKey(privatekey)
    crifrado = PKCS1_OAEP.new(key,hashAlgo=SHA256)
    mesj_decrypt = crifrado.decrypt(crypto_msg)
    return mesj_decrypt.decode('utf8')

if __name__ == "__main__":
    #generate_keys()
    #mesj = encrypt()
    print(decrypt())
