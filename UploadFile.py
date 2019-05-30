import ftplib
import Settings

FTPaddress = Settings.FTPaddress
username = Settings.username
password = Settings.password
filename = Settings.filename

def Upload():
    session = ftplib.FTP(FTPaddress,username,password)
    file = open(filename,'rb')                  # file to send
    session.storbinary('STOR '+filename, file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
    print('File '+filename+' uploaded')

