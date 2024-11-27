#izveidot Python programmu name.py kas prasa
#ievadīt vārdu un ieraksta to failā name.txt

vards = input('Ievadi vārdu: ')

with open('name.txt','a',encoding='utf-8') as f:
    f.write(vards + '\n')