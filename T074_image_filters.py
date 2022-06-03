# Milestone 3
# Team: T074
# Date submitted: February 22, 2021
# Filename: T074_image_filters.py
# 101205579 Didikiye Ogbowu
from Cimpl import *
import numpy as np
from  simple_Cimpl_filters import grayscale
from point_manipulation import *

def __iterR__(self: Image) -> Image:
    """Return a generator object that iterates over this Image's pixels
    from left to right, top to bottom. The values when iterating are
    Color objects, each containing the RGB color of one pixel. The Values are
    then changed so that only the green levels are maintained and the others are 
    set to zero.
    
    Author's Name: Darius Banker 101196575
    """
    width = self.get_width()
    height = self.get_height()
    for y in range(0, height):
        for x in range(0, width):
            col = Color._make(self.pixels[x, y])
            [r, g, b] = col 
            self.pixels[x, y] = tuple([r, 0, 0])
    return self

def red_channel(image: Image) -> Image:
    """Takes an Image, copies it, and creates a new image with only 
    the red RGB values per pixel remaining.
    
    Author's Name: Darius Banker 101196575
    """
    new_image = __iterR__(image)
    return new_image
        
def __iterG__(self: Image) -> Image:
    """Return a generator object that iterates over this Image's pixels
    from left to right, top to bottom. The values when iterating are
    Color objects, each containing the RGB color of one pixel. The Values are
    then changed so that only the green levels are maintained and the others are 
    set to zero
    
    Author's Name: Darius Banker 101196575
    """
    width = self.get_width()
    height = self.get_height()
    for y in range(0, height):
        for x in range(0, width):
            col = Color._make(self.pixels[x, y])
            [r, g, b] = col 
            self.pixels[x, y] = tuple([0, g, 0])
    return self

def green_channel(image: Image) -> Image:
    """Takes an Image, copies it, and creates a new image with only 
    the green RGB values per pixel remaining.
    
    Author's Name: Darius Banker 101196575
    """
    new_image = __iterG__(image)
    return new_image

def blue_channel(image: Image) -> Image:
    """ Returns a copy of an image with only the blue RGB value of each pixel
    
    Developer: James Keith 101201510
    """
    blue_pict = copy(image)
    height = get_height(blue_pict)
    width = get_width(blue_pict)
    for h in range(height):
        for w in range(width):
            c = get_color(blue_pict, w, h )
            r,g,b = c
            blue_c = create_color(0, 0, b)
            set_color(blue_pict, w, h, blue_c)
    return blue_pict

def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:
    """ Returns an image with RGB colour value from each of the images input as 
    arguments, i.e. the red value of the output image is that of "red_image". The
    green value is that of "green_image", and the blue value is that of "blue_image".
    
    Developer: 101205579 Didikiye Ogbowu
    """
    
    new_image = copy(red_image)
    
    for unit in new_image:
        x, y, (r, g, b) = unit
        this_image = list((r, g, b))
        
        this_image[1] = green_image.pixels[x, y][1]
        this_image[2] = blue_image.pixels[x, y][2]
        
        new_image.pixels[x, y] = tuple(this_image)
    return new_image

def three_tone(image: Image, color1: str, color2: str, color3: str) -> Image:
    """ Returns a modified version of the image 'image' that is made up of at most three
    RGB colours. This works by segregating pixel brightness into three classes: If the 
    average brightness of a pixel s is between 0 and 84, it is set to the first colour 
    'color1'. If the average brightness is between 85 and 170, it is set to the second colour 
    'color2'. If the average brightness is between 171 and 255, it is set to the third colour
    'color3'. 
    
    Developer: 101205579 Didikiye Ogbowu
    """
    new_image = copy(image)
    
    for unit in new_image:
        x, y, (r, g, b) = unit    
        brightness = (r + g + b) / 3
        
        if brightness <= 84:
            if color1 == "black":
                new_image.pixels[x, y] = (0, 0, 0)
            elif color1 == "white":
                new_image.pixels[x, y] = (255, 255, 255)       
            elif color1 == "blood":
                new_image.pixels[x, y] = (255, 0, 0)    
            elif color1 == "green":
                new_image.pixels[x, y] = (0, 255, 0)      
            elif color1 == "blue":
                new_image.pixels[x, y] = (0, 0, 255)
            elif color1 == "lemon":
                new_image.pixels[x, y] = (255, 255, 0)
            elif color1 == "cyan":
                new_image.pixels[x, y] = (0, 255, 255)                
            elif color1 == "magenta":
                new_image.pixels[x, y] = (255, 0, 255)
            else:
                new_image.pixels[x, y] = (128, 128, 128)
        elif brightness <= 170:
            if color2 == "black":
                new_image.pixels[x, y] = (0, 0, 0)
            elif color2 == "white":
                new_image.pixels[x, y] = (255, 255, 255)       
            elif color2 == "blood":
                new_image.pixels[x, y] = (255, 0, 0)    
            elif color2 == "green":
                new_image.pixels[x, y] = (0, 255, 0)      
            elif color2 == "blue":
                new_image.pixels[x, y] = (0, 0, 255)
            elif color2 == "lemon":
                new_image.pixels[x, y] = (255, 255, 0)
            elif color2 == "cyan":
                new_image.pixels[x, y] = (0, 255, 255)                
            elif color2 == "magenta":
                new_image.pixels[x, y] = (255, 0, 255)
            else:
                new_image.pixels[x, y] = (128, 128, 128)          
        else:
            if color3 == "black":
                new_image.pixels[x, y] = (0, 0, 0)
            elif color3 == "white":
                new_image.pixels[x, y] = (255, 255, 255)       
            elif color3 == "blood":
                new_image.pixels[x, y] = (255, 0, 0)    
            elif color3 == "green":
                new_image.pixels[x, y] = (0, 255, 0)      
            elif color3 == "blue":
                new_image.pixels[x, y] = (0, 0, 255)
            elif color3 == "lemon":
                new_image.pixels[x, y] = (255, 255, 0)
            elif color3 == "cyan":
                new_image.pixels[x, y] = (0, 255, 255)                
            elif color3 == "magenta":
                new_image.pixels[x, y] = (255, 0, 255)
            else:
                new_image.pixels[x, y] = (128, 128, 128)
    
    return new_image

def __iterE__(self: Image)-> Image:
    """Return a generator object that iterates over this Image's pixels
    from left to right, top to bottom. The values when iterating are
    Color objects, each containing the RGB color of one pixel. The function then
    compares the values of each pixel, and will set each individual RGB value per pixel
    to a certain value depending on what its stored value is, if the RGB value for a pixel is greater
    or equal to 128 it sets it to 255, if lower it is set to 0
    
    Author's Name: Darius Banker 101196575
    """
    width = self.get_width()
    height = self.get_height()
    for y in range(0, height):
        for x in range(0, width):
            col = Color._make(self.pixels[x, y])
            [r, g, b] = col 
            if(r >= 128):
                self.pixels[x, y] = tuple([255, g, b])
                r=255
            else:
                self.pixels[x, y] = tuple([0, g, b])
                r=0
            if(g >=128):
                self.pixels[x, y] = tuple([r, 255, b])
                g=255
            else:
                self.pixels[x, y] = tuple([r, 0, b])
                g=0
            if(b >= 128):
                self.pixels[x, y] = tuple([r, g, 225])
                b=225
            else:
                self.pixels[x, y] = tuple([r, g, 0])
                b=0
    return self
                
def extreme_contrast(image: Image) -> Image:
    """Takes an Image, copies it, and creates a new image with the values for each RGB level
    pixel set to either 255 or 0. It then saves and displays the newly created image.
    
    Author's Name: Darius Banker 101196575
    """
    copy_image = copy(image)
    new_image = __iterE__(copy_image)
    return new_image

def __iterS__(self: Image)-> Image:
    """Return a generator object that iterates over this Image's pixels
    from left to right, top to bottom. The values when iterating are
    Color objects, each containing the RGB color of one pixel. The Red and Blue values 
    are then changed based on the Red value of the pixel was and will reduce the Blue value 
    and increase the Red value by specific values depending on the previous red value 
    of the pixel. A sepia picture will be made if this filter is used sequentially after the
    grayscale function.
    Author's Name: Darius Banker 101196575
    """
    width = self.get_width()
    height = self.get_height()
    for y in range(0, height):
        for x in range(0, width):
            col = Color._make(self.pixels[x, y])
            [r, g, b] = col 
            if(r < 63):
                r = (int(r*1.1))
                b= (int(b*0.9))
                self.pixels[x, y] = tuple([r, g, b])
            elif(191 >= r >= 63):
                r =(int(r*1.15))
                b = (int(b*0.85))
                self.pixels[x, y] = tuple([r, g, b])
            elif(236 >= r > 191):
                r = (int(r*1.08))
                b = (int(b*0.93))
                self.pixels[x, y] = tuple([r, g, b])
            else:
                r=255
                b=(int(b*0.93))
                self.pixels[x, y] = tuple([r, g, b])
    return self

def sepia(image: Image) -> Image:
    """Takes an Image, copies it, and creates a new image in gray scale and then
    both increases and decreases the by a select percentage based upon what the grayscale
    value of the pixel is. It then saves and displays the newly created image.
    Author's Name: Darius Banker 101196575
    """
    
    copy_image = copy(image)
    new_image = __iterS__(grayscale(copy_image))
    return new_image

def _adjust_component(rgb_value: int) -> int:
    """ Returns the midpoint of the quadrant that the given RGB value is in. 
    >>> _adjust_component(50)
    31
    >>> _adjust_component(100)
    95
    Developer: James Keith 101201510
    """
    if rgb_value <= 63:
        new_rgb = 31
    elif 64 <= rgb_value <= 127:
        new_rgb = 95
    elif 128 <= rgb_value <= 191:
        new_rgb = 159
    else:
        new_rgb = 223
    return new_rgb

def posterize(image: Image) -> Image:
    """ Returns a copy of the given image with all the RGB values set to the midpoint
    of the quadrant they are in.
    
    Developer: James Keith 101201510
    """
    pict = copy(image)
    width = get_width(pict)
    height = get_height(pict)
    for h in range(height):
        for w in range(width):
            c = get_color(pict, w, h)
            r,g,b = c
            r = _adjust_component(r)
            g = _adjust_component(g)
            b = _adjust_component(b)
            new_c = create_color(r, g, b)
            set_color(pict, w, h, new_c)
    return pict

def __iterEdge__(self: Image, t: int) -> Image:
    """Return a generator object that iterates over this Image's pixels
    from left to right, top to bottom. The values when iterating are
    Color objects, each containing the RGB color of one pixel. The Values are
    then are then compared to the values of the pixel below it, and if the difference
    has a greater value that |8|, then the pixel is set to black(0,0,0). Once the iteration 
    reaches the bottom row, all the values are set to white (255,255,255). It then displays
    and returns the image in this format.
    Author's Name: Darius Banker 101196575
    """
    width = self.get_width()
    height = self.get_height()
    
    if t >= 0:               
        for y in range(0, height):
            for x in range(0, width):
                if(y < height-1):           
                    col = Color._make(self.pixels[x, y])
                    [r, g, b] = col 
                    bright1 = (r)
                    col1= Color._make(self.pixels[x, y+1])
                    [r, g, b] = col1 
                    bright2 = (r)                  
                    contrast= abs(bright1-bright2)
                    if(contrast >= t):
                        self.pixels[x, y] = tuple([0, 0, 0])
                    elif(contrast < t):
                        self.pixels[x, y] = tuple([255, 255, 255])
                elif(y==height-1):
                    self.pixels[x, y] = tuple([255, 255, 255])
                    return self
    else:
        print("Please Choose a Postive Value for t")
    

def detect_edges(image: Image, t) -> Image:
    """Takes an Image, copies it, and creates a new image with edge detection
    that looks like it has been sketched
    Author's Name: Darius Banker 101196575
    """
    copy_image = copy(image)
    new_image = __iterEdge__(copy_image, t)
    return new_image

def _interpolation(pointlist: list) -> list:
    """ Returns a list of the coefficients of the equation of fit curve from highest
    to lowest degree. A list pointlist containing tuples of length two is plugged into
    the function. These tuples represent coordinates. If the number of tuples in the list is 
    less than four, the coefficients would be found for an interpolation curve. Otherwise, they
    would be found for a regression curve. In both cases, a matrix equation AX = B is derived
    and solved. The matrices A and B are derived by sorting. X is the list of coefficients to be
    returned
    >>> _interpolation([(34, 80), (20, 138)])
    [-4.142857142857143, 220.85714285714286]
    >>> _interpolation([(100, 205), (288, 312), (490, 210)])
    [54.242021276594535, -53.67287234042434, 39.60106382979065]
    >>> _interpolation([(0,10),(20,37),(99,120),(200,0)])
    [-382017.69999641925, 386839.09999637405, -2447.1999999766817]
    
    Developer: 101205579 Didikiye Ogbowu
    """
    sorted_list = sort_points(pointlist)
    my_vectors = get_x_y_lists(sorted_list)    
    
    if len(pointlist) < 4:
        if len(pointlist) == 2:
            x1 = my_vectors[0][0]
            x2 = my_vectors[0][1]
            
            A = np.array([[x1, 1], [x2, 1]])
        else:
            x1 = my_vectors[0][0]
            x2 = my_vectors[0][1]
            x3 = my_vectors[0][2]
            
            A = np.array([[(x1 ^ 2), x1, 1], [(x2 ^ 2), x2, 1], [(x3 ^ 2), x3, 1]])
        B = np.array(my_vectors[1])
        
    else:
        x_four = 0
        x_three = 0
        x_two = 0
        x = 0
        y = 0
        x_beta = 0
        x_alpha = 0
        one = 0          
        
        for i in range(len(my_vectors[0])):
            x_four += my_vectors[0][i] ^ 4
            x_three += my_vectors[0][i] ^ 3
            x_two += my_vectors[0][i] ^ 2
            x += my_vectors[0][i]
            y += my_vectors[1][i]
            x_beta += my_vectors[0][i] * my_vectors[1][i]
            x_alpha += (my_vectors[0][i] ^ 2) * my_vectors[1][i]
            one += 1
            
        A = np.array([[x_four, x_three, x_two], [x_three, x_two, x], [x_two, x, one]])
        B = np.array([x_alpha, x_beta, y])
    #print(X)
    X = list(np.linalg.solve(A, B))
    return X

def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> int:
    """
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains the
    coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds.
   
    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None
    
    Developer: 101205579 Didikiye Ogbowu
    """
    EPSILON = 1
    guess = 0
    
    while guess < max_x:
        test_val = np.polyval(polycoeff, guess)
        
        if abs(test_val - val) <= EPSILON:
            break
        else:
            guess += EPSILON
            
    test_val = np.polyval(polycoeff, guess)
    
    if abs(test_val - val) > EPSILON:
        return None
    else:
        return guess
    
def _image_border_finding(size: list, coeff: list) -> list:
    """ Returns a list containing the points of intersection of a polynomial with
    coefficients coeff with the border of an image of size size. The points of 
    intersection on the vertical borders are found by plugging the extreme values
    into the polynomial, and the points of intersection on the horizontal borders are 
    found by setting the polynomial to extreme values and using exhaustive enumeration
    to solve.
    >>> _image_border_finding([100, 100], [7, 4, 3])
    [(0, 3)]
    >>> _image_border_finding([640, 480], [54.242021276594535, -53.67287234042434, 39.60106382979065])
    [(0, 39)]
    >>> _image_border_finding([640, 480], [-382017.69999641925, 386839.09999637405, -2447.1999999766817])
    []
    
    Developer: 101205579 Didikiye Ogbowu
    """
    X = size[0]
    Y = size[1]
    points = []
   
    vert1 = np.polyval(coeff, 0)
    vert2 = np.polyval(coeff, X - 1)
    hor1 = _exhaustive_search(X, coeff, 0)
    hor2 = _exhaustive_search(X, coeff, Y - 1)
    
    
    if 0 <= vert1 <= Y - 1:
        points.append((0, int(vert1)))
        #print("good")
    if 0 <= vert2 <= Y - 1:
        points.append((X - 1, int(vert2)))
        #print("good")
    if hor1 != None and 0 <= hor1 <= X - 1:
        points.append((int(hor1), 0))
        #print("good")
    if hor2 != None and 0 <= hor2 < X - 1:
        points.append((int(hor2), Y - 1))  
        #print("good")
    
    return points

def draw_curve(image: Image, colour: str, pointlist: list = None) -> tuple:
    """ Returns a tuple containing a image with a specified curve drawn on it and a
    list containing the points of intersection of the curve with the border of the image.
    
    Developer: 101205579 Didikiye Ogbowu
    """
    X = get_width(image)
    Y = get_height(image)
    size_list = [X, Y]
    
    if pointlist == None:
        pointlist = []
        print("Image size, width and height respectively:", size_list)
        list_len = int(input("How many points do you want to provide? The number should be greater than 1. "))
        
        for i in range(list_len):
            x_coord = int(input("Input x coordinate: "))
            y_coord = int(input("Input y coordinate: "))
            coord = (x_coord, y_coord)
            pointlist += [coord]
    
    #print(pointlist)
    coeff_list = _interpolation(pointlist)
    #print(coeff_list)
    border_points = _image_border_finding(size_list, coeff_list)
    
    new_image = copy(image)
    EPSILON = 1
    
    for unit in new_image:
        x, y, (r, g, b) = unit
        derived =  np.polyval(coeff_list, x)

        if 0 <= y - derived < EPSILON:
            if colour == "black":
                new_image.pixels[x, y - 2] = (0, 0, 0)
                new_image.pixels[x, y - 1] = (0, 0, 0)
                new_image.pixels[x, y] = (0, 0, 0)
                new_image.pixels[x, y + 1] = (0, 0, 0)
                new_image.pixels[x, y + 2] = (0, 0, 0)
            elif colour == "white": 
                new_image.pixels[x, y - 2] = (255, 255, 255) 
                new_image.pixels[x, y - 1] = (255, 255, 255) 
                new_image.pixels[x, y] = (255, 255, 255) 
                new_image.pixels[x, y + 1] = (255, 255, 255) 
                new_image.pixels[x, y + 2] = (255, 255, 255)                 
            elif colour == "blood":
                new_image.pixels[x, y - 2] = (255, 0, 0)
                new_image.pixels[x, y - 1] = (255, 0, 0)
                new_image.pixels[x, y] = (255, 0, 0)
                new_image.pixels[x, y + 1] = (255, 0, 0)
                new_image.pixels[x, y + 2] = (255, 0, 0)               
            elif colour == "green":   
                new_image.pixels[x, y - 2] = (0, 255, 0)
                new_image.pixels[x, y - 1] = (0, 255, 0)
                new_image.pixels[x, y] = (0, 255, 0)
                new_image.pixels[x, y + 1] = (0, 255, 0)
                new_image.pixels[x, y + 2] = (0, 255, 0)                
            elif colour == "blue":
                new_image.pixels[x, y - 2] = (0, 0, 255)
                new_image.pixels[x, y - 1] = (0, 0, 255)
                new_image.pixels[x, y] = (0, 0, 255)
                new_image.pixels[x, y + 1] = (0, 0, 255)
                new_image.pixels[x, y + 2] = (0, 0, 255)               
            elif colour == "lemon":
                new_image.pixels[x, y - 2] = (255, 255, 0)
                new_image.pixels[x, y - 1] = (255, 255, 0)
                new_image.pixels[x, y] = (255, 255, 0)
                new_image.pixels[x, y + 1] = (255, 255, 0)
                new_image.pixels[x, y + 2] = (255, 255, 0)                
            elif colour == "cyan":         
                new_image.pixels[x, y - 2] = (0, 255, 255)
                new_image.pixels[x, y - 1] = (0, 255, 255)
                new_image.pixels[x, y] = (0, 255, 255)
                new_image.pixels[x, y + 1] = (0, 255, 255)
                new_image.pixels[x, y + 2] = (0, 255, 255)                
            elif colour == "magenta":
                new_image.pixels[x, y - 2] = (255, 0, 255)
                new_image.pixels[x, y - 1] = (255, 0, 255)
                new_image.pixels[x, y] = (255, 0, 255)
                new_image.pixels[x, y + 1] = (255, 0, 255)
                new_image.pixels[x, y + 2] = (255, 0, 255)                
            else:        
                new_image.pixels[x, y - 2] = (128, 128, 128)
                new_image.pixels[x, y - 1] = (128, 128, 128)
                new_image.pixels[x, y] = (128, 128, 128)
                new_image.pixels[x, y + 1] = (128, 128, 128)
                new_image.pixels[x, y + 2] = (128, 128, 128)
                
    return (new_image, border_points)

def flip_horizontal(image):
    """ Flips an image along the vertical centre line
    
    Developer: James Keith 101201510
    """
    pict = copy(image)
    height = get_height(pict)
    width = get_width(pict)
    for h in range(height):
        for w in range(width):
            c = get_color(image, width - 1 - w, h)
            set_color(pict, w, h, c)
    return pict

def flip_vertical(image):
    """ Flips an image along the center horizontal line.
    
    Developer: James Keith 101201510
    """
    pict = copy(image)
    height = get_height(pict)
    width = get_width(pict)
    for h in range(height):
        for w in range(width):
            c = get_color(image, w, height - 1 - h)
            set_color(pict, w, h, c)
    return pict
