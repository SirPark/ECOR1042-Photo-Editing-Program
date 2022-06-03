#Name:Darius Banker
#Student Number: 101196575
#Filename: T074_interactive_ui
from Cimpl import* 
from T074_image_filters import *
from simple_Cimpl_filters import*
from string import*

def filterers(an_image: Image, keyword: str) -> Image:
    """ Returns a version of the image an_image with the filter represented by keyword
    applied to it. For filter functions that require additional arguments, those arguments
    are hard-coded.
    
    Developer: Darius Banker 101196575
    """
    if keyword == "3":
        an_image = three_tone(an_image, "blood", "lemon", "gray")
        show(an_image)
    elif keyword == "X":
        an_image = extreme_contrast(an_image)
        show(an_image)
    elif keyword == "T":
        an_image = sepia(an_image)
        show(an_image)
    elif keyword == "P":
        an_image = posterize(an_image)
        show(an_image)
    elif keyword == "E":
        print("Threshold Value?")
        threshold = int(input())
        an_image = detect_edges(an_image, THRESHOLD)
        show(an_image)
    elif keyword == "D":
        this_image = draw_curve(an_image, "cyan")
        an_image = this_image[0]
        show(an_image)
    elif keyword == "V":
        an_image = flip_horizontal(an_image)
        show(an_image)
    elif keyword == "H":
        an_image = flip_vertical(an_image)
        show(an_image)
    elif keyword == "Q":
        return None
    elif keyword == "L":
        an_image = load_image(choose_file())
        show(an_image)    
    elif keyword == "S":
        save_as(an_image)
    else:
        print("No such command")
    return an_image

def get_command() -> None:
    """Prints an interactive user interface and prompts the user for input based 
    on the options given. Once an image is load is puts the chosen image through
    each of the chosen filters and will display the image. It will cancel
    the loop when prompted and can load a new image when prompted.
    
    Developers: Darius Banker 101196575 and James Keith 101201510
    """
    keys=['S', '3', 'X', 'T', 'P', 'E', 'D', 'V', 'H', 'Q', 'L']
    print("L)oad image S)ave-as\n3)-tone X)treme contrast T)int sepia P)osterize\nE)dge detect D)raw curve V)ertical flip H)orizontal flip\nQ)uit\n\n: ")
    while True:
        keyword=input()
        keyword= keyword.upper()
        if keyword == "Q":
            break        
        elif keyword == "L":
            an_image = load_image(choose_file())
            show(an_image)
            while True:
                keyword = input()
                keyword = keyword.upper()
                if keyword == "Q":
                    break
                elif keyword in keys:
                    an_image = filterers(an_image, keyword)
                elif keyword not in keys:
                    print("No such command")  
        elif keyword != "L" and keyword in keys:
            print("No Image Loaded")
        elif keyword not in keys:
            print("No such command")
                        
            
        
#Main Script       
if __name__ == "__main__":
    get_command()
    
        
        







