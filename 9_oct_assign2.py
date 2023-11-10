import os
try:
    os.rename("Hyderabad","HYD")
    print("Folder Renamed---Verify")
except FileNotFoundError:
    print("Old Folder Does not exists")