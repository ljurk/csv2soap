#refrence: https://python-zeep.readthedocs.io/en/master/api.html

import csv

#from zeep import Client

list = []
verbose = 0
wsdl = 'SOME_WSDL_URL'

#initialize
print("initializing SOAP-Client")
print("WSDL: " + wsdl)
#soapClient = Client(wsdl)

#read csv
with open('test.csv','r') as f:
    print("start reading file")
    reader = csv.DictReader(f,delimiter=';')
    for row in reader:
        list.append(row)
    print("reading complete")
    print("lines:" + str(len(list)))
    print()

#print csv data
if verbose:
    for i in list:
        print(i)
print('')
print("start sending")
for data in list:
    print('')
    print(data['userName'])
    try:
        print("ok")
         #result = soapClient.service.func(data)
    except:
        print("An exception occurred")
print("END")


