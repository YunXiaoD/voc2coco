import os
annPath = "./VOC/Annotations"
nameList = os.listdir(annPath)
with open("./VOC/annpaths_list.txt","a") as f:
    for i,name in enumerate(nameList):
        writePath = annPath+"/"+name
        f.write(writePath+"\n")
f.close()
