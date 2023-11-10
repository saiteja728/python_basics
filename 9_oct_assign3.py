import os
try:
    os.rmdir("D:\KV234")
    print("Folder Removed-verify")
except FileNotFoundError:
    print("Folder Name does not Exists")
except OSError:
    print("Specified Folder Contains files-can't be removed")