# check if a file is a jpg 

import os
from PIL import Image 
import PIL 

def isJPG(fileName_caption, directory):
    for i, filename in enumerate(os.listdir(directory)):
        d = dict()
        if filename[-3:] == "jpg":
            d["image"] = Image.open(directory+"/"+filename)
            d["caption"] = ""
            if i + 2 < len(os.listdir(directory)) and os.listdir(directory)[i + 2][-3:] == "txt":
                with open(directory+"/"+os.listdir(directory)[i + 2], 'r', encoding='utf8') as txtFile:
                    d["caption"] = " ".join(txtFile.readlines()).strip("\n")
            fileName_caption.append(d)


def main():
    fileName_caption = list()
    path = "C:/Users/junya/Downloads/UCI/HackAtUCI/PetrGen/Backend/"
    for filename in os.listdir(path):
        if os.path.isdir(path +filename):
            isJPG(fileName_caption, path+filename)

main()
