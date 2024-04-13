from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import time

def generate_des_key():
    des_block_size = 64  # DES block size in bits
    return get_random_bytes(des_block_size // 8)

def encrypt_des(data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data, DES.block_size)
    return cipher.encrypt(padded_data)

def main():
    # Read content from target.txt file
    with open("Targettext.txt", "rb") as file:
        data = file.read()

    # DES encryption
    des_key = generate_des_key()
    des_encrypted_data = encrypt_des(data, des_key)
    with open("target_des_encrypted.txt", "wb") as file:
        file.write(des_encrypted_data)

if __name__ == "__main__":
    main()
