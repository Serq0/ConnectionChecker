from datetime import datetime
import Settings


def connectString(mainstring, stringtoadd):
    return mainstring+'<br>'+str(stringtoadd)

def SaveIndex():
    try:
        attempts = ReadFile(Settings.attemptfile)
    except:
        print("File "+Settings.attemptfile+" not found, creating new one")
        SaveFile(Settings.attemptfile,1)
        attempts = ReadFile(Settings.attemptfile)

    try:
        failsR = ReadFile(Settings.failfile)
    except:
        print("File "+Settings.failfile+" not found, creating new one")
        SaveFile(Settings.failfile,0)
        failsR = ReadFile(Settings.failfile)
    
    fails = 'Failed: '+str(failsR)
    toSave = 'Attempts: '+str(attempts)
    toSave = connectString(fails,toSave)
    
    
    percentage = 100 - (int(failsR)/int(attempts))*100
    toSave = connectString(toSave,'Working Time: '+str(percentage)+'%')
    
    lastUpload = 'Last Uploaded: '+str(datetime.now())
    toSave = connectString(toSave,lastUpload)

    try:
        error_file = open(Settings.errorfile, 'r')
    except:
        print("File "+Settings.errorfile+" not found, creating new one")
        SaveFile(Settings.errorfile)
        error_file = open(Settings.errorfile, 'r')
    text_file = open(Settings.filename, "w")
    text_file.write(toSave+'<br><br><br>'+error_file.read())
    text_file.close()

def SaveFile(file,value=''):
    f = open(file, "w")
    f.write(str(value))
    f.close()

def ReadFile(file):
    f = open(file)
    for line in f:
        return line

def AddError():
    try:
        with open(Settings.errorfile, 'a+') as file:
            file.write(str(datetime.now())+'    <br>\n')
            file.close()
    except:
        print("File "+Settings.errorfile+" not found, creating new one")
        SaveFile(Settings.errorfile)
        AddError()



