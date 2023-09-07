creditor_Name="saiteja"
Debitor_Name="7hills"
bank_Name="KARURVYSHYA"
print("the orginal of String :",creditor_Name)
print("the reverse of string:",creditor_Name[::-1])
print("concatination of two strings:",creditor_Name+Debitor_Name)
print("repeatation of creditor:",creditor_Name*3)
print("substring of creditor_name:", creditor_Name[::])
print("string using in operator:", "sai" in creditor_Name)
print("string using not in debitor:", "yedu" not in Debitor_Name)
print("using split operator:", creditor_Name.split("a"))
print("using joining operator:", "%".join(bank_Name))
print("using replace method:", creditor_Name.replace("sai", "smart"))
print("concatination of string:", len(creditor_Name))
print("using upper method:", creditor_Name.upper())
print("using lower method:", creditor_Name.lower())
print("using find functoin:", creditor_Name.find("s"))
print("using index function:", Debitor_Name.index("7"))
print("using isupper() function:", bank_Name.isupper())
print("using islower() function:", bank_Name.islower())
print("using isdigit() function:", Debitor_Name.isdigit())
print("using isnumeric() function:", Debitor_Name.isnumeric())
multi_String= """the sky is blue my love is true east or west mylove is best"""
for iterator in multi_String[0:8].join("PYTHON"[::-1]):
    print(iterator)

    
