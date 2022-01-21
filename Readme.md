# Security Project

## Description
Through our application made for INSAT students, create an accout using your email (@insat.ucar.tn) and get access to a 
list of functionalities including encrypting / decrypting messages, as well as encoding and decoding strings to base64 
and also having a secure ChatRoom for it's users

## Requirements:
To have the application up and running into your machine you need the following: 
* python 3 Interpreter with the following libraries :
  * RSA
  * mysql-connector
  * hashlib
  * cryptography
  * json
  * email / smtplib
  * bcrypt
* mysql database

## Functionalities
* Authentication: In both cases of loging in or creating a new account an email with a verification code is sent to the email provided
* Rsa, AES and DES encryption : Note that the output of these functions gets stored in a file named 'output.txt' found in the root directory of the project
* To decrypt a message using RSA, AES or DES you need to provide a path to file encrypted in that session by the corresponding algorithm
* for ElGamal algorithm, the message encrypted is a list of the encrypted chars one by one
* To decrypt a message using ElGamal algo you need to have already encrypted one message before and you need to provide each char encrypted one at a time
