import os
import pandas as pd
spisok_add=[]
spisok_dirs=[]
spisok_files=[]
spisok_rashir=[]
dates={}
count=0
def generation():
    for address, dirs, files in os.walk(r'C:\Users\User\Downloads\testtask'):
        try:
            spisok_add.append(address)
            spisok_files.append(files)
            spisok_dirs.append(dirs)
        except NameError:
            print('list couldnt find')
        for file in files:
            full=os.path.join(file)
        if '.' in full:
            full=full.split('.')
            full=full[-1]
        else:
            full="-"
        spisok_rashir.append(full)
    dates={'folders':spisok_dirs, 'files':spisok_files, 'extension':spisok_rashir }
    return dates

            
a=generation()
print(a)
try:
    df = pd.DataFrame(data=a)
    df.to_excel("res.xlsx", index=False)
    print("Dictionary converted into excel...")
except Exception:
    print("error")



