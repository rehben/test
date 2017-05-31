# import pandas as pd
# import numpy as np
# import csv
# with open('C:\\Users\\Ben\\Documents\\Book1.csv', 'r+') as test:
#     test_csv = csv.writer(test)
#     test_csv.writerow(["a", 24])
#     test_read = csv.reader(test)
#     for row in test_read:
#         print(row)
#     test.close()

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print(A5)
print(A6)
