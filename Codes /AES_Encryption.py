from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import time

def generate_aes_key(key_size):
    return get_random_bytes(key_size // 8)

def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, AES.block_size)
    return cipher.encrypt(padded_data)

def main():
    # Read content from target.txt file
    with open("Targettext.txt", "rb") as file:
        data = file.read()

    # AES encryption
    aes_key_size = 256  # AES key size in bits
    aes_key = generate_aes_key(aes_key_size)
    aes_encrypted_data = encrypt_aes(data, aes_key)
    with open("target_aes_encrypted.txt", "wb") as file:
        file.write(aes_encrypted_data)

if __name__ == "__main__":
    main()
