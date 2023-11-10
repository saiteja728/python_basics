import os
try:
    os.mkdir("g:\Mango\apple\kiwi")
    print("Folder Created--Verify")
except FileExistsError:
    print("Folder was already created-it can't create again")
except OSError:
    print("The Hierarchy of Folders unable create:")