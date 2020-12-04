print("#####################\nPart 1 program START.\n#####################")
import metadata
from PIL import Image, ImageDraw
import numpy
import math

def drawpopulationmatrix(id):
    tempStorage = []

    with open("data/outputdata/step0_mergegrid/mergegrid_" + query + ".csv"  , "r" , encoding="utf-8") as input_file:
        for line in input_file:
            NewLine = line.strip()
            NewLine = NewLine.split(",")
            oriCellID = int(NewLine[0])
            Population = int(NewLine[1])
            tempStorage.append((oriCellID,Population))

    matrix = [[0 for i in range(5120)] for j in range(6240)]

    for eachGrid in tempStorage:
        (oriCellID,Population) = eachGrid
        oriCellID=str(oriCellID)        
        Yaxis01 = [int(oriCellID[0:2]),int(oriCellID[4]),int(oriCellID[6])]
        Xaxis01 = [int(oriCellID[2:4]),int(oriCellID[5]),int(oriCellID[7])]
        lastDigit = int(oriCellID[8])

        if lastDigit == 3 or lastDigit == 4:
            y = 0
        elif lastDigit == 1 or lastDigit == 2:
            y = 1
        Yaxis = (68-Yaxis01[0])*160 + (7-Yaxis01[1])*20 + (9-Yaxis01[2])*2 + y

        if lastDigit == 3 or lastDigit == 1:
            x = 0
        elif lastDigit == 4 or lastDigit == 2:
            x = 1
        Xaxis = (Xaxis01[0]-22)*160 + Xaxis01[1]*20 + Xaxis01[2]*2 + x

        matrix[Yaxis][Xaxis] = Population

    return matrix
            
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
            else:
                pix[x,y] = (int(round(255 - (255)/(1+6.96875*math.e**(-(0.0007734370765*(temp[y,x])))))),
                            int(round(255 - (255)/(1+6.96875*math.e**(-(0.0007734370765*(temp[y,x])))))),
                            int(round(255 - (255)/(1+6.96875*math.e**(-(0.0007734370765*(temp[y,x])))))))
            # (R,G,B)
            #logistic-0.0030937483
            #h(x)=int(round(255 - (255)/(1+6.96875*math.e**(-(0.0007734370765*(temp[y,x]))))))
            #255 - (255)/(1+6.96875*e^(-(0.0007734370765*x])))
            #h(0)=32 , b = 0.0007734370765

    im.save("data/outputdata/step1_populationmap/populationmap_" + year + '.tif')
    print("Map is output")
    

if __name__ == "__main__":

    while True:
        #query = input("Which year? : ")

        #if query != "quit":

        target = ["1995","2000","2005","2010","2015"]
        for year in target:
            query = year

            requestedpopmatrix = drawpopulationmatrix(query)

            filename = "data/outputdata/step1_populationmap/populationmap_" + str(query) + ".csv"
            metadata.writeout(requestedpopmatrix,filename)

            drawpopulationmap(requestedpopmatrix,year)

        break

        #elif query == "quit":
        #    break
    print("#####################\nPart 1 program END. \n#####################")
