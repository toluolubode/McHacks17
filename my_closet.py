import math
import requests
from colorthief import ColorThief

clothes = ([
    # ["pant", 59, 60, 80, "http://www.onguardapparel.com/images/products/detail/74398_Company%20Pant-Navy.jpg"],
    #         ["pant", 69, 95, 144, "http://bit.ly/2kgERnh"],
    #         ["sweater", 37, 41, 65, "http://www.fabiboutique.com/buy-online/photos/italian-sweater-men.png"],
    #         ["pant", 52, 58, 80, "http://bit.ly/2kByKaq"],
    #         ["pants", 28, 28, 36, "http://thebestfashionblog.com/wp-content/uploads/2011/11/Dior-Jeans-for-Men_1.png"],
    #         ["shirt", 78, 125, 175, "http://bit.ly/2kg72m5"],
    #         ["sweater", 161, 159, 149, "http://bit.ly/2kgjq64"],
    #         ["sweater", 153, 152, 148, "http://bit.ly/2jj8wN7"]
])


def getUnrankedClothe(clothType):
    unrankedClothes = [];
    for cloth in clothes:
        if cloth[0] == clothType:
            unrankedClothes.append(cloth)
    return unrankedClothes



def getRankedClothe(unrankedClothes, cloth):
    diff = 0
    for unrankedClothe in unrankedClothes:
        r = math.fabs(cloth[1]-unrankedClothe[1])
        g = math.fabs(cloth[2]-unrankedClothe[2])
        b = math.fabs(cloth[3]-unrankedClothe[3])
        diff = int((r+g+b)/3)
        if len(unrankedClothe) == 6:
            unrankedClothe[5] = diff
        else:
            unrankedClothe.append(diff)
    rankedClothes = sorted(unrankedClothes, key=lambda x: float(x[5]))
    return rankedClothes


def lookForPants(cloth):
    unrankedPants = getUnrankedClothe("pant")
    rankedPants = getRankedClothe(unrankedPants, cloth)
    print(rankedPants)


def lookForSweaters(cloth):
    unrankedPants = getUnrankedClothe("sweater")
    rankedPants = getRankedClothe(unrankedPants, cloth)
    print(rankedPants)


def lookForShirt(cloth):
    unrankedPants = getUnrankedClothe("shirt")
    rankedPants = getRankedClothe(unrankedPants, cloth)
    print(rankedPants)


def main(lookFor, cloth):

    if lookFor == "pant":
        lookForPants(cloth)
    elif lookFor == "sweater":
        lookForSweaters(cloth)
    elif lookFor == "shirt":
        lookForShirt(cloth)
    clothes.append(cloth)


def getColor(fileName):
    color_thief = ColorThief(fileName)
    dominant_color = color_thief.get_color(quality=1)
    colors = [0,0,0]
    i = 0
    for color in dominant_color:
        colors[i] = color
        i += 1
    return colors


def start():
    while True:
        cloth = []
        cloth.append(input("Enter the cloth you have "))
        url = input("Url of the image")
        img_data = requests.get(url.strip()).content
        with open('image_name.png', 'wb') as handler:
            handler.write(img_data)
        colors = getColor('image_name.png')
        print("Enter RGB value for it")
        for color in colors:
            cloth.append(color)
        cloth.append(url)
        print(cloth)
        lookFor = input("Enter the clothe you are looking for:")
        main(lookFor, cloth)

start()
