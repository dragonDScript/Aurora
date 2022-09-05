from os import path

def file(fileName):
    return path.join(__file__, "..", fileName)

def icon(iconName):
    return path.join(__file__, "..", "icons", iconName)