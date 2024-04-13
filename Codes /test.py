import time
import traceback

from DES_Encryption import main as des_main
from DES3_Encryption import main as triple_des_main
from AES_Encryption import main as aes_main
from RSA_Encryption import main as rsa_main

def main():
    try:
        start_time = time.time()

        # DES encryption
        des_main()

        # Record DES encryption time
        des_encryption_time = int((time.time() - start_time) * 10**9)
        print("DES time ",des_encryption_time, "nanoseconds")

        # Triple DES encryption
        triple_des_main()

        # Record Triple DES encryption time
        triple_des_encryption_time = int((time.time() - start_time) * 10**9)
        print("DES3 time ",triple_des_encryption_time, "nanoseconds")

        # AES encryption
        aes_main()

        # Record AES encryption time
        aes_encryption_time = int((time.time() - start_time) * 10**9)
        print("AES time ",aes_encryption_time, "nanoseconds")

        # RSA encryption
        rsa_main()

        # Record RSA encryption time
        rsa_encryption_time = int((time.time() - start_time) * 10**9)
        print("RSA time ",rsa_encryption_time, "nanoseconds")

        # Write results to output.txt
        with open("DES_Encryption_time.txt", "w") as f:
            f.write("Time taken for DES encryption: " + str(des_encryption_time) + " nanoseconds\n")

        with open("DES3_Encryption_time.txt", "a") as f:  
            f.write("Time taken for Triple DES encryption: " + str(triple_des_encryption_time) + " nanoseconds\n")

        with open("AES_Encryption_time.txt", "a") as f:
            f.write("Time taken for AES encryption: " + str(aes_encryption_time) + " nanoseconds\n")

        with open("RSA_Encryption_time.txt", "a") as f:
            f.write("Time taken for RSA encryption: " + str(rsa_encryption_time) + " nanoseconds\n")

    except Exception as e:
        # Log the error traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
