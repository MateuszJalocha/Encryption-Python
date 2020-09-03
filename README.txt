# Encryption in Python

The project was carried out in the first year of studies as part of the Python classes, where the aim was to create an application with basic UI.  It included encryption and decryption, and it is the ciphers used that count: ** Substitution cipher **, ** Rail fence cipher **, ** Two square cipher **

## Operating instructions

To run the application you need the Python compiler (PyCharm, Spyder).
When the program starts, we have three ciphers: the message can be both encrypted and deciphered. 
In order to do so, you need to enter the selected message in the field and then click on the button with the selected cipher. 
For the substition and rail fence cipher you have to choose a key. In case of the substition cipher, it indicates,
if the letters are to move (range: 0 to 25). As for the hurdle code, it indicates the number of lines,
to which letters will be assigned. 
Decrypted/encrypted content will appear above the message entry field. 
In order to finish working with the program, select the "Finish" window.

## Characteristics of ciphers

- ** Substitution cipher ** - It works by converting each character of the Latin alphabet into a character appearing x positions after it, with no case-sensitivity when transforming the meaning
- ** Rail fence cipher ** - It works by reordered the order of letters,
based on the simplified shape of the wooden fence (the fence has as many levels as its key). The letters are read in lines from top to bottom.
- ** Two square cipher ** - It divides the plain text of a message into character groups, and then assigns one of the other predefined character groups (two-letter) to each of these groups. In our case, we used predefined keys that allow us to create two squares with letters used to encrypt character groups.

## Contributors

- ** Mateusz Jałocha ** (mat.jalocha@gmail.com)

- ** Jakub Ignatik ** (https://github.com/JakubIg)

## Sources

- ** Substitution cipher ** (szyfruj1, deszyfruj2): http://www.crypto-it.net/pl/proste/szyfr-cezara.html?tab=2

- ** Rail fence cipher ** (szyfruj3): http://www.crypto-it.net/pl/proste/szyfr-plotkowy.html?tab=2

- ** Two square cipher ** (szyfruj2): http://www.crypto-it.net/pl/proste/dwukwadratowy.html?tab=2

