import os
import sys

def generate_key(length):
    return os.urandom(length)

def encrypt_file(input_file, otp_file, encrypted_file):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    key = generate_key(len(plaintext))
    
    with open(otp_file, 'wb') as f:
        f.write(key)

    ciphertext = bytearray(len(plaintext))
    for i in range(len(plaintext)):
        ciphertext[i] = plaintext[i] ^ key[i]

    with open(encrypted_file, 'wb') as f:
        f.write(ciphertext)

def decrypt_file(encrypted_file, otp_file, decrypted_file):
    with open(otp_file, 'rb') as f:
        key = f.read()

    with open(encrypted_file, 'rb') as f:
        ciphertext = f.read()

    plaintext = bytearray(len(ciphertext))
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[i] ^ key[i]

    with open(decrypted_file, 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <encrypt/decrypt> <input_file> <otp_file/encrypted_file> <output_file>")
        sys.exit(1)

    action = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if action == "encrypt":
        otp_file = sys.argv[4]
        encrypt_file(input_file, otp_file, output_file)
        print(f"File encrypted and saved as {output_file}")
        print(f"OTP key saved as {otp_file}")
    elif action == "decrypt":
        otp_file = input_file
        encrypted_file = sys.argv[4]
        decrypt_file(encrypted_file, otp_file, output_file)
        print(f"File decrypted and saved as {output_file}")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")