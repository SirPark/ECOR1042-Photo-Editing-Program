# ECOR1042-Photo-Editing-Program
Photo Editor Version 1.0 02/26/2021

CONTACT INFORMATION
-------------------
================================================================================================================================================================
E-mail: didikiye.ogbowu@carleton.ca

DESCRIPTION
-----------
================================================================================================================================================================
The program will be able to apply one of eight image filters cumulatively to an image. It is divided into two interfaces. 
The batch user interface take in the file name of a batch file that contains lines of commands to be executed. Each line
will have first, the file name of the original image that is to be edited, followed by the file name that the edited image
will be saved as, then a sequence of text characters, which represent the image filter to be applied cumulatively. The 
interactive user interface will the display the commands to be used and prompt the user to enter commands to load, edit,
and save images.

INSTALLATION
------------
================================================================================================================================================================
To run the program, a folder containing the image filter module, the interactive user interface, the batch user interface, batch files and the auxiliary modules
should be downloaded. Python 3.6 or higher would also need to be installed, and the numpy library would need to be installed by typing "pip install numpy" in
CMD. A python text editor such as Wing 101 7.2 would also need to be installed to open and run the program.

USAGE
-----
================================================================================================================================================================
To use the program, the interactive user interface or the batch user interface would need to be opened and run.

For the batch user interface, the name of the batch file is simply entered:

>>> batch_sample.txt
[Lines of commands in 'batch_sample.txt' are executed. The edited images are saved]

For the interactive user interface, the commands to be used are printed, and the user is prompted to enter commands to load, edit,
and save images:

L)oad image S)ave-as
3)-tone X)treme contrast T)int sepia P)osterize
E)dge detect D)raw curve V)ertical flip H)orizontal flip
Q)uit

:
>>> L
[Prompts the user to select an image file from the directory]
>>> P
[Applies the posterize filter to the selected image]
>>> V
[Applies the vertical flip filter to the image cumulative with the previous edit]
>>> S
[Prompts the user to save the edited image in the directory]

CREDITS
-------
================================================================================================================================================================
There are eight filters;

Three Tone filter was built by Didikiye Ogbowu
Extreme Contrast filter was built by Darius Banker
Sepia filter was built by Darius Banker
Posterize filter was built by James Keith 
Edge Detect filter was built by Darius Banker
Draw Curve filter was built by Didikiye Ogbowu
Vertical Flip filter was built by James Keith
Horizontal Flip filter was built by James Keith


MIT License

Copyright (c) 2021 Didikiye D. Ogbowu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
