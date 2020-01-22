#python script which removes files older than $age
import os, datetime

target='APPL\OFM\SOA\PRD\K8S\K0017_UCM'
age=10
age_minus=-50 #we reduce age numberfrom 60
exclude=['ERRORS','INCOMING_LIST_ARCHIVE','MANUAL','PROCESSED','REPORTS','REPORTS-TEMP-NEW_SERVER','TEMP','UCM_RETRY']

today=datetime.datetime.now()
for root, dirs, files in os.walk(target): #this part goes through folders recursively
    dirs[:] = [d for d in dirs if d not in exclude]
    for file in files:
        if file.endswith('camelExclusiveReadLock'):#scirpt is checking if file is ending with provided extension
            file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(root, file))) #assigns time when file was created
            difference_time=(today.minute-file_cre_date.minute)
            if difference_time > age or difference_time >age_minus:
                os.remove(os.path.join(root, file))