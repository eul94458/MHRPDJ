print("#####################\nPart 15 program START.\n#####################")

def find_deltainlist(listname):
    listname.sort()
    smallestnumber = int(listname[0])
    listname.sort(reverse=True)
    largestnumber = int(listname[0])
    
    delta = abs(smallestnumber - largestnumber)
    return delta
    

def trim_validlist(listname):
    qR = 0
    
     

import metadata
from PIL import Image, ImageDraw
import numpy

valid_Lv1meshID = metadata.call_populated_lv1mesh()

if __name__ == "__main__":

    while True:
        query = input("Please input the Global Agglomeration's ID the you are interested in : ")
        
        if query != int:
        
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
                       
            print(1,end="")
            
            QuestedGlobalAggloINFO = QuestedGlobalAggloINFO[2:]
            
            MeshIDs = []            
            for items in QuestedGlobalAggloMesh:
                MeshIDs.append([items])            
            
            print(2,end="")
            
            for element in QuestedGlobalAggloINFO:
                for (index,everyMeshID) in enumerate(MeshIDs):
                    if str(everyMeshID[0]) == str(element[:4]):
                        newAggloID = element[5:element.index("_",5)]
                        MeshIDs[index].append(newAggloID)
            
            # MeshIDs = [ [ meshID_1, AggloID, AggloID, AggloID ],
            #             [ meshID_2, AggloID, AggloID, AggloID ],
            #             [ meshID_3, AggloID, AggloID, AggloID ] ]
            
            #CellsCount = 0
            
            print(3,end="")
            
            for eachMeshDATAs in MeshIDs:
            
                print(4,end="")
                
                meshID = eachMeshDATAs[0]
                AggloIDS = eachMeshDATAs[1:]
                
                print(5,end="")
                
                #####################
                cellNoConverter = []
                                
                for lv1Y in range(7,-1,-1):          
                    for Lv2Y in range(9,-1,-1):     
                        for Lv3Y in range(9,-1,-1):
                            
                            bufferrow = []
                            for Lv1X in range(0,8,+1):
                                for Lv2X in range(0,10,+1):
                                    for Lv3X in range(0,10,+1):
                                        buffercell = int(meshID)*1000000+ lv1Y*100000+ Lv1X*10000+ Lv2Y*1000+ Lv2X*100+ Lv3Y*10+ Lv3X*1
                                        bufferrow.append(str(buffercell))
                                        #if buffercell == 5339779999:
                                        #    print(lv1Y,Lv1X,Lv2Y,Lv2X,Lv3Y,Lv3X)
                                        #    break
                            cellNoConverter.append(bufferrow)
                    cellNoConverter.append(bufferrow)
                ######################
                
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
                
                ####################
                matrix = [[0 for i in range(800)] for j in range(800)]
                
                for eachAggloDATA in NeededDATA:
                    cellDATAs = eachAggloDATA[2:]
                    
                    for eachCell in cellDATAs:
                        CellINFO = eachCell.split("_")
                        meshID = int(CellINFO[0])
                        cellY = int(CellINFO[1])
                        cellX = int(CellINFO[2])
                        cellPopulation = float(CellINFO[3])    
                        
                        matrix[cellY][cellX] = cellPopulation
                ####################

                finalCSV = []
                for Y in range(800):
                    for X in range(800):
                        A = int(cellNoConverter[Y][X])
                        B = float(matrix[Y][X])
                        if B != 0:
                            finalCSV.append([A,B])
                
                        
                filename = "data/step15_GISBuiltupPOP/"+str(GlobalAggloID)+"_"+str(meshID)+"_builtuppop.csv"
                metadata.writeout(finalCSV,filename)
        
        elif query == "quit":
            break




    print("#####################\nPart 15 program END.\n#####################")

