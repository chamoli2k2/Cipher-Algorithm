from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import time

def generate_rsa_keypair(key_size):
    return RSA.generate(key_size)

def encrypt_rsa(data, keypair):
    rsa_cipher = PKCS1_OAEP.new(keypair.publickey())
    encrypted_data = b""
    # Encrypt data in chunks to avoid exceeding maximum length
    chunk_size = 128  # Limit chunk size to fit RSA key size
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        encrypted_chunk = rsa_cipher.encrypt(chunk)
        encrypted_data += encrypted_chunk
    return encrypted_data

    
def main():
    # Read content from target.txt file
    with open("Targettext.txt", "rb") as file:
        data = file.read()

    # RSA encryption
    rsa_key_size = 2048  # RSA key size in bits
    rsa_keypair = generate_rsa_keypair(rsa_key_size)
    rsa_encrypted_data = encrypt_rsa(data, rsa_keypair)
    with open("target_rsa_encrypted.txt", "wb") as file:
        file.write(rsa_encrypted_data)

if __name__ == "__main__":
    main()
