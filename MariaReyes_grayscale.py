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
