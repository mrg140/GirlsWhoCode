from grandfilter import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("kit.jpg")
    #pick one of the filters here
    newImg = maggie_grayscale(myImg)

    newImg.show()

main()
