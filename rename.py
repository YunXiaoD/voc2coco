import os
path = "./VOC/Annotations"
xmllist = os.listdir(path)
for i,name in enumerate(xmllist):
    os.rename(os.path.join(path,name),os.path.join(path,str(i)+".xml"))
    print(os.path.join(path,str(i)+".xml"))
print("rename success")