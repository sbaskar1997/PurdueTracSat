import csv
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



fieldnames = ["binary"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

for i in range(len(messageArrayBinary)):
    messageArrayBinary[i] = str(messageArrayBinary[i]).zfill(7)
    print(messageArrayBinary[i])
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
            
    
