# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(picture):
    im = Image.open(picture)
    return im
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(picture):
    picture.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(picture, new):
    picture.save(new)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):
    pixel = list(im.getdata())
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightblue = (112,150,158)
    yellow = (252,227,166)

    new_pic = []

    for p in pixel:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pic.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pic.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pic.append(lightblue)
        elif intensity >= 546:
            new_pic.append(yellow)

    cat_new = Image.new("RGB", (450,300))
    cat_new.putdata(new_pic)
    cat_new.show()

    im = Image.open("kit.jpg")
#    new_pic = im.putdata(intensity)
#    def save_img (im, cat_new):
#        im.save(cat_new)
#    save_img(im, "kit.jpg")
#    newpicture = load_img("kit.jpg")
#    show_img(newpicture)

def grayscale(im):
    pixel = list(im.getdata())
    black= (0, 0 ,0)
    darkgray= (105,105,105)
    lightgray= (211,211,211)
    white= (255,255,255)
    newgray = []

    for p in pixel:
        intensity = p[0] + p[1] + p[2]
        if intensity < 200:
            newgray.append(black)
        elif intensity >= 180 and intensity < 360:
            newgray.append(darkgray)
        elif intensity >= 360 and intensity < 540:
            newgray.append(lightgray)
        elif intensity >= 540:
            newgray.append(white)

    cat_new = Image.new ("RGBA", (450, 300))
    cat_new.putdata (newgray)
    cat_new.show()

def alt(im):
    pixelR = list(im.getdata(0))
    #pixelG = list (im.getdata(1))
    pixelB = list(im.getdata(2))
    pixel = list(im.getdata())
    green = (0, 100 , 0)
    new_alt=[]
    #for p in pixelR:
    #    new_alt.append(pixelR)
    for p in pixel:
        intensity = p[0] + p[1] + p[2]
        list(im.getdata(0))+green
        list(im.getdata(2))+green
        #makes image green, not a green tint
    #for p in pixelB:
        #new_alt.append(pixelB)
    cat_new = Image.new ("RGBA", (450, 300))
    cat_new.putdata (new_alt)
    cat_new.show()

im = load_img("kit.jpg")
show_img(im)


newpic = alt(im)

#save_img(im, "Kitty.jfif")
