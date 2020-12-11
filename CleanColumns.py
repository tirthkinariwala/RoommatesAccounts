
import pandas as pd
import glob

folder = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\Raw to Clean\\Credit"
output_foler = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\Raw to Clean\\Credit\\Final"
all_files = glob.glob(folder + "/*.csv")
output_files = glob.glob(output_foler + "/*.csv")

#for filename in all_files:
for i in range(len(all_files)):
    filename = all_files[i]
    output_filename = output_files[i]
    df = pd.read_csv(filename, index_col=0, usecols = [0,1,2,3])
    df.columns = df.columns.str.replace(r"(^Unnamed: [0123456789])", "No")
    df.fillna("No", inplace=True)
    df.to_csv(output_filename)
    print(output_filename)

folder = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\Raw to Clean\\Debit"
output_folder = "\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\Raw to Clean\\Debit\\Final"
all_files = glob.glob(folder + "/*.csv")
output_files = glob.glob(output_folder + "/*.csv")

#for filename in all_files:
for i in range(len(all_files)):
    filename = all_files[i]
    output_filename = output_files[i]
    df = pd.read_csv(filename, index_col=0, usecols = [0,1,2,3,4,5])
    df.columns = df.columns.str.replace(r"(^Unnamed: [0123456789])", "No")
    # A = df.loc[df["column"].isnull()]
    # print(A)
    df.fillna("No", inplace=True)
    df.to_csv(output_filename)
    print(output_filename)