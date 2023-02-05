import os
from PIL import Image  
import json 


def loopPetrDir(fileName_caption, directory):
    """
    This function will loop though the petr directory of images and text files.
    It will add create a dictionary of {image: imageName, caption: text} and add to the list. 
    """
    for filename in os.listdir(directory):
        d = dict() # {image: imageName, caption: text}
        if filename[-3:] == "jpg":
            d["image"] = filename
            d["caption"] = ""

            # if there are multiple images per post,
            # the filename will end in _n for which n is the number of images in a post
            # we will rename the filename, by removing the _n
            if filename[-5].isnumeric(): 
                filename = filename[0:-6] + ".jpg"

            # if the caption file exists in the directory 
            # we will open the text file and 
            # set the contents of the text file as the caption 
            if filename[:-3]+"txt" in os.listdir(directory):
                with open(directory+"/"+filename[:-3]+"txt", 'r', encoding='utf8') as txtFile:
                    d["caption"] = " ".join(txtFile.readlines()).strip("\n")
            
            # add the newly created dictionary to the list 
            fileName_caption.append(d)


def loopDir(path):
    """
    This function will iterate though the folder to look up directories of petr folders.
    And will add {images and captions} to the returned list.
    """
    fileName_caption = list()
    for filename in os.listdir(path):
        # if the filename is a petr director, add to the list 
        if os.path.isdir(path+"/"+filename):
            loopPetrDir(fileName_caption, path+"/"+filename)
    return fileName_caption


def main():
    """
    This is the main function, which will ask the user for their path, 
    loop through the directory, and create a json file from the data. 
    """
    path = input("Enter path to directory: ")
    jsonData = loopDir(path)

    # will create a data.json file to write the list contents in json format 
    with open("data.json", "w") as f:
        json.dump(jsonData, f)


if __name__ == "__main__":
    main()
