def xmaslight():
    # This is the code from my 
    
    #NOTE THE LEDS ARE GRB COLOUR (NOT RGB)
    
    # Here are the libraries I am currently using:
    import time
    import board
    import neopixel
    import re
    import math
    import opensimplex
    
    # You are welcome to add any of these:
    # import random
    # import numpy
    # import scipy
    # import sys
    
    # If you want to have user changable values, they need to be entered from the command line
    # so import sys sys and use sys.argv[0] etc
    # some_value = int(sys.argv[0])
    
    # IMPORT THE COORDINATES (please don't break this bit)
    
    coordfilename = "Python/coords.txt"
	
    fin = open(coordfilename,'r')
    coords_raw = fin.readlines()
    
    coords_bits = [i.split(",") for i in coords_raw]
    
    coords = []
    
    for slab in coords_bits:
        new_coord = []
        for i in slab:
            new_coord.append(int(re.sub(r'[^-\d]','', i)))
        coords.append(new_coord)
    
    #set up the pixels (AKA 'LEDs')
    PIXEL_COUNT = len(coords) # this should be 500
    
    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)
    
    
    # YOU CAN EDIT FROM HERE DOWN
    
    # VARIOUS SETTINGS
    
    # pause between cycles (normally zero as it is already quite slow)
    slow = 0

    # simplex
    simplex_r = opensimplex.OpenSimplex(0)
    simplex_g = opensimplex.OpenSimplex(1)
    simplex_b = opensimplex.OpenSimplex(2)

    # brightness
    brightness = 100

    # position
    pos = (0.0, 0.0, 0.0)
    delta = (0.0, 0.0, 25.0)
    zoom = 400
    
    # yes, I just run which run is true
    run = 1
    while run == 1:
        
        time.sleep(slow)
        
        LED = 0
        while LED < len(coords):
            x = (coords[LED][0] + pos[0]) / zoom
            y = (coords[LED][1] + pos[1]) / zoom
            z = (coords[LED][2] + pos[2]) / zoom
            r = (simplex_r.noise3d(x, y, z) + 1) * brightness / 2
            g = (simplex_g.noise3d(x, y, z) + 1) * brightness / 2
            b = (simplex_b.noise3d(x, y, z) + 1) * brightness / 2
            pixels[LED] = [g, r, b]
            LED += 1
        
        # use the show() option as rarely as possible as it takes ages
        # do not use show() each time you change a LED but rather wait until you have changed them all
        pixels.show()

        # update position
        pos = (
            pos[0] + delta[0],
            pos[1] + delta[1],
            pos[2] + delta[2],
        )

    return 'DONE'


# yes, I just put this at the bottom so it auto runs
xmaslight()
