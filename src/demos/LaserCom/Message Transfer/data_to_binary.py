import csv
<<<<<<< HEAD
import random
import time
=======
>>>>>>> 9ff79ca9fc3c375193fc7f16abb9c6146ff40174
import sys

if len(sys.argv) < 2:
    print("Usage: python data_to_binary.py [MESSAGE]")
    sys.exit(1)


messageArray = sys.argv[1:]
message = ' '.join(messageArray)
print("Message: " + message)
messageStringBinary = ' '.join(format(ord(x), 'b') for x in message)
messageArrayBinary = messageStringBinary.split(" ")
print(messageArrayBinary)
<<<<<<< HEAD
=======



>>>>>>> 9ff79ca9fc3c375193fc7f16abb9c6146ff40174
fieldnames = ["binary"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

for i in range(len(messageArrayBinary)):
<<<<<<< HEAD
=======
    messageArrayBinary[i] = str(messageArrayBinary[i]).zfill(7)
    print(messageArrayBinary[i])
>>>>>>> 9ff79ca9fc3c375193fc7f16abb9c6146ff40174
    for j in range(len(list(messageArrayBinary[i]))):
        with open('data.csv', 'a') as csv_file:
            if j == len(list(messageArrayBinary[i])) - 1 and i != len(messageArrayBinary) - 1:
                digit = list(messageArrayBinary[i])[j]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                info = {
                    "binary": digit,
                }
                csv_writer.writerow(info)
                digit = '*'
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                info = {
                    "binary": digit,
                }
                csv_writer.writerow(info)
            else:
                digit = list(messageArrayBinary[i])[j]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                info = {
                    "binary": digit,
                }
                csv_writer.writerow(info)
            
    
