import openpyxl
import os 
import sys

def getFileList(folderPath):
    if not os.path.exists(folderPath):
        print(f"Folder not found: {folderPath}")
        return []
    if not os.path.isdir(folderPath):
        print(f"Not a folder: {folderPath}")
        return []
    
    fileList = []
    for file in os.listdir(folderPath):
        if verifyFile(os.path.join(folderPath, file)) == 0:
            fileList.append(os.path.join(folderPath, file))
        else:
            print(f"Skipping invalid file: {file}, in folder: {folderPath}, error code: {verifyFile(os.path.join(folderPath, file))}")
    return fileList

def verifyFile(filelist):
    for file in filelist:
        if not os.path.exists(file):
            print(f"File not found: {file}")
            return 1
        if not file.endswith(('.png', '.jpg', '.jpeg')):
            print(f"Invalid image file: {file}")
            return 2
    else :
        return 0

def initWorkbook(destinationFile):
    if os.path.exists(destinationFile):
        print(f"File already exists: {destinationFile}")
        return None
    workbook = openpyxl.Workbook()
    return workbook

def closeWorkbook(workbook,destinationFile):
    if workbook is None:
        print("No workbook to save.")
        return
    try:
        workbook.save(destinationFile)
        print(f"Workbook saved successfully: {destinationFile}")
    except Exception as e:
        print(f"Error saving workbook: {e}")

def copyImage(imagePath,destinationFile,workbook,sheetName,rowNum,colNum):
    pass
