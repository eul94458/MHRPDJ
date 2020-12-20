print("start")

import metadata
from PIL import Image, ImageDraw
import numpy

def output_graph(list):
    #temp = numpy.genfromtxt(g, delimiter = ',', autostrip=True,)
    temp = numpy.array(list)
    im = Image.fromarray(temp,"RGB")
    pix = im.load()
    #rows, cols = im.size
    height = len(graph)
    width = len(graph[0])
    for x in range(width):
        for y in range(height):
            #print(str(x) + " " + str(y))

            if temp[y,x] == 0:
                pix[x,y] = (256,256,256)
            else:
                #pix[x-1,y-1] = (0,0,0)
                #pix[x-1,y] = (0,0,0)
                #pix[x-1,y+1] = (0,0,0)
                #pix[x,y-1] = (0,0,0)
                pix[x,y] = (0,0,0)
                #pix[x,y+1] = (0,0,0)
                #pix[x+1,y-1] = (0,0,0)
                #pix[x+1,y] = (0,0,0)
                #pix[x+1,y+1] = (0,0,0)
    im.save("thresholdtest" + '.tif')

def cal_distance():
    templist = [int(0) for width in range(561)]
    for q in range(0,250,step):
        for w in range(0,250,step):
            for p in range(250,500,step):
                for o in range(0,250,step):                
                    x1,y1 = (q,w)
                    x2,y2 = (p,o)
                    magnitude = round(( (y2-y1)**2 + (x2-x1)**2 )**(1/2))
                    templist[magnitude] += 1
    return templist
                



query = input("Type any thing to start")

if query != "quit" :
    step = 1
    print("1",end=(""))
    print("1",end=(""))
    print("1",end=(""))
    
    resultlist = cal_distance()


    print("2",end=(""))
    print(len(resultlist))

    with open("thresholdtest.csv","w") as output_file:
        for i,z in enumerate(resultlist):
            output_file.write(str(i))
            output_file.write(",")
            output_file.write(str(z))
            output_file.write("\n")

    print("4",end=(""))

    print("Map is output")





