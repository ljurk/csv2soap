'''
refrence: https://python-zeep.readthedocs.io/en/master/api.html

prerequisites:
	pip install zeep
	pip install colorama
'''
import sys
import csv
from colorama import Fore, Style, init
from zeep import Client

#colors
cRed = Style.BRIGHT + Fore.RED
cDefault = Style.RESET_ALL
cGreen = Style.BRIGHT + Fore.GREEN
cYellow = Style.BRIGHT + Fore.YELLOW

#variables
list = []
verbose = 0
wsdl = 'SOME_WSDL_URL'
csvSet = 0
pathToCsv = ''

#init colorama
init()


if len(sys.argv) != 1:
    for i in range(len(sys.argv)):
        if sys.argv[i] == 'verbose':
            verbose = i
        elif '.csv' in sys.argv[i]: 
            pathToCsv = sys.argv[i]
            csvSet = 1

#only continue if csv is given
if not csvSet:
    print(cRed + "ERROR: no csv given")
else:
    #initialize SOAP Client
    soapClient = Client(wsdl)
    print(cYellow + "initializing SOAP-Client")
    print(cYellow + "WSDL: " + wsdl)
    print(cYellow + "CSV: " + pathToCsv)
    
    print('')
    
    #read csv
    with open(pathToCsv,'r') as f:
        print("start reading file")
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            list.append(row)
    
    print(cGreen + "reading complete")
    print(cDefault + "Number of lines:" + str(len(list)))
    
    print('')
    
    #print csv data
    if verbose:
        for i in list:
            print(i)
    print('')
    
    #send data
    print(cRed + "start sending")
    for data in list:
        print('')
        print(cYellow + data['userName'])
        try:
            print(cGreen + "ok")
            result = soapClient.service.func(data)
            if result.status == 'error':
                print(cRed + result.status.upper() + "    " + result.message)
            elif result.status == 'success':
                print(cGreen + result.status.upper() + "    " + result.message)
            else:
                print(cRed + "unknown status:" + result.status)
        except:
            print(cRed + "An exception occurred")
    print('')
print("END")
