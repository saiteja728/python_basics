import os

# # directory=os.mkdir("D:\\filehandling")
# # if not os.path.exists(directory) :
# #     print("created new directory with name", directory)
# # else:
# #     print("already exist")
# #
# # print("current directory path is:",directory)
# # changeDirectory=os.chdir("D:\\filehandling")
# # print("changed directory is:",changeDirectory)
# # oldDirectory=os.listdir(changeDirectory)
# # print("list of content is:", oldDirectory)
# # insideDire=os.mkdir("D:\\filehandling\\newFile1.doc")
# os.rmdir("D:\\filehandling")
# directory=os.removedirs("C:\\filehandling\\interview.txt")
# os.rmdir("D:\\filehandling")


# os.mkdir('D:\\file')
# Specify the path to the directory you want to change to
new_directory_path = 'D:\\file'

# Use os.chdir() to change the current working directory
os.chdir(new_directory_path)

# Now, the current working directory is set to 'new_directory'

# Check the current working directory after the change
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")



