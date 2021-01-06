import os
import pandas as pd
from datetime import datetime
masterFilePath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\MasterSheet\\Master_Accounts.xlsx"
catrgoriesPath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\Categories.csv"
rawFileFolder =  "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\ProcessedRaw\\"

def fileCombiner(catrgoriesPath, masterFilePath, rawFileFolder):
    mydict = pd.read_csv(catrgoriesPath, header=None,
                         index_col=0, squeeze=True).to_dict()


    masterFile = pd.read_excel(masterFilePath, sheet_name='Master Sheet', index_col=0)
    indexShift = len(masterFile)
    del masterFile
    df = pd.DataFrame()
    df.to_excel("output.xlsx", index=False)
    del df

    entries = os.listdir(rawFileFolder)
    entries = [rawFileFolder + x for x in entries]
    # makes an array of all the files in the folder of interest

    for entry in entries:
        print(entry)
        file = entry
        MasterFile = pd.read_excel("output.xlsx")
        # extension = os.path.splitext(file)[1]
        fileName = os.path.splitext(file)[0]
        fileName = fileName.split('\\')
        fileNameString = fileName[len(fileName) - 1]
        fileNameSplit = fileNameString.split('_')
        cardType = fileNameSplit[0]
        name = fileNameSplit[3]
        openFile = pd.read_csv(file, header=None)
        if cardType == 'Debit' or cardType == 'debit':
            openFile.columns = ['Date', 'Amount', 'Empty', 'Info', 'Location', 'To Split']
        else:
            openFile.columns = ['Date', 'Location', 'Amount', 'To Split']
        openFile['Paid By'] = name
        openFile['Card Type'] = cardType
        MasterFile = [MasterFile, openFile]
        appended_df = pd.concat(MasterFile)
        appended_df['Date'] = pd.to_datetime(appended_df['Date'])
        appended_df.to_excel("output.xlsx", index=False)
        del openFile
        del MasterFile
    del appended_df

    finalMaster = pd.read_excel('output.xlsx')
    finalMaster.index = finalMaster.index + indexShift
    finalToSplit = finalMaster[finalMaster["To Split"] == "Yes"]
    cols = list(set(finalMaster["Paid By"].values))
    print(cols)
    with pd.ExcelWriter('output.xlsx') as writer:
        finalMaster.to_excel(writer, sheet_name='Master Sheet')
        finalToSplit.to_excel(writer, sheet_name='To Split Sheet')
        for people in cols:
            personalSheets = finalMaster[(finalMaster['Paid By'] == people) & (finalMaster['To Split'] == "No")]
            personalSheets.to_excel(writer, sheet_name=people)
    del finalMaster
    del finalToSplit
    del personalSheets

    getSheets = pd.ExcelFile('output.xlsx')
    sheets = getSheets.sheet_names
    with pd.ExcelWriter('output3.xlsx') as writer:
        for sheet in sheets:
            masterFile = pd.read_excel(masterFilePath, sheet_name=sheet, index_col=0)
            openFile = pd.read_excel('output.xlsx', sheet_name=sheet, index_col=0)
            masterFile = [masterFile, openFile]
            appended_df = pd.concat(masterFile)
            appended_df.to_excel(writer, sheet_name=sheet)

fileCombiner(catrgoriesPath, masterFilePath, rawFileFolder)