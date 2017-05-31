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

with open('C:\\Users\\Ben\\Documents\\test_practice\\practice_doc.py\\text_test.txt', 'r+') as test:
    test.write('this is a test')
    test.write('\n')
    test.write('\n')
    test.write('this is a test 2')

t = open('C:\\Users\\Ben\\Documents\\test_practice\\practice_doc.py\\text_test.txt', 'r+')
t_read = t.read()
t.close()

print(t_read)


