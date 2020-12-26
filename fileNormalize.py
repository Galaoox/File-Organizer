import os

path = os.path.join(os.getcwd(),'../')
typeFiles = {
    'DOCUMENTS': ['.doc', '.docx','.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd'],
    'IMAGES':['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff'],
    'VIDEOS':['.3g2', '.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'],
    'AUDIO': ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg','.wav', '.wma', '.wpl'],
    'OTHERS': []
}

def createDirectory(name, path):
    try:
        pdfsFolderExist = os.path.exists(path + name)
        if pdfsFolderExist == False:
            os.mkdir(path + name)

    except OSError:
        print ("Creation of the directory %s failed" % path)

def createDirectories():
    for directoryName in typeFiles.keys():
        createDirectory(directoryName, path)


createDirectories()

def validateTypeFile(nameFile):
    for typeFile in typeFiles.keys():
        if nameFile.endswith(tuple(typeFiles[typeFile])):
            print(nameFile, typeFile)

nameFiles = os.listdir(path)

def formatName(name: str):
    name = name.replace('-', ' ').upper().split()
    print('godd')
    name[len(name) -1] =name[len(name) -1].lower()
    return '-'.join(name)
    

for nameFile in nameFiles:
    formatName(nameFile)
#     validateTypeFile(nameFile)

textTest = '    Hola esto es un nombre de  archivbo 123213213213213 -SAD.png'





formatName(textTest)




