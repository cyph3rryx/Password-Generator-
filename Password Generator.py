import secrets
import string
import base64
from cryptography.fernet import Fernet

def generate_password(length):
  # Generate a random password
  alphabet = string.ascii_letters + string.digits
  password = ''.join(secrets.choice(alphabet) for i in range(length))
  return password

def encrypt_password(password):
  # Generate a random key
  key = Fernet.generate_key()

  # Encrypt the password using the key
  f = Fernet(key)
  encrypted_password = f.encrypt(password.encode())

  # Return the encrypted password and the key
  return encrypted_password, key

def write_to_file(encrypted_password, key):
  # Write the encrypted password and key to a file
  with open('password.txt', 'w') as f:
    f.write(base64.encodebytes(encrypted_password).decode())
    f.write('\n')
    f.write(base64.encodebytes(key).decode())

def decrypt_password(encrypted_password, key):
  f = Fernet(key)
  decrypted_password = f.decrypt(encrypted_password).decode()
  return decrypted_password

if __name__ == '__main__':
  password = generate_password(30)
  encrypted_password, key = encrypt_password(password)
  write_to_file(encrypted_password, key)
