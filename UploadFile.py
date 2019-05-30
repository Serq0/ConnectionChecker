import ftplib
import Settings

def Upload():
    session = ftplib.FTP(Settings.FTPaddress,Settings.username,Settings.password)
    file = open(Settings.filename,'rb')                  # file to send
    session.storbinary('STOR '+Settings.filename, file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
    print('File '+Settings.filename+' uploaded')

