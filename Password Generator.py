import secrets
import string
import base64
from cryptography.fernet import Fernet

def generate_password(length):
    # Generate a random password
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def encrypt_password(password, key):
    # Encrypt the password using the key
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())

    # Return the encrypted password
    return encrypted_password

def write_to_file(encrypted_password, key):
    # Write the encrypted password and key to a file
    with open('password.txt', 'wb') as f:
        f.write(base64.b64encode(encrypted_password))
        f.write(b'\n')
        f.write(base64.b64encode(key))

def decrypt_password(key):
    # Read the encrypted password and key from the file
    with open('password.txt', 'rb') as f:
        encrypted_password = base64.b64decode(f.readline())
        key = base64.b64decode(f.readline())

    # Decrypt the password using the key
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()

    # Return the decrypted password
    return decrypted_password

if __name__ == '__main__':
    # Generate a random password
    password = generate_password(30)

    # Generate a random key
    key = Fernet.generate_key()

    # Encrypt the password using the key
    encrypted_password = encrypt_password(password, key)

    # Write the encrypted password and key to a file
    write_to_file(encrypted_password, key)

    # Decrypt the password from the file
    decrypted_password = decrypt_password(key)
    print(decrypted_password)
