import numpy as np
import matplotlib.pyplot as plt

# Function to read encrypted data from a text file
def read_encrypted_data(file_path):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    # Decode encrypted data if necessary
    # encrypted_data = decode_base64(encrypted_data)
    return encrypted_data

# Function to generate and save images from encrypted data
def visualize_encrypted_data(encrypted_data, algo_name):
    # Convert encrypted data to numpy array (replace with your conversion logic)
    encrypted_array = np.random.rand(10, 10)  # Example conversion
    # Generate and save image from the encrypted array
    plt.imshow(encrypted_array, cmap='jet')
    plt.title(f"{algo_name} Encrypted Data")
    plt.axis('off')
    plt.savefig(f"{algo_name}_encrypted_data.png")
    plt.close()

# File paths for encrypted data
des_encrypted_file = "target_des_encrypted.txt"
triple_des_encrypted_file = "target_triple_des_encrypted.txt"
aes_encrypted_file = "target_aes_encrypted.txt"
rsa_encrypted_file = "target_rsa_encrypted.txt"

# Read encrypted data from text files
des_encrypted_data = read_encrypted_data(des_encrypted_file)
triple_des_encrypted_data = read_encrypted_data(triple_des_encrypted_file)
aes_encrypted_data = read_encrypted_data(aes_encrypted_file)
rsa_encrypted_data = read_encrypted_data(rsa_encrypted_file)

# Visualize encrypted data for each algorithm
visualize_encrypted_data(des_encrypted_data, "DES")
visualize_encrypted_data(triple_des_encrypted_data, "Triple DES")
visualize_encrypted_data(aes_encrypted_data, "AES")
visualize_encrypted_data(rsa_encrypted_data, "RSA")
