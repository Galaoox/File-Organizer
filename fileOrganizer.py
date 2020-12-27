import os
import shutil

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


def moveFile(nameFile, directory):
    shutil.move(path + nameFile, path +directory + '/' + nameFile)

def validateTypeFile(nameFile):
    findedType = False
    for typeFile in typeFiles.keys():
        
        if nameFile.endswith(tuple(typeFiles[typeFile])):
            moveFile(nameFile, typeFile)
            findedType = True
            break
    if findedType == False:
        moveFile(nameFile, 'OTHERS')

createDirectories()

nameFiles = os.listdir(path)




for nameFile in nameFiles:
    if os.path.isdir(path + nameFile) == False:
        validateTypeFile(nameFile)

textTest = '    Hola esto es un nombre de  archivbo 123213213213213 -SAD.png'









