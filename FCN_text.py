import os
import pickle

def saveList(saveFolder,listFile, filename = 'outfile'):
    # Writing a list to a file with Python
    with open(saveFolder + "/" + filename, 'wb') as fp:
        pickle.dump(listFile, fp)

path = 'C:\Users\CYEH1\OneDrive - Monsanto\Stalk_Images_lab_batch-blue'
saveFolder = path

os.chdir(path)
listFile = []
cnt = 0
file = open("stalkFCN.txt","w")
for filename in os.listdir("."):
    if filename.startswith("DSC"):
        # save first one as demo
        cnt = cnt + 1
        if cnt == 1:
            continue
        file.write( filename + " " + "circle_mask" + filename + "\n")
        print filename


"""example"""
# file = open("text.txt","w")
# file.write("11 33\n")
# file.write("1221\n")
file.close()