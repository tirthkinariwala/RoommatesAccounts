import os
import pandas as pd
#
# masterFilePath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\MasterSheet\\Master_Accounts.xlsx"
# masterFile = pd.read_excel(masterFilePath, index_col=0)
# masterFile.to_excel("output.xlsx", index=False)
# del masterFile
#
#
# folder = input('File Path: ')
# #   \\AURORA\Users\Public\Documents\Accounts 2020\Raw\
# entries = os.listdir(folder)
# entries = [folder + x for x in entries]
# # makes an array of all the files in the folder of interest
#
# for entry in entries:
#     print(entry)
#     file = entry
#     MasterFile = pd.read_excel("output.xlsx")
#     # extension = os.path.splitext(file)[1]
#     fileName = os.path.splitext(file)[0]
#     fileName = fileName.split('\\')
#     fileNameString = fileName[len(fileName) - 1]
#     fileNameSplit = fileNameString.split('_')
#     cardType = fileNameSplit[0]
#     name = fileNameSplit[3]
#     openFile = pd.read_csv(file, header=None)
#     if cardType == 'Debit' or cardType == 'debit':
#             openFile.columns = ['Date', 'Amount', 'Empty', 'Info', 'Location', 'To Split']
#     else:
#             openFile.columns = ['Date', 'Location', 'Amount', 'To Split']
#     openFile['Paid By'] = name
#     openFile['Card Type'] = cardType
#     MasterFile = [MasterFile, openFile]
#     appended_df = pd.concat(MasterFile)
#     appended_df.to_excel("output.xlsx", index=False)
#     del openFile
#     del MasterFile
#
#
# finalMaster = pd.read_excel('output.xlsx')
# finalToSplit = finalMaster[finalMaster["To Split"]=="Yes"]
# cols = list(set(finalMaster["Paid By"].values))
# print(cols)
# with pd.ExcelWriter('output2.xlsx') as writer:
#     finalMaster.to_excel(writer, sheet_name='Master Sheet')
#     finalToSplit.to_excel(writer, sheet_name='To Split Sheet')
#     for people in cols:
#         personalSheets = finalMaster[(finalMaster['Paid By'] == people) & (finalMaster['To Split'] == "No")]
#         personalSheets.to_excel(writer, sheet_name=people)
