import pandas as pd
import os

# mydict = pd.read_csv('/Users/saurav/Desktop/MasterBD.csv', header=None, index_col=0, squeeze=True).to_dict()

billDividerFilePath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\MasterBD.xlsx"
MasterFilePath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\MasterSample.xlsx"
MasterFile = pd.read_excel(MasterFilePath, sheet_name='ToSplitSample', index_col=0)
billDivider = pd.read_excel(billDividerFilePath)
billDividerPersonalEntries = billDivider[billDivider["Cash Out"] == "No"]
billDividerCashoutEntries = billDivider[billDivider["Cash Out"] == "Yes"]
cols = ['Tirth', 'Saurav', 'Sachin', 'Meet' ]
df = pd.DataFrame(columns=['index', 'Date', 'Location', 'Amount', 'Category'])

print(MasterFile.to_string())
BeenSplit = MasterFile.loc[MasterFile['Empty'] == 'x']

with pd.ExcelWriter('TEST.xlsx') as writer:
    for col in cols:
        df['Date'] = billDividerPersonalEntries['Date']
        df['Location'] = billDividerPersonalEntries['Location']
        df['Category'] = billDividerPersonalEntries['Category']
        df['Amount'] = -1*billDividerPersonalEntries[col]
        df['index'] = billDividerPersonalEntries['UID']
        df.to_excel(writer, sheet_name=col, index=False)
    BeenSplit.to_excel(writer, sheet_name='Been Split')

billDivider = pd.read_excel(billDividerFilePath)
print(billDividerCashoutEntries["Paid By"])

# with pd.ExcelWriter('TEST2.xlsx') as writer2:
#     for col in cols:
#         for x in range(1,(len(billDividerCashoutEntries)+1))