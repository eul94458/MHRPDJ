print("#####################\nPart 16 program START.\n#####################")
import math
import metadata
from PIL import Image, ImageDraw
import numpy

def check_cell_position(YX,h,w):
    (y,x) = YX
    h -= 1
    w -=1
    #print("y=",y,"\t","x=",x)

    if y ==0 and x == 0:
        return "upper_left"
    elif y ==0 and x == w:
        return "upper_right"
    elif y ==h and x == 0:
        return "bottom_left"
    elif y ==h and x == w:
        return "bottom_right"
    elif y ==0 and ( x !=0 and x !=w):
        return "top"
    elif y ==h and ( x !=0 and x !=w):
        return "bottom"
    elif ( y !=0 and y != h ) and x == 0:
        return "left"
    elif ( y !=0 and y != h ) and x == w:
        return "right"
    elif ( y !=0 and y != h ) and ( x !=0 and x !=w):
        return "normal"

def check_adjacent_cell(cellYX,cell_position):
    (y,x) = cellYX
    #print("y=",y,"\t","x=",x,"\t",cell_position)
    AdjacentCellLIST = []

    if cell_position == "upper_left":
        AdjacentCellLIST = [(1,y,x+1),(1,y+1,x),(2,y+1,x+1)]
    elif cell_position == "upper_right":
        AdjacentCellLIST = [(1,y,x-1),(2,y+1,x-1),(1,y+1,x)]
    elif cell_position == "bottom_left":
        AdjacentCellLIST = [(1,y-1,x),(2,y-1,x+1),(1,y,x+1)]
    elif cell_position == "bottom_right":
        AdjacentCellLIST = [(2,y-1,x-1),(1,y-1,x),(1,y,x-1)]
    elif cell_position == "top":
        AdjacentCellLIST = [(1,y,x-1),(1,y,x+1),(2,y+1,x-1),(1,y+1,x),(2,y+1,x+1)]
    elif cell_position == "bottom":
        AdjacentCellLIST = [(2,y-1,x-1),(1,y-1,x),(2,y-1,x+1),(1,y,x-1),(1,y,x+1)]
    elif cell_position == "left":
        AdjacentCellLIST = [(1,y-1,x),(2,y-1,x+1),(1,y,x+1),(1,y+1,x),(2,y+1,x+1)]
    elif cell_position == "right":
        AdjacentCellLIST = [(2,y-1,x-1),(1,y-1,x),(1,y,x-1),(2,y+1,x-1),(1,y+1,x)]
    elif cell_position == "normal":
        AdjacentCellLIST = [(2,y-1,x-1),(1,y-1,x),(2,y-1,x+1),(1,y,x-1),(1,y,x+1),(2,y+1,x-1),(1,y+1,x),(2,y+1,x+1)]

    return AdjacentCellLIST

def drawmap(listname,filename):
    maxlist = []
    for row in listname:
        buffer = max(row)
        maxlist.append(buffer)
    maxium = max(maxlist)
    print(maxium)

    temp = numpy.array(listname)
    im = Image.fromarray(temp,"RGB")
    pix = im.load()
    width = len(listname[0])
    height = len(listname)
    for x in range(width):
        for y in range(height):
            #print(str(x) + " " + str(y))

            if temp[y,x] == 0:
                pix[x,y] = (255,255,255)
            elif temp[y,x] <= 3:
                pix[x,y] = (223,223,223)
            else:
                pix[x,y] = (0,0,0)

            #else:
            #    pix[x,y] = (int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*temp[y,x]))))),
            #                int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*temp[y,x]))))),
            #                int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*temp[y,x]))))))
            # (R,G,B)
            #要用顏色深淺黎表達人口密度
            #人口密度上限係10000
            #先將10000除256 得出256階linear色階

            #logistic-0009
            #g(x)=255-(255)/(1+6.96875e^(-(0.0009*x)))
            #g(0)=32 , b = 0.0009

            #logistic-0.0030937483
            #h(x)=255-(255)/(1+6.96875e^(-(0.0030937483*x)))
            #h(0)=32 , b = 0.0030937483

            #logistic-0.01933592691
            #m(x)=255-(255)/(1+6.96875e^(-(0.01933592691*x)))
            #m(0)=32 , b = 0.01933592691

            #linear
            #f(x)=255-( (223/1000)*x +32)

            #m = (ln(128/6.96875(255-128)))/100
            #int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*temp[y,x])))))
            # f(3) = 128
    im.save("data/step16_1stderivativeBuiltupPOP/"+str(filename) + '.tif')

def drawmap_logistic(listname,filename):
    maxlist = []
    for row in listname:
        buffer = max(row)
        maxlist.append(buffer)
    maxium = max(maxlist)
    print(maxium)

    temp = numpy.array(listname)
    im = Image.fromarray(temp,"RGB")
    pix = im.load()
    width = len(listname[0])
    height = len(listname)
    for x in range(width):
        for y in range(height):
            #print(str(x) + " " + str(y))

            if temp[y,x] == 0:
                pix[x,y] = (255,255,255)
            else:
                pix[x,y] = (int(round(255-(255)/(1+6.96875*math.e**(-(0.01933592691*temp[y,x]))))),
                            int(round(255-(255)/(1+6.96875*math.e**(-(0.01933592691*temp[y,x]))))),
                            int(round(255-(255)/(1+6.96875*math.e**(-(0.01933592691*temp[y,x]))))))
            # (R,G,B)
            #要用顏色深淺黎表達人口密度
            #人口密度上限係10000
            #先將10000除256 得出256階linear色階

            #logistic-0009
            #g(x)=255-(255)/(1+6.96875e^(-(0.0009*x)))
            #g(0)=32 , b = 0.0009

            #logistic-0.0030937483
            #h(x)=255-(255)/(1+6.96875e^(-(0.0030937483*x)))
            #h(0)=32 , b = 0.0030937483 , h(625)=128

            #logistic-0.01933592691
            #m(x)=255-(255)/(1+6.96875e^(-(0.01933592691*x)))
            #m(0)=32 , b = 0.01933592691 , m(100)=128

            #linear
            #f(x)=255-( (223/1000)*x +32)

            #m = (ln(128/6.96875(255-128)))/100
            #int(round(255-(255)/(1+6.96875*math.e**(-(0.6445308971*temp[y,x])))))
            # f(3)=128
    im.save("data/step16_1stderivativeBuiltupPOP/"+str(filename) + '.tif')

def find_deltainlist(listname):
    listname.sort()
    smallestnumber = int(listname[0])
    listname.sort(reverse=True)
    largestnumber = int(listname[0])

    delta = abs(smallestnumber - largestnumber)
    return delta

def gen_scale():
    scale = []
    for i in range(256):
        gradiant = i
        scale.append([gradiant])

    temp = numpy.array(scale)
    im = Image.fromarray(temp,"RGB")
    pix = im.load()
    #rows, cols = im.size
    height = len(scale)
    width = 1
    for x in range(width):
        for y in range(height):
            if temp[y,x] == 0:
                pix[x,y] = (255,255,255)
            else:
                pix[x,y] = (255-temp[y,x],255-temp[y,x],255-temp[y,x])

    im.save("data/step16_1stderivativeBuiltupPOP/grayscale.tif")
    print("Scale is output")


valid_Lv1meshID = metadata.call_populated_lv1mesh()

if __name__ == "__main__":

    while True:
        query = input("Please input the Global Agglomeration's ID the you are interested in : ")

        if query != int:
            #gen_scale()

            GlobalAggloID = int(query)

            bigpicture = []
            with open("data/step13_bigpicture_builtuppop/bigpicture_builtuppop.csv" , "r" , encoding="utf-8") as input_file:
                for line in input_file:
                    NewLine = line.strip()
                    #NewLine = NewLine[:-1]
                    NewLine = NewLine.strip().split(",")
                    bigpicture.append(NewLine)

            QuestedGlobalAggloINFO = bigpicture[GlobalAggloID]

            QuestedGlobalAggloPopulation = QuestedGlobalAggloINFO[1]

            QuestedGlobalAggloMesh = set()

            for length in range(len(QuestedGlobalAggloINFO)-2):
                QuestedGlobalAggloMesh.add(QuestedGlobalAggloINFO[length+2][:4])

            print("Global Agglomeration you selected is located in mesh\n",
                    QuestedGlobalAggloMesh ,"\n",
                    "with total population of", float(QuestedGlobalAggloPopulation),".")

            tempMeshIDY = set()
            tempMeshIDX = set()
            for items in QuestedGlobalAggloMesh:
                Y = int(items[:2])
                tempMeshIDY.add(Y)
                X = int(items[2:])
                tempMeshIDX.add(X)
            MeshIDY = []
            MeshIDX = []
            for items in tempMeshIDY:
                MeshIDY.append(items)
            for items in tempMeshIDX:
                MeshIDX.append(items)
            MeshHeight = find_deltainlist(MeshIDY) + 1
            MeshWidth = find_deltainlist(MeshIDX) + 1
            matrix = [[0 for i in range(800*MeshWidth)] for j in range(800*MeshHeight)]
            MeshIDY.sort(reverse=True)
            MeshIDX.sort()
            # so we created a matrix that is big enough
            # lets pour all data into it

            QuestedGlobalAggloINFO = QuestedGlobalAggloINFO[2:]

            MeshIDs = []
            for items in QuestedGlobalAggloMesh:
                MeshIDs.append([items])

            for element in QuestedGlobalAggloINFO:
                for (index,everyMeshID) in enumerate(MeshIDs):
                    if str(everyMeshID[0]) == str(element[:4]):
                        newAggloID = element[5:element.index("_",5)]
                        MeshIDs[index].append(newAggloID)

            # MeshIDs = [ [ meshID_1, AggloID, AggloID, AggloID ],
            #             [ meshID_2, AggloID, AggloID, AggloID ],
            #             [ meshID_3, AggloID, AggloID, AggloID ] ]

            #CellsCount = 0

            for eachMeshDATAs in MeshIDs:

                meshID = eachMeshDATAs[0]
                AggloIDS = eachMeshDATAs[1:]

                RegionalAggloDATAs = []

                with open("data/step9_regional_builtuppop/regional_builtuppop_sorted_"+str(meshID)+".csv" , "r" , encoding="utf-8") as input_file:
                    for line in input_file:
                        NewLine = line.strip()
                        #NewLine = NewLine[:-1]
                        NewLine = NewLine.strip().split(",")
                        RegionalAggloDATAs.append(NewLine)

                NeededDATA = []

                for eachAggloID in AggloIDS:
                    buffer = RegionalAggloDATAs[int(eachAggloID)]
                    NeededDATA.append(buffer)

                # NeededDATA = [ [ AggloID_1, cellID, cellID, cellID ],
                #                [ AggloID_2, cellID, cellID, cellID ],
                #                [ AggloID_3, cellID, cellID, cellID ] ]

                OffsetY = abs(int(MeshIDY[0]) - int(meshID[:2]))
                OffsetX = abs(int(meshID[2:]) - int(MeshIDX[0]))

                for eachAggloDATA in NeededDATA:
                    cellDATAs = eachAggloDATA[2:]

                    for eachCell in cellDATAs:
                        CellINFO = eachCell.split("_")
                        meshID = int(CellINFO[0])
                        cellY = int(CellINFO[1]) + 800*OffsetY
                        cellX = int(CellINFO[2]) + 800*OffsetX
                        cellPopulation = float(CellINFO[3])

                        matrix[cellY][cellX] = cellPopulation
                        #CellsCount += 1


            # First trim height
            Ysumpop = []
            for rows in matrix:
                rowpop = sum(rows)
                Ysumpop.append(rowpop)
            #Ysumpop = [0,0,0,0,123,1515,6367,52,12,0,0,0,0]
            YLeadingZero = 0
            YFollowingZero = 0
            stopper = -1
            n = 0
            while stopper != 1:
                if Ysumpop[n] == 0:
                    n += 1
                elif Ysumpop[n] != 0:
                    stopper = 1
                    YLeadingZero = n
            stopper = -1
            n = -1
            while stopper != 1:
                if Ysumpop[n] == 0:
                    n -= 1
                elif Ysumpop[n] != 0:
                    stopper = 1
                    YFollowingZero = n

            trimedmatrix = matrix[YLeadingZero+1:YFollowingZero+1]

            # Second trim width
            XLeadingZero = []
            XFollowingZero = []

            for (y,rows) in enumerate(trimedmatrix):
                stopper = -1
                n = 0
                while stopper != 1:
                    if rows[n] == 0:
                        n += 1
                    elif rows[n] != 0:
                        stopper = 1
                        tempnum = n
                        XLeadingZero.append(tempnum)
                stopper = -1
                n = -1
                while stopper != 1:
                    if rows[n] == 0:
                        n -= 1
                    elif rows[n] != 0:
                        stopper = 1
                        tempnum = n
                        XFollowingZero.append(tempnum)
            for y in range(len(trimedmatrix)):
                trimedmatrix[y] = trimedmatrix[y][min(XLeadingZero)+1:max(XFollowingZero)+1]

            height = len(trimedmatrix)
            width = len(trimedmatrix[0])

            matrixslopezmax = [[0 for i in range(width)] for j in range(height)]
            matrixslopemean = [[0 for i in range(width)] for j in range(height)]

            slopeinventory = []
            for Y in range(height):
                for X in range(width):
                    if trimedmatrix[Y][X] != 0:
                        CellYX = (Y,X)
                        CellPosition = check_cell_position(CellYX,height,width)
                        ValidAdjacentCell = check_adjacent_cell(CellYX,CellPosition)
                        localslopemeanlist = []
                        for adjacentcellID in ValidAdjacentCell:
                            (tpe,adjY,adjX) = adjacentcellID
                            if trimedmatrix[adjY][adjX] != 0:
                                denominator = 1
                                if tpe == 2:
                                    denominator = 1.41421
                                partialslope = abs(trimedmatrix[adjY][adjX]-trimedmatrix[Y][X])/denominator
                                slopeinventory.append(partialslope)
                                localslopemeanlist.append(partialslope)

                        localslopemean = sum(localslopemeanlist)/len(localslopemeanlist)
                        matrixslopemean[Y][X] = localslopemean

            numofslope = len(slopeinventory)
            slopemean = sum(slopeinventory)/numofslope
            slopevar = 0
            for eachslopt in slopeinventory:
                valuebuffer = (eachslopt-slopemean)**2
                slopevar += valuebuffer
            slopestddev = (slopevar/numofslope)**(1/2)
            print(slopestddev)

            globalzscore = []
            for Y in range(height):
                for X in range(width):
                    if trimedmatrix[Y][X] != 0:
                        CellYX = (Y,X)
                        CellPosition = check_cell_position(CellYX,height,width)
                        ValidAdjacentCell = check_adjacent_cell(CellYX,CellPosition)
                        localzscore = set()
                        for adjacentcellID in ValidAdjacentCell:
                            (tpe,adjY,adjX) = adjacentcellID
                            if trimedmatrix[adjY][adjX] != 0:
                                denominator = 1
                                if tpe == 2:
                                    denominator = 1.41421
                                partialslope = abs(trimedmatrix[adjY][adjX]-trimedmatrix[Y][X])/denominator
                                zscore = round(partialslope/slopestddev,1)
                                localzscore.add(zscore)
                                globalzscore.append(zscore)
                        zmax = max(localzscore)
                        matrixslopezmax[Y][X] = zmax

            sparezscoreinventory = globalzscore[:]
            sparezscoreinventory.sort()
            newzscoreinventory = []
            storedlist = []
            for item in sparezscoreinventory:
                if (item in storedlist) == False :
                    buffer = item
                    quantity = sparezscoreinventory.count(buffer)
                    newzscoreinventory.append([buffer,quantity])
                    storedlist.append(buffer)

            filename = "data/step16_1stderivativeBuiltupPOP/GlobalAggloID_"+str(GlobalAggloID)+"_slopeinventory.csv"
            metadata.writeout(newzscoreinventory,filename)

            filenameslopezmax = "GlobalAggloID_" + str(GlobalAggloID) + "_slopezmax"
            drawmap(matrixslopezmax,filenameslopezmax)

            filenameslopemean = "GlobalAggloID_" + str(GlobalAggloID) + "_slopemean"
            drawmap_logistic(matrixslopemean,filenameslopemean)

        elif query == "quit":
            break




    print("#####################\nPart 16 program END.\n#####################")

