import os
import glob
from collections import Counter
import hashlib
input_path = input("Enter path: ")
extentions = []
largest_folders = []
same_files_path = []
for a in glob.glob(os.path.join(input_path,"**\\*.*"),recursive=True):
    extentions.append(a.split(".")[1])
counted = Counter(extentions)
print(counted.most_common(5))
print()
for b in os.listdir(input_path):
    sum_Folder = 0
    if os.path.isdir(os.path.join(input_path,b)):
        for c in glob.glob(os.path.join(os.path.join(input_path,b),"**\\*.*"),recursive=True):
            sum_Folder += os.path.getsize(c)
        largest_folders.append((os.path.join(input_path,b),sum_Folder))
print(sorted(largest_folders, key=lambda x: x[1]))
print()
def same_file(file):
    sha256 = hashlib.sha256()
    with open(file ,"rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()
files = [h for h in glob.glob(os.path.join(input_path,"**\\*.*"),recursive=True)]
for i in files:
    list_same_files = [i]
    for t in files:
        if i != t and same_file(i) == same_file(t):
            list_same_files.append(t)
            files.remove(t)
    same_files_path.append((list_same_files,len(list_same_files)))
for qq in sorted(same_files_path, key=lambda w: w[1]*-1)[0:5]:
    print(qq[0],qq[1])
    print()
for qq in sorted(os.walk(input_path), key=lambda wwe:len(wwe[0].split("\\"))*-1):
    print(qq[0],qq[-1])