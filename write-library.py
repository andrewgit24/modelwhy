# Library code string using python multiline quotes. Do not include test code, only the functions you want to reuse and the imports they need.
code: str = '''
from hub import light_matrix
def right():
    light_matrix.show_image(light_matrix.IMAGE_ARROW_E)
def left():
    light_matrix.show_image(light_matrix.IMAGE_ARROW_W)
'''
def exportProgram(): # Function to export the library code string
    import os
    global code
    #os.mkdir('/flash/customlib')
    os.chdir('/flash/customlib') # change directory to root
    try:
        os.remove('team66218lib.py') # remove any existing library file of the same name
    except:
        pass
    f = open('team66218lib.py', 'w+') # Create a new file customlib.py in the SPIKE hub root
    f.write(code) # Write out the library code string to the customlib.py file
    f.close()
 
import sys
exportProgram() # Runs the export function
