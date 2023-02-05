import os
from PIL import Image 
import PIL 
import json 


def isJPG(fileName_caption, directory):
    for i, filename in enumerate(os.listdir(directory)):
        d = dict()
        if filename[-3:] == "jpg":
            d["image"] = filename # Image.open(directory+"/"+filename)
            d["caption"] = ""
            if i + 2 < len(os.listdir(directory)) and os.listdir(directory)[i + 2][-3:] == "txt":
                with open(directory+"/"+os.listdir(directory)[i + 2], 'r', encoding='utf8') as txtFile:
                    d["caption"] = " ".join(txtFile.readlines()).strip("\n")
            fileName_caption.append(d)


def main(path):
    fileName_caption = list()
    for filename in os.listdir(path):
        if os.path.isdir(path+"/"+filename):
            isJPG(fileName_caption, path+"/"+filename)
    return fileName_caption


if __name__ == "__main__":
    path = input("Enter path to directory: ")
    jsonData = main(path)
    print(jsonData)
    print(len(jsonData))

    with open("data.json", "w") as f:
        json.dump(jsonData, f)
    
# C:\Users\junya\Downloads\UCI\HackAtUCI\PetrGen\Back\PetrsNCaps