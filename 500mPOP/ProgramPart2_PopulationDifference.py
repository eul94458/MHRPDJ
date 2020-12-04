print("#####################\nPart 2 program START.\n#####################")
import metadata
from PIL import Image, ImageDraw
import numpy
import math

def call_populationmap(year):
    matrix = []
    with open("data/outputdata/step1_populationmap/populationmap_" + str(year) + ".csv"  , "r" , encoding="utf-8") as input_file:
        for line in input_file:
            NewLine = line.strip()
            NewLine = NewLine.split(",")
            matrix.append(NewLine)
    return matrix

def defferentiate(universe):
    for n in range(len(universe)-1):
        before = universe[n]
        after = universe[n+1]

        matrixDifference = [[0 for i in range(5120)] for j in range(6240)]

        maxium = 0

        for rows in range(6240):
            for fields in range(5120):
                PopulationDifferent = int(after[rows][fields]) - int(before[rows][fields])
                matrixDifference[rows][fields] = PopulationDifferent
                if abs(PopulationDifferent) > maxium:
                    maxium = abs(PopulationDifferent)

        print("max =" , maxium)
        name = str(n+1)
        drawpopulationmap(matrixDifference,name)


def drawpopulationmap(matx,year):
    temp = numpy.array(matx)
    im = Image.fromarray(temp,"RGB")
    pix = im.load()
    height = len(matx)
    width = len(matx[0])
    for x in range(width):
        for y in range(height):
            if temp[y,x] == 0:
                pix[x,y] = (255,255,255)
            elif temp[y,x] < 0: #negative                    
                pix[x,y] = (int( 255- round( abs( (255)/(1+6.96875*math.e**(-(0.0007734370765*abs(temp[y,x]))))))),
                            int( 255- round( abs( (255)/(1+6.96875*math.e**(-(0.0007734370765*abs(temp[y,x]))))))),
                            int( 255))
                            
            elif temp[y,x] > 0: #positive                    
                pix[x,y] = (int( 255),
                            int( 255- round( abs( (255)/(1+6.96875*math.e**(-(0.0007734370765*abs(temp[y,x]))))))),
                            int( 255- round( abs( (255)/(1+6.96875*math.e**(-(0.0007734370765*abs(temp[y,x]))))))))
            # (R,G,B)
            #logistic-0.0030937483
            #h(x)=int(round(255 - (255)/(1+6.96875*math.e**(-(0.0007734370765*(temp[y,x]))))))
            #h(0)=32 , b = 0.0007734370765

    im.save("data/outputdata/step2_populationdifference/populationdifference_" + str(year) + '.tif')
    print("Map is output")


if __name__ == "__main__":

    while True:
        #query = input("Which year? : ")

        #if query != "quit":

        popmap1995 = call_populationmap(1995)
        popmap2000 = call_populationmap(2000)
        popmap2005 = call_populationmap(2005)
        popmap2010 = call_populationmap(2010)
        popmap2015 = call_populationmap(2015)

        wholelist = [popmap1995,popmap2000,popmap2005,popmap2010,popmap2015]

        defferentiate(wholelist)

        break


        #elif query == "quit":
        #    break
        #
        # 1995>2000 max=5000 count=5739
        # 2000>2005 max=1865 count=187313
        # 2005>2010 max=3162 count=14884
        # 2010>2015 max=2636 count=20883
    print("#####################\nPart 2 program END. \n#####################")
