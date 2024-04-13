from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import time

def generate_triple_des_key():
    # Choose between 16 bytes (DES-EDE) or 24 bytes (DES-EDE3)
    key_size = 16 if DES3.key_size == 16 else 24
    return get_random_bytes(key_size)

def encrypt_triple_des(data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data, DES3.block_size)
    return cipher.encrypt(padded_data)

def main():
    # Read content from target.txt file
    with open("Targettext.txt", "rb") as file:
        data = file.read()

    # Triple DES encryption
    triple_des_key = generate_triple_des_key() # key size is 16 or 24 bytes 
    triple_des_encrypted_data = encrypt_triple_des(data, triple_des_key)
    with open("target_triple_des_encrypted.txt", "wb") as file:
        file.write(triple_des_encrypted_data)

if __name__ == "__main__":
    main()
