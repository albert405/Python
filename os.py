import os, datetime

target='C:\\Users\\albcy\\PycharmProjects\\untitled3\\testowy'

test = os.listdir(target)

today=datetime.datetime.now()

for root, dirs, files in os.walk(target):
    for file in files:
        if file.endswith('pdf'):
            print(os.path.join(root, file),datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(root, file))))


print(today)
"""
for i in test:
    if i.endswith('.txt'):
        if i.startswith('dupa'):
            print(i)


print(test)"""

#os.path.getctime(targe)