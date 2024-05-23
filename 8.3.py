import hashlib
import Crypto.PublicKey.RSA as RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Cryptodome.PublicKey import ElGamal
from Cryptodome import Random

def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_sign(message, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)
    return signature

def rsa_verify(message, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Przykład użycia
private_key, public_key = generate_rsa_keypair()
message = b"essa"
signature = rsa_sign(message, private_key)
print("Podpis cyfrowy:", signature)
print("Weryfikacja podpisu:", rsa_verify(message, signature, public_key))



def generate_elgamal_keypair():
    key = ElGamal.generate(2048, Random.new().read)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def elgamal_sign(message, private_key):
    key = ElGamal.import_key(private_key)
    h = hashlib.sha256(message).digest()
    k = Random.new().read(key.size())
    signature = key.sign(h, k)
    return signature

def elgamal_verify(message, signature, public_key):
    key = ElGamal.import_key(public_key)
    h = hashlib.sha256(message).digest()
    try:
        key.verify(h, signature)
        return True
    except ValueError:
        return False

# Przykład użycia
private_key, public_key = generate_elgamal_keypair()
message = b"Hello, world!"
signature = elgamal_sign(message, private_key)
print("Podpis cyfrowy:", signature)
print("Weryfikacja podpisu:", elgamal_verify(message, signature, public_key))
