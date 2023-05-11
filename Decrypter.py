with open('password.txt', 'r') as f:
  encrypted_password = base64.decodebytes(f.readline().strip().encode())
  key = base64.decodebytes(f.readline().strip().encode())
  decrypted_password = decrypt_password(encrypted_password, key)
  print(decrypted_password)
