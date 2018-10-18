import openpyxl 
import os
import logging
import road_mapping.model as model

SUPPORTED_FILE_EXTENSIONS = ['.xlsx', '.xlsm']
WORKSHEET_NAME = 'to_import'

class xlsx_loader:
    def loadModel(filePath, ):
        if os.path.isfile(filePath) != True:
            raise Exception('model_loader: not a file')
        
        _, ext = os.path.splitext(filePath)
        if any(ext in s for s in SUPPORTED_FILE_EXTENSIONS) != True:
            raise Exception('model_loader: file extension {}'.format(ext))
        
        capabilities = []
        features = []

        ### ASSUMPTIONS ###
        # assume the data is formatted in a worksheet named 'to_import'
        # assume table has a header row, with the appropriate column titles
        # assume the minimun data for a row is an id
        # assume the table is positioned at the top left of the worksheet (cell A1)
        # assume the data is arranged as contiguous rows beneath the header

        # if the worksheet is not found, an exception is thrown
        workbook = openpyxl.load_workbook(filePath)
        sheet = workbook[WORKSHEET_NAME]
        
        idColumn = -1
        nameColumn = -1
        summaryColumn = -1
        descriptionColumn = -1

        # find the relevant columns
        for col in range(1, sheet.max_column):
            cell = sheet.cell(row=1, column=col)
            if cell.data_type == openpyxl.cell.cell.Cell.TYPE_STRING:
                cellValue = cell.value.lower()

                if cellValue == 'id':
                    idColumn = col
                elif cellValue == 'name':
                    nameColumn = col
                elif cellValue == 'summary':
                    summaryColumn = col
                elif cellValue == 'description':
                    descriptionColumn = col

            # should probably add another exit condition here

        if idColumn == -1:
            raise Exception('model_loader: Id column not found')

        for row in range(2, sheet.max_row):
            cell = sheet.cell(row=row, column=idColumn)
            capability = model.Capability(cell.value)

            if nameColumn != -1:
                cell = sheet.cell(row=row, column=nameColumn)
                capability.name = cell.value
            
            if summaryColumn != -1:
                cell = sheet.cell(row=row, column=summaryColumn)
                capability.summary = cell.value

            if descriptionColumn != -1:
                cell = sheet.cell(row=row, column=descriptionColumn)
                capability.description = cell.value

            capabilities.append(capability)


        return capabilities, features