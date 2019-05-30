from urllib.request import urlopen


def CheckConnection(address):
    try:
        urlopen(address, timeout=1)
        return True
    except: 
        return False
