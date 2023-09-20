import os
import shutil

#using append mode:
# fdirectory=os.mkdir("D:\\fileDirectory")
createFile1=open("D:\\fileDirectory\\file1.txt","a+")
# createFile1.write("jai bolo ganesh marath ki jai")
print("file append operation is done")

#using readmode:
createFile1=open("D:\\fileDirectory\\file1.txt","r+")
# createFile1.write("jack and jill went off the hill")
print(createFile1.read())

#using writemode:
createFile=open("D:\\fileDirectory\\file2.doc","w+")
# createFile.write("jack and jill went off the hill")
print("the file write is completed")

#binary files:
# createFile1=open("D:\\fileDirectory\\file3.mp4","x")

#using shutil package:
# shutil.copy("D:\\fileDirectory\\file1.txt","D:\\fileDirectory\\file2.doc")
print("copy done")
shutil.move("D:\\fileDirectory\\file3.mp4")
# createFile1.write("all is well")
# # print(createFile1.read())
# # print("the file read is completed")
# createFile1.truncate(2)
#
# createFile1.write("the file write is completed")
# createFile2=open("D:\\file2.txt","r+")
