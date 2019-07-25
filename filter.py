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
def show_img(file):
    file.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgn, new):
    imgn.save(new)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
#def obamicon():


im = load_img("cat.jfif")
show_img(im)

save_img(im, "Kitty.jfif")
