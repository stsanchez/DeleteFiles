import shutil
import os
import shutil
import datetime
from datetime import datetime
import time
from datetime import date
from datetime import datetime, date, time, timedelta

"""This program deletes some files that other processes generate massively.
I only need to keep the ones of the current day. That's why I compare the date and if they are earlier they are deleted.
That saves me from having to do it manually every day, freeing up disk space and improving performance on the server."""

#Set the date format
date_format = '%d/%m/%Y'

#Get the current date for compare
current_date = date.today()
date_time = current_date.strftime(date_format)

#Set the path where are the files to compare and delete
path = 'D:\\PATH\\...'

#Get a list with all files
files = os.listdir(path)

#Create a log file for check the information
log = open("log.txt", "a")

#Iterate the list for start to compare
for element in files:

    #Join the path with the name of element
    file = path + os.sep + element

    #Get the stat of the file
    estado = os.stat(file)

    #Get the last modified date
    modified_date = datetime.fromtimestamp(estado.st_mtime)   

    #Set the file las modified date format
    modified_date = modified_date.strftime(date_format)

    #Compare if is equal or not equal to delete.
    if modified_date == date_time:
        #Write a line in the log with the file information
        log.write (file+ '-->' + modified_date + '||' + date_time + ':Equal'+  os.linesep)

    elif modified_date != date_time:
        #Write a line in the log with the file information
        log.write (file+ '-->' + modified_date + '||' + date_time + ': not equal. Deleted'+  os.linesep)
        #Delete the file because is not equal
        shutil.rmtree(file)

#write a lines to separate the times that the program works 
log.write('-'*15)

log.close()

