print("#####################\nPart 2.7 program START.\n#####################")
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

    matrixLocalChange = []
    matrixLocalZ = []
    matrixLocalStddev = [[0 for i in range(5120)] for j in range(6240)]

    for rows in range(6240):
        for fields in range(5120):
            condition1 = int(universe[1][rows][fields]) != 0
            condition2 = int(universe[2][rows][fields]) != 0
            condition3 = int(universe[3][rows][fields]) != 0
            condition4 = int(universe[4][rows][fields]) != 0
            conditionsum = condition1 or condition2 or condition3 or condition4
            if conditionsum == True:
                CellYX = str(rows) + "_" + str(fields)
                changelist = []

                for n in range(len(universe)-1):
                    before = universe[n][rows][fields]
                    after = universe[n+1][rows][fields]
                    pplchange = int(after)-int(before)
                    changelist.append(pplchange)
                
                #print(changelist)
                changemean = sum(changelist) / len(changelist)
                changevariantlist = []
                for n in changelist:
                    variant = (n - changemean)**2
                    changevariantlist.append(variant)
                samplestddev = sum(changevariantlist) / (len(changelist)-1)

                changezscore = []
                for n in changelist:
                    if samplestddev != 0:
                        zscore = (n - changemean) / samplestddev
                        changezscore.append(zscore)
                    else:
                        changezscore.append(0)
                        
                matrixLocalStddev[rows][fields] = samplestddev
                changelist.insert(0,CellYX)
                changezscore.insert(0,CellYX)
                matrixLocalChange.append(changelist)
                matrixLocalZ.append(changezscore)
    
    
    filenameChange = "data/outputdata/step2_populationdifference/LocalChange.csv"
    metadata.writeout(matrixLocalChange,filenameChange)
    
    filenameZ = "data/outputdata/step2_populationdifference/LocalZ.csv"
    metadata.writeout(matrixLocalZ,filenameZ)
    
    filenameS = "data/outputdata/step2_populationdifference/LocalStddec.csv"
    metadata.writeout(matrixLocalStddev,filenameS)
    
    filenameStddev = "LocalStddec"
    drawmap(matrixLocalStddev,filenameStddev,1)
    
    


def drawmap(matx,c,para):
    temp = numpy.array(matx)
    im = Image.fromarray(temp,"RGB")
    pix = im.load()
    width = len(matx[0])
    height = len(matx)
    for x in range(width):
        for y in range(height):
            if para == 1:
                if temp[y,x] == 0:
                    pix[x,y] = (255,255,255)
                else:
                    pix[x,y] = (int(round(255-(255)/(1+6.96875*math.e**(-(0.0030937483*temp[y,x]))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(0.0030937483*temp[y,x]))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(0.0030937483*temp[y,x]))))))
            elif para == 2:
                if temp[y,x] == 0:
                    pix[x,y] = (255,255,255)
                else:
                    pix[x,y] = (int(round(255-(255)/(1+6.96875*math.e**(-(0.01933592691*temp[y,x]))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(0.01933592691*temp[y,x]))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(0.01933592691*temp[y,x]))))))
            elif para == 3:
                if temp[y,x] == 0:
                    pix[x,y] = (255,255,255)
                elif -2 <= temp[y,x] <= 2 and temp[y,x] != 0:
                    pix[x,y] = (128,128,128)
                elif temp[y,x] < -2:
                    pix[x,y] = (223,223,223)
                elif 2 < temp[y,x]:
                    pix[x,y] = (0,0,0)
            elif para == 4:
                if temp[y,x] == 0:
                    pix[x,y] = (255,255,255)
                else:
                    pix[x,y] = (int(round(255-(255)/(1+6.96875*math.e**(-(3.867185382*temp[y,x]))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(3.867185382*temp[y,x]))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(3.867185382*temp[y,x]))))))
            elif para == 5:
                if temp[y,x] == 0:
                    pix[x,y] = (128,128,128)
                else:
                    pix[x,y] = (int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*(temp[y,x])+3))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*(temp[y,x])+3))))),
                                int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*(temp[y,x])+3))))))

            #logistic-0009
            #g(x)=255-(255)/(1+6.96875e^(-(0.0009*x)))
            #g(0)=32 , b = 0.0009

            #logistic-0.0030937483
            #h(x)=255-(255)/(1+6.96875e^(-(0.0030937483*x)))
            #h(0)=32 , b = 0.0030937483 , h(625)=128

            #logistic-0.01933592691
            #m(x)=255-(255)/(1+6.96875e^(-(0.01933592691*x)))
            #m(0)=32 , b = 0.01933592691 , m(100)=128

            #logistic-0.01933592691
            #m(x)=255-(255)/(1+6.96875e^(-(3.867185382*x)))
            #m(0)=32 , b = 0.01933592691 , m(0.5)=128

            #linear
            #f(x)=255-( (223/1000)*x +32)

            #m = (ln(128/6.96875(255-128)))/100
            #int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*(temp[y,x])+3)))))
            #255-(255)/(1+6.96875*e**(-(0.6445308971*(x+3))))
            # f(3)=128
    im.save("data/outputdata/step2_populationdifference/" + c + '.tif')
    print("Map is output")


if __name__ == "__main__":

    while True:

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

#max= 610.5 +mean= 0.4259507742607847 +ddev= 0.4749627144919295 min= -1.0 -mean= -0.1950052426900056 -stddev= 0.19530622874674042

#max= 1545.0 +mean= 0.8248890106968028 +ddev= 0.9064839304260386 min= -1.0 -mean= -0.39053747089385843 -stddev= 0.39001647456425587

#max= 1136.0 +mean= 0.5141332834719601 +ddev= 0.5808755089575358 min= -1.0 -mean= -0.26359615679908094 -stddev= 0.26364790390178944

#max= 1103.0 +mean= 0.553058258193743 +ddev= 0.6192574953280646 min= -1.0 -mean= -0.29360948190878305 -stddev= 0.29358297316042353
    print("#####################\nPart 2.7 program END. \n#####################")
