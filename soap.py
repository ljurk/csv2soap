'''
refrence: https://python-zeep.readthedocs.io/en/master/api.html

prerequisites:
	pip install zeep
'''
#imports
import sys
import csv
import logging as log
from zeep import Client

#variables
list = []
verbose = 0
wsdl = 'SOME_WSDL_URL'
csvSet = 0
pathToCsv = ''
silent = 0
logFile = './soappy.log'

#init log
log.basicConfig(filename=logFile, level=log.INFO, format='%(asctime)s : %(levelname)s: %(message)s' )
log.getLogger().addHandler(log.StreamHandler())

#parse arguments
if len(sys.argv) != 1:
    for i in range(len(sys.argv)):
        if sys.argv[i] == 'verbose':
            verbose = i
        elif sys.argv[i] == 'silent':
            silent = 1
        elif '.csv' in sys.argv[i]: 
            pathToCsv = sys.argv[i]
            csvSet = 1

log.info('start')

#only continue if csv is given
if not csvSet:
    log.error('no csv given')
else:
    #initialize SOAP Client
    soapClient = Client(wsdl)

    log.info('initializing SOAP-Client')
    log.info('WSDL: ' + wsdl)
    log.info('CSV: ' + pathToCsv)
    
    #read csv
    with open(pathToCsv,'r') as f:
        log.info('start reading csv-file')
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            list.append(row)

    log.info('reading complete')
    log.info('number of lines: ' + str(len(list)))
    log.info('start sending')
    for data in list:
        log.info(data['userName'] + ':' + data['matricNumber'])

        #ask before every dataset if silent isn't set
        if not silent:
            cont = raw_input('send? y/n: ')
        else:
            cont = 'y'

        if cont.upper() == 'Y':
            try:
                result = soapClient.service.func(data)
                if result.status == 'error':
                    log.error(result.message)
                elif result.status == 'success':
                    log.info(result.message)
                else:
                    log.error(result.status + result.message)
            except:
                 log.error('An exception occurred')
log.info('end')
