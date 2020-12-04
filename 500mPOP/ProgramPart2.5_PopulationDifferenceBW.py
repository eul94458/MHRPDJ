print("#####################\nPart 2.5 program START.\n#####################")
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
        number = 0
        
        diffall = []
        for rows in range(6240):
            for fields in range(5120):
                condition1 = int(after[rows][fields])==0 and int(before[rows][fields])==0
                if condition1 == False :
                    PopulationDifferent = int(after[rows][fields]) - int(before[rows][fields])
                    matrixDifference[rows][fields] = PopulationDifferent
                    diffall.append(PopulationDifferent)
                    if abs(PopulationDifferent) > maxium:
                        maxium = abs(PopulationDifferent)
                    if PopulationDifferent != 0:
                        number += 1
                        
        diffmean = sum(diffall)/len(diffall)

        diffvar = []
        for rows in matrixDifference:
            for fields in rows:
                if fields != 0:
                    varient = (fields - diffmean)**2
                    diffvar.append(varient)
        diffstddev = (sum(diffvar)/len(diffvar))**(1/2)
        matrixZ = [[0 for i in range(5120)] for j in range(6240)]
        for rows in range(6240):
            for fields in range(5120):
                if matrixDifference[rows][fields] != 0:
                    zscore = (matrixDifference[rows][fields] - diffmean)/diffstddev
                    matrixZ[rows][fields] = zscore

        print("max =" , maxium)
        print("mean =" , diffmean)
        print("stddev =" , diffstddev)
        k = "populationdiffZ_" + str(n+1) +"BW"
        drawmap(matrixZ,k,5)


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
#max = 5000 #mean = 4.255880032562949 #stddev = 115.3959255638346

#max = 4580 #mean = 1.6954440902304184 #stddev = 94.6641438639075

#max = 6721 #mean = 0.578827872300598 #stddev = 78.28886461440672

#max = 4279 #mean = -1.935201907681552 #stddev = 69.8525677327891

    print("#####################\nPart 2.5 program END. \n#####################")
