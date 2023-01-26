# Password Generator and Encrypter

This project is a Python script that generates a random password of a specified length, and then encrypts it using the AES algorithm in CTR mode. The resulting ciphertext and key are written to a file, and the original password can be retrieved by decrypting the ciphertext using the key.

## Getting Started

To use this script, you will need to have Python and the `cryptography` library installed on your machine. You can install `cryptography` using `pip`, the Python package manager:

``` pip install cryptography ```


Once you have Python and `cryptography` installed, you can run the script by navigating to the directory containing the script and running the following command:

``` python password generator.py ```


The script will prompt you to enter the desired length for the password. The password will be generated and encrypted, and the resulting ciphertext and key will be written to the file `password.txt`.

To decrypt the password, you can use the `decrypt_password` function defined in the script. This function takes the encrypted password and key as arguments, and returns the original, decrypted password.

## Customizing the Script

You can customize the script by modifying the `generate_password` function to specify the desired character set for the password, and by modifying the `encrypt_password` function to specify the desired encryption algorithm and mode.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. I welcome all contributions, including bug fixes, new features, and improvements to the code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Author: Cyph3rRyx
