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

# with open('C:\\Users\\Ben\\Documents\\test_practice\\practice_doc.py\\text_test.txt', 'r+') as test:
#     test.write('this is a test')
#     test.write('\n')
#     test.write('\n')
#     test.write('this is a test 2')
#
# t = open('C:\\Users\\Ben\\Documents\\test_practice\\practice_doc.py\\text_test.txt', 'r+')
# t_read = t.read()
# t.close()
#
# print(t_read)


class Person(object):

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def about_person(self):
        return "my name is %s and  I am %s and I am %s inches tall" % (self.name, str(self.age), str(self.height))


class Job(Person):
    def __init__(self, name, age, height, job_title):
        super(Job, self).__init__(name, age, height)
        self.job_title = job_title

    def about_person(self):
        super(Job, self).about_person()
        return "my name is %s and  I am %s and I am %s inches tall and I am a %s" \
               % (self.name, str(self.age), str(self.height), self.job_title)

bob = Person('Bob', 45, 70)
print(bob.about_person())

jon = Job('Jon', 32, 71, 'data analyst')
print(jon.about_person())


