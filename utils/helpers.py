import binascii
import bcrypt
import jwt
from django.conf import settings
def requete(sql):
    import psycopg2
    conn = psycopg2.connect(
        host= "localhost",
        database = "auto-reserv",
        user="mahmoud",
        password="passer"
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return cursor
    cursor.close()
    conn.close()
    
    
def en_hexadecimal(ch):
    return binascii.hexlify(ch).decode('utf-8')


def en_binaire(ch):
    return binascii.unhexlify(ch)


def crypter_mot_de_passe(ch):
    return en_hexadecimal(bcrypt.hashpw(ch.encode('utf-8'), bcrypt.gensalt()))

def verifier_mot_de_passe(entered_password, hexadecimal_password):
    if bcrypt.checkpw(entered_password.encode('utf-8'), en_binaire(hexadecimal_password)):
        return True
    else:
        return False
    
def decoder_jwt(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.InvalidTokenError:
        print('Invalid token')
        
def coder_jwt(payload):
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
