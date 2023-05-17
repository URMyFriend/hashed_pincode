import csv
from hashlib import sha256

hash_dict = dict()

for i in range(0,10000):
    i = str(i)
    hash_dict[sha256(i.encode("utf-8")).hexdigest()] = i.zfill(4)


a = input("whats your hashed pass? ")

answer = hash_dict.get(a)

while a != 1:
    
    answer = hash_dict.get(a)
    print("the pass is ",answer)
    a = input("whats your hashed pass? ")


