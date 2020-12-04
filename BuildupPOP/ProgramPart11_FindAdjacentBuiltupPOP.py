print("#####################\nPart 11 program START.\n#####################")

import metadata

valid_Lv1meshID = metadata.call_populated_lv1mesh()

def check_adjacent_mesh(currentMeshID,CellPosition):
    currentMeshID = int(currentMeshID)

    # 1.1 upper left
    if CellPosition == "upperleft":
        adjacentMesh = [str(currentMeshID+99),str(currentMeshID+100),str(currentMeshID-1)]
    # 1.2 upper right
    elif CellPosition == "upperright":
        adjacentMesh = [str(currentMeshID+100),str(currentMeshID+101),str(currentMeshID+1)]
    # 1.3 bottom left
    elif CellPosition == "bottomleft":
        adjacentMesh = [str(currentMeshID-1),str(currentMeshID-101),str(currentMeshID-100)]
    # 1.4 bottom right
    elif CellPosition == "bottomright":
        adjacentMesh = [str(currentMeshID+1),str(currentMeshID-100),str(currentMeshID-99)]
    # 2. edge
    # 2.1 top
    elif CellPosition == "top":
        adjacentMesh = [str(currentMeshID+100)]
    # 2.2 bottom
    elif CellPosition == "bottom":
        adjacentMesh = [str(currentMeshID-100)]
    # 2.3 left
    elif CellPosition == "left":
        adjacentMesh = [str(currentMeshID-1)]
    # 2.4 right
    elif CellPosition == "right":
        adjacentMesh = [str(currentMeshID+1)]

    return adjacentMesh

def check_position_validadjacentmesh(determinant):
    #########################################
    # x+99  x+100  x+101
    # x-1    {x}   x+1
    # x-101 x-100  x-99
    if determinant == 99: #upperleft
        MeshPosition = "upperleft"
    elif determinant == 100: #top
        MeshPosition = "top"
    elif determinant == 101: #upperright
        MeshPosition = "upperright"
    elif determinant == -1: #left
        MeshPosition = "left"
    elif determinant == 1: #right
        MeshPosition = "right"
    elif determinant == -101: #bottomleft
        MeshPosition = "bottomleft"
    elif determinant == -100: #bottom
        MeshPosition = "bottom"
    elif determinant == -99: #bottomright
        MeshPosition = "bottomright"
    return MeshPosition

def check_adjacent_cellinfo(CellPosition,adjacentMeshPosition,CellY,CellX):

    global Position

    if CellPosition == "upperleft":
        if adjacentMeshPosition == "upperleft":
            Position = ["799_799"]
        elif adjacentMeshPosition == "top":
            Position = ["799_0","799_1"]
        elif adjacentMeshPosition == "left":
            Position = ["0_799","1_799"]

    elif CellPosition == "upperright":
        if adjacentMeshPosition == "top":
            Position = ["799_798","799_799"]
        elif adjacentMeshPosition == "upperright":
            Position = ["799_0"]
        elif adjacentMeshPosition == "right":
            Position = ["0_0","1_0"]

    elif CellPosition == "bottomleft":
        if adjacentMeshPosition == "left":
            Position = ["798_799","799_799"]
        elif adjacentMeshPosition == "bottomleft":
            Position = ["0_799"]
        elif adjacentMeshPosition == "bottom":
            Position = ["0_0","0_1"]

    elif CellPosition == "bottomright":
        if adjacentMeshPosition == "right":
            Position = ["798_0","799_0"]
        elif adjacentMeshPosition == "bottom":
            Position = ["0_798","0_799"]
        elif adjacentMeshPosition == "bottomright":
            Position = ["0_0"]

    elif adjacentMeshPosition == "top":
        one = str(799)+"_"+str(CellX - 1)
        two = str(799)+"_"+str(CellX)
        three = str(799)+"_"+str(CellX + 1)
        Position = [one,two,three]
    elif adjacentMeshPosition == "bottom":
        one = str(0)+"_"+str(CellX - 1)
        two = str(0)+"_"+str(CellX)
        three = str(0)+"_"+str(CellX + 1)
        Position = [one,two,three]
    elif adjacentMeshPosition == "left":
        one = str(CellY - 1)+"_"+str(799)
        two = str(CellY)+"_"+str(799)
        three = str(CellY + 1)+"_"+str(799)
        Position = [one,two,three]
    elif adjacentMeshPosition == "right":
        one = str(CellY - 1)+"_"+str(0)
        two = str(CellY)+"_"+str(0)
        three = str(CellY + 1)+"_"+str(0)
        Position = [one,two,three]

    return Position

def check_validity(targetlist,check_from):

    checkkkresult = []

    for (i,target) in enumerate(targetlist):
        if check_from.count(target) > 0 : # if list_check_from contains target, we made it!
            checkkkresult.append([target,1])
        else:
            checkkkresult.append([target,0])
    #print(result)
    return checkkkresult

def check_validity2(result):
    # this function is used to check
    # whether one list contain element on another list
    # this is use after check_validity
    # as the result of previous function = [ [a,0],[b,1],[c,1] ]
    # it is more convient to have a function to check whether "1" == result[n][1]

    ValidiyCodeOfResult = []

    for (i,EachSET) in enumerate(result):
        ValidiyCodeOfResult.append(EachSET[1])
        # so we obtain ValidiyCodeOfResult = [1,1,0,0,1]
        # all we need is to count 1 in this list
    if ValidiyCodeOfResult.count(1) == 0:
        return 0 # means there is no "1"
    else:
        return 1 # means there has "1"

if __name__ == "__main__":

    MarginalAggloDATA = []

    with open("data/step10_marginal_builtuppop/marginal_builtuppop.csv", "r" , encoding="utf-8") as input_file:
        for line in input_file:
            NewLine = line.strip()
            #NewLine = NewLine[:-1]
            NewLine = NewLine.strip().split(",")
            MarginalAggloDATA.append(NewLine)

    adjacent_agglomerations = []

    MarginalAggloLIST = []

    # 4.0 make a marginal_cell_list for confirmation
    for EachAggloDATA in MarginalAggloDATA:

        MarginalcellLIST = []

        AggloINFO = EachAggloDATA[0].split("_")
        MeshID,AggloID = AggloINFO[0],AggloINFO[1]

        MarginalcellLIST.append(MeshID)
        MarginalcellLIST.append(AggloID)

        CellINFO = EachAggloDATA[1:]

        for CellINDEX in range(len(CellINFO)):

            CellID = CellINFO[CellINDEX].split("_")
            #print(cell_position)
            cellY = int(CellID[1])
            cellX = int(CellID[2])
            cell_coordinate = str(cellY)+"_"+str(cellX)

            MarginalcellLIST.append(cell_coordinate)
            #MarginalcellLIST = [ meshID, aggloID, y_x, y_x, y_x, ... ]

        MarginalAggloLIST.append(MarginalcellLIST)
        #MarginalAggloLIST = [[ meshID, aggloID, y_x, y_x, y_x, ... ],
        #                     [ meshID, aggloID, y_x, y_x, y_x, ... ],
        #                     [ meshID, aggloID, y_x, y_x, y_x, ... ] ]


    # 4.1 Extract marginal cell information from marginal_agglomerations
    for EachAggloDATA in MarginalAggloDATA:

        AggloINFO = EachAggloDATA[0].split("_")
        MeshID,AggloID = AggloINFO[0],AggloINFO[1]

        MarginalCellINFO = EachAggloDATA[1:]

        cell_need_to_check = [] # of this Marginal Agglomeration

        for EachMarginalCell in MarginalCellINFO:

            CellINFO = EachMarginalCell.split("_")
            CellPosition = CellINFO[0]
            CellY = int(CellINFO[1])
            CellX = int(CellINFO[2])

            adjacentMesh = check_adjacent_mesh(MeshID,CellPosition)
            ValidadjacentMesh = check_validity(adjacentMesh,valid_Lv1meshID)
            NumberOfValidadjacentMesh = 0

            for i in range(len(ValidadjacentMesh)):
                if ValidadjacentMesh[i][1] == 1:
                    NumberOfValidadjacentMesh += 1

            if NumberOfValidadjacentMesh > 0:
                for adjacentMeshID in ValidadjacentMesh:

                    AdjMeshID = adjacentMeshID[0]
                    Determinant = int(AdjMeshID) - int(MeshID)
                    adjacentMeshPosition = check_position_validadjacentmesh(Determinant)
                    adjacentCellPosition = check_adjacent_cellinfo(CellPosition,adjacentMeshPosition,CellY,CellX)
                    adjacentCellPosition.insert(0,AdjMeshID)
                    
                    #print("0\t", EachAggloDATA[0], CellPosition)            
                    #print("1\t", adjacentMeshID, adjacentMeshPosition,"\n")

                    #  adjacentCellPosition = [adjmeshID,one,two,three]
                    buffer = adjacentCellPosition[:]

                    cell_need_to_check.append(buffer)
        #            if (['5134', '5133', '0_318', '0_319'] in cell_need_to_check) == True:
        #                break
        #        if (['5134', '5133', '0_318', '0_319'] in cell_need_to_check) == True:
        #                break
        #    if (['5134', '5133', '0_318', '0_319'] in cell_need_to_check) == True:
        #                break
        #if (['5134', '5133', '0_318', '0_319'] in cell_need_to_check) == True:
        #                break
                        
        #if str(AggloINFO) == "5233_0" or str(AggloINFO) == "5134_3":
        #    print(cell_need_to_check)
        #if str(MeshID) == str(5233) and str(AggloID) == str(0):
        #    print(MeshID,cell_need_to_check)
        #if str(MeshID) == str(5134) and str(AggloID) == str(3):
        #    print(MeshID,cell_need_to_check)
        
        
        # for one Marginal Agglomeration , its adjacent Cells are all in cell_need_to_check[]

          # here we finished extracting adjacent_meshID and adjacent_cellID
          # so we cango next step, to check whether the adjacentcell is present
    # 4.7 Check whether adjacent cell is really present
          # structure of cell_need_to_check[] is like:
          # because there may be several adjacent mesh present e.g. for the cell at corner,
          # so it is a 2 dimension cell
          # cell_need_to_check[] = [ [adjmeshID1,YX,YX,YX],
          #                          [adjmeshID2,YX,YX,YX],
          #                          [adjmeshID3,YX,YX,YX], ... ]
          #
          # check whether the adjacent cell is in marginal_cell_list[]
          # MarginalAggloLIST = [ [meshID,aggloID,YX,YX],
          #                       [meshID,aggloID,YX,YX,YX,YX],
          #                       [meshID,aggloID,YX,YX,YX,YX],
          #                       [meshID,aggloID,YX,YX,YX,YX], ... ]
          #
          # we can first scan for the meshID
          # then we found the certain meshID, and start to scan for the adjacent cellID
          # maybe use list.count
          # for this way, we need to set a parameter to check if the process is skipped due to absent of adjacent cell
          # finally, if the adjacent cell is present, mark it down

        for row2 in cell_need_to_check:
            meshID_2 = row2[0]
            temp_result = []

            for (i,row1) in enumerate(MarginalAggloLIST):
                # callout row of MarginalAggloLIST
                # check whether the adjmeshID is present in certain row

                meshID_1 = row1[0]
                aggloID_1 = row1[1]
                connection = 0

                if int(meshID_2) == int(meshID_1):
                    for n in range(len(row2)-1):
                         if row1.count(row2[n+1]) > 0:
                            connection += 1
                            break
            #print("A",str(connection))

                if connection >= 1:
                    temp_result.append(str(MeshID)+"_"+str(AggloID))
                    temp_result.append(str(meshID_1)+"_"+str(aggloID_1))
                    #print("before", str(temp_result))
                    temp_result.sort(reverse=True)
                    #print("after", str(temp_result))

                    existence_checker = -1

                    # existence checker
                    #print("B",str(adjacent_agglomerations.count(temp_result)))

                    if adjacent_agglomerations.count(temp_result) >= 1:
                        existence_checker = 1
                        #print("Data is already in the list !")

                    else:
                        existence_checker = 0
                        #print("Discovery of inter-mesh agglomeration !")


                    if (existence_checker == 0) or (existence_checker == -1) :
                        #print("C",str(existence_checker))
                        #print("Discovery of inter-mesh agglomeration !")
                        #print(temp_result)

                        adjacent_agglomerations.append(temp_result)
                        existence_checker = -1

        # here we should finished all scanning process
        # we can output our result

        #print(len(adajcent_agglomerations))
        #for i in range(10):
        #    print(adajcent_agglomerations[i])

    filename = "data/step11_adjacent_builtuppop/adjacent_builtuppop.csv"
    metadata.writeout(adjacent_agglomerations,filename)
    
    #with open("data/step11_adjacent_builtuppop/adjacent_builtuppop.csv" , "w") as output_file:
    #    for each_row in adjacent_agglomerations:
    #        for each_field in each_row:
    #            output_file.write(str(each_field)+",")
    #        output_file.write("\n")

    print("#####################\nPart 11 program END.\n#####################")

