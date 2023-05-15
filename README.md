<b>Password Cracker using OpenSSL and Python</b>

This is a Python script for cracking a password-protected private key file using the openssl command-line tool. The script reads a wordlist of potential passwords from a text file (rockyou.txt in this case), and tries each password until the correct one is found. The password is used to decrypt the private key, and the resulting key file is saved as out.key.

<b>Requirements</b>

This script requires Python 3.x and the openssl command-line tool to be installed on the system.

<b>Usage</b>

To run the script, simply execute the following command from the terminal:

python3 ./password_cracker.py
The script will try each password in the wordlist until the correct one is found, and print the key to the console. If no correct password is found, the script will print "Finished Wordlist".

![image](https://github.com/PatrickAcheson/private-RSA-key-bruteforce/assets/90014630/68caa96e-d391-409c-90df-c2d3451eed93)

<b>Customization</b>

You can customize the script by changing the following variables:

wordlist_file: the path to the wordlist file to be used for password cracking. By default, it is set to rockyou.txt.
private_key_file: the path to the private key file that you want to crack. By default, it is set to private.pem.
pass_prefix: the prefix for the openssl command to decrypt the private key. By default, it is set to "openssl rsa -in {file} -out out.key -passin pass:".

<b>License</b>

This script is licensed under the MIT License. Please see the LICENSE file for more information.
