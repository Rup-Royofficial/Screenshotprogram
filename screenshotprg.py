import pyscreenshot #first python -m install Pillow pyscreenshot

image = pyscreenshot.grab(bbox=(10, 10, 1000, 400)) #screen resolution for SS 1. is for left margin 2. is for top margin 3. is for breadth 4. bottom margin
image.show() # shows you the ss
image.save("TestingSSprogram.png") #saves as per the name