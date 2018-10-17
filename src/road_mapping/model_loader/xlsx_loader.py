from openpyxl import load_workbook
import os

SUPPORTED_FILE_EXTENSIONS = ['.xlsx', '.xlsm']

def loadModel(filePath):
    if os.path.isfile(filePath) != True:
        raise Exception('model_loader: not a file')
    
    filename, ext = os.path.splitext(filePath)
    if any(ext in s for s in SUPPORTED_FILE_EXTENSIONS) != True:
        raise Exception('model_loader: file extension {}'.format(ext))
    
    # should parse the input path to make sure it is valid (e.g. exists, has the right extension, of the right format)
    workbook = load_workbook(filePath)