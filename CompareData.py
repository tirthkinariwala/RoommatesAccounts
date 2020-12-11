import pandas as pd

toSplitPath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\MasterSample.xlsx"
toSplitData = pd.read_excel(toSplitPath, sheet_name='ToSplitSample', index_col=0)

masterBDPath = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\MasterBD.xlsx"
masterBDData = pd.read_excel(masterBDPath)

# toSplitData.columns.name = 'UI'
toSplitData['Amount'] = -1 * toSplitData['Amount']

x = toSplitData.copy()
y = masterBDData.copy()

modified1 = x.reset_index()
modified2 = y.reset_index()

inner_join = pd.merge(modified1,
                      modified2,
                      on = 'Unique',
                      how = 'inner')

for i in range(len(inner_join)):
    masterBDData['UID'].iloc[inner_join['index_y'].iloc[i]] = inner_join['index_x'].iloc[i]
    masterBDData['UID'].iloc[inner_join['index_y'].iloc[i] - 1] = inner_join['index_x'].iloc[i]
    toSplitData['Empty'].iloc[inner_join['index_y'].iloc[i] - 1] = "x"

masterBDData.to_excel('CompareData.xlsx', index=False)

print(toSplitData.to_string())
