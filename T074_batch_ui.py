# Milestone 3
# Team: T074
# Date submitted: February 22, 2021
# Filename: T074_batch_ui.py
# 101205579 Didikiye Ogbowu
from Cimpl import *
from T074_image_filters import *

def filterer(an_image: Image, keyword: str) -> Image:
    """ Returns a version of the image an_image with the filter represented by keyword
    applied to it. For filter functions that require additional arguments, those arguments
    are hard-coded.
    
    Developer: 101205579 Didikiye Ogbowu
    """
    THRESHOLD = 15
    
    if keyword == "3":
        new_image = three_tone(an_image, "blood", "lemon", "gray")
    elif keyword == "X":
        new_image = extreme_contrast(an_image)
    elif keyword == "T":
        new_image = sepia(an_image)
    elif keyword == "P":
        new_image = posterize(an_image)
    elif keyword == "E":
        new_image = detect_edges(an_image, THRESHOLD)
    elif keyword == "V":
        new_image = flip_horizontal(an_image)
    elif keyword == "H":
        new_image = flip_vertical(an_image)

    return new_image

# Main Script
file_name = input("Input name of file:  ")

infile = open(file_name, "r")

for line in infile:
    key_container = line.split()
    
    my_image = key_container[0]
    image = load_image(my_image)
    
    for i in range(2, len(key_container)): 
        image = filterer(image, key_container[i])
    
    save_as(image, key_container[1])
        