import Settings
import SaveFile
import time
import CheckConnection
import UploadFile


def Pause(refreshRate):
    time.sleep(refreshRate)

def Init():
    print("Starting...")
    try:
        file = open(Settings.filename)
        file.close()
    except:
        SaveFile.SaveFile(Settings.filename)
    try:
        file = open(Settings.errorfile)
        file.close()
    except:
        SaveFile.SaveFile(Settings.errorfile)
    try:
        file = open(Settings.attemptfile)
        file.close()
    except:
        SaveFile.SaveFile(Settings.attemptfile,0)
    try:
        file = open(Settings.failfile)
        file.close()
    except:
        SaveFile.SaveFile(Settings.failfile,0)

def Main():
    attempts = int(SaveFile.ReadFile(Settings.attemptfile)) #wczytaj ilosc prob
    fails = int(SaveFile.ReadFile(Settings.failfile)) #wczytaj ilosc niepowodzen
    uploadIndex = False
    print("Starting attempts: "+str(attempts),"Starting fails: "+str(fails))
    while(True):
        if(uploadIndex == False):
            Pause(Settings.refreshRate) #przerwa
        else:
            Pause(Settings.refreshRate-2)
        attempts += 1 #zacznij probe kolejna
        GoogleStatus = CheckConnection.CheckConnection(Settings.GOOGLE_ADDRESS)
        if(GoogleStatus != True): #sprawdz polaczenie z google
            StackOverflowStatus = CheckConnection.CheckConnection(Settings.STACKOVERFLOW_ADDRESS)
            if(StackOverflowStatus != True): #sprawdz polaczenie z stovfl
                fails += 1 #obie strony nie dzialaja
                SaveFile.AddError() #dodaj blad
                SaveFile.SaveIndex() #odswiez index.html
                uploadIndex = True
                SaveFile.SaveFile(Settings.failfile,fails) #aktualizuj ilosc niepowodzen
                print("Connection error "+str(fails))
        SaveFile.SaveFile(Settings.attemptfile,attempts) #aktualizuj ilosc prob

        if(attempts%100 == 1): #co 100 prob aktualizuj statystyki
            SaveFile.SaveIndex() #odswiez index.html
            uploadIndex = True

        if(uploadIndex):
            try:
                UploadFile.Upload()
                uploadIndex = False
            except:
                pass


Init()
Main()
