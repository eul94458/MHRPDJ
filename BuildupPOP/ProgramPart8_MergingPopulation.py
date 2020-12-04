print("#####################\nPart 8 program START.\n#####################")

import metadata

valid_Lv1meshID = metadata.call_populated_lv1mesh()

if __name__ == "__main__":

    for meshID in valid_Lv1meshID:

    #while True:
        #meshID = input("Please Enter a Valid Lv1 MeshID : ")
        #if meshID == "exit" :
        #    break
        #else :
        BuiltupMap = metadata.call_landuse_distribution_map(meshID)
        PopMap = metadata.call_population_distribution_map(meshID)

        PopulationAssignedBuiltupMatrix = [[0 for i in range(800)] for j in range(800)]

        #count = 0
        for PopCoorY in range(160):

            for PopCoorX in range(160):
                #this is for PopMap
                # 4 quadrant as one unit
                # Q2pop Q1pop
                # Q3pop Q4pop
                Q2pop = int(PopMap[PopCoorY*2+0][PopCoorX*2+0])
                Q1pop = int(PopMap[PopCoorY*2+0][PopCoorX*2+1])
                Q3pop = int(PopMap[PopCoorY*2+1][PopCoorX*2+0])
                Q4pop = int(PopMap[PopCoorY*2+1][PopCoorX*2+1])
                tempPop = [[Q2pop,Q1pop],[Q3pop,Q4pop]]

                BuiltupOrNotInformation = [[0,0],[0,0]]
                # keep log in this format
                # Q2 Q1
                # Q3 Q4
                
                # first check for whole cell
                for BuiltupY in range(2):
                    for BuiltupX in range(2):
                        for LocalY in range(2):
                            for LocalX in range(2):
                                if int(BuiltupMap[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+3*BuiltupX+LocalX]) == 700:
                                    BuiltupOrNotInformation[BuiltupY][BuiltupX] += 1

                # second check for half cell
                for BuiltupY in range(2):
                        for LocalY in range(2):
                                if int(BuiltupMap[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+2]) == 700:
                                    BuiltupOrNotInformation[BuiltupY][0] += 0.5
                                    BuiltupOrNotInformation[BuiltupY][1] += 0.5
                for BuiltupX in range(2):
                        for LocalX in range(2):
                                if int(BuiltupMap[PopCoorY*5+2][PopCoorX*5+3*BuiltupX+LocalX]) == 700:
                                    BuiltupOrNotInformation[0][BuiltupX] += 0.5
                                    BuiltupOrNotInformation[1][BuiltupX] += 0.5

                # third check for quater cell
                if int(BuiltupMap[PopCoorY*5+2][PopCoorX*5+2]) == 700:
                    for BuiltupY in range(2):
                        for BuiltupX in range(2):
                            BuiltupOrNotInformation[BuiltupY][BuiltupX] += 0.25

                # case1, ppl!=0 and builtup!=0
                # normal

                # case2, ppl==0 and builtup!=0
                # count as 0 ppl

                # case3, ppl!=0 and builtup==0
                # n / zero = fail
                # spread possibility to all cells

                # case2, ppl==0 and builtup==0
                # all zero
                
                # check validity
                totalpopadd = 0
                
                # first assign for whole cell
                for BuiltupY in range(2):
                    for BuiltupX in range(2):
                        # for populated empty area
                        if tempPop[BuiltupY][BuiltupX] != 0 and BuiltupOrNotInformation[BuiltupY][BuiltupX] ==0:
                            for LocalY in range(2):
                                for LocalX in range(2):
                                    Value = (tempPop[BuiltupY][BuiltupX]/6.25)*1
                                    PopulationAssignedBuiltupMatrix[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+3*BuiltupX+LocalX] = Value
                                    totalpopadd += Value
                        # for populated builtup area
                        elif tempPop[BuiltupY][BuiltupX] != 0 and BuiltupOrNotInformation[BuiltupY][BuiltupX] !=0:
                            for LocalY in range(2):
                                for LocalX in range(2):
                                    if int(BuiltupMap[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+3*BuiltupX+LocalX]) == 700:
                                        Value = (tempPop[BuiltupY][BuiltupX]/BuiltupOrNotInformation[BuiltupY][BuiltupX])*1
                                        PopulationAssignedBuiltupMatrix[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+3*BuiltupX+LocalX] = Value
                                        totalpopadd += Value

                # second assign for half cell
                # for vertical half cell
                for BuiltupY in range(2):
                    for BuiltupX in range(2):
                        if tempPop[BuiltupY][BuiltupX] != 0 :
                            # for populated empty area at 1st column
                            if BuiltupOrNotInformation[BuiltupY][BuiltupX] == 0:
                                for LocalY in range(2):
                                    Value = tempPop[BuiltupY][BuiltupX]*(0.5/6.25)
                                    PopulationAssignedBuiltupMatrix[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+2] += Value
                                    totalpopadd += Value

                            # for populated builtup area at 1st column
                            elif BuiltupOrNotInformation[BuiltupY][BuiltupX] != 0:
                                for LocalY in range(2):
                                    if int(BuiltupMap[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+2]) == 700:
                                        if tempPop[BuiltupY][BuiltupX] != 0:
                                            Value = tempPop[BuiltupY][BuiltupX]*(0.5/BuiltupOrNotInformation[BuiltupY][BuiltupX])
                                            PopulationAssignedBuiltupMatrix[PopCoorY*5+3*BuiltupY+LocalY][PopCoorX*5+2] += Value
                                            totalpopadd += Value

                # for horizontal half cell
                for BuiltupX in range(2):
                    for BuiltupY in range(2):
                        # for populated empty area at 1st row
                        if tempPop[BuiltupY][BuiltupX] != 0 :
                            if BuiltupOrNotInformation[BuiltupY][BuiltupX] == 0:
                                for LocalX in range(2):
                                    Value = tempPop[BuiltupY][BuiltupX]*(0.5/6.25)
                                    PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+3*BuiltupX+LocalX] += Value
                                    totalpopadd += Value

                            # for populated builtup area at 1st row
                            elif BuiltupOrNotInformation[BuiltupY][BuiltupX] != 0:
                                for LocalX in range(2):
                                    if int(BuiltupMap[PopCoorY*5+2][PopCoorX*5+3*BuiltupX+LocalX]) == 700:
                                        if tempPop[BuiltupY][BuiltupX] != 0:
                                            Value = tempPop[BuiltupY][BuiltupX]*(0.5/BuiltupOrNotInformation[BuiltupY][BuiltupX])
                                            PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+3*BuiltupX+LocalX] += Value
                                            totalpopadd += Value

                # third assign for quater cell
                # for populated builtup area
                if int(BuiltupMap[PopCoorY*5+2][PopCoorX*5+2]) == 700:
                    if tempPop[0][0] != 0:
                        ValueA = tempPop[0][0]*(0.25/BuiltupOrNotInformation[0][0])
                        PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueA
                        totalpopadd += ValueA
                    if tempPop[0][1] != 0:
                        ValueB = tempPop[0][1]*(0.25/BuiltupOrNotInformation[0][1])
                        PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueB
                        totalpopadd += ValueB
                    if tempPop[1][0] != 0:
                        ValueC = tempPop[1][0]*(0.25/BuiltupOrNotInformation[1][0])
                        PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueC
                        totalpopadd += ValueC
                    if tempPop[1][1] != 0:
                        ValueD = tempPop[1][1]*(0.25/BuiltupOrNotInformation[1][1])
                        PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueD
                        totalpopadd += ValueD

                # for populated empty area
                if int(BuiltupMap[PopCoorY*5+2][PopCoorX*5+2]) != 700:
                    if tempPop[0][0] != 0:
                        if BuiltupOrNotInformation[0][0] ==0:
                            ValueA = tempPop[0][0]*(0.25/6.25)
                            PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueA
                            totalpopadd += ValueA
                    if tempPop[0][1] != 0:
                        if BuiltupOrNotInformation[0][1] ==0:
                            ValueB = tempPop[0][1]*(0.25/6.25)
                            PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueB
                            totalpopadd += ValueB
                    if tempPop[1][0] != 0:
                        if BuiltupOrNotInformation[1][0] ==0:
                            ValueC = tempPop[1][0]*(0.25/6.25)
                            PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueC
                            totalpopadd += ValueC
                    if tempPop[1][1] != 0:
                        if BuiltupOrNotInformation[1][1] ==0:
                            ValueD = tempPop[1][1]*(0.25/6.25)
                            PopulationAssignedBuiltupMatrix[PopCoorY*5+2][PopCoorX*5+2] += ValueD
                            totalpopadd += ValueD
                            
                deviation = totalpopadd-sum([Q1pop,Q2pop,Q3pop,Q4pop])
                if  deviation != totalpopadd:
                    if deviation >= 0.01:
                        print(meshID,PopCoorY*2,PopCoorX*2,deviation)
                
                
            #print(count)
            #count += 1

        filename = "data/step8_builtuppop_data/PopulationAssignedBuiltup_" + str(meshID) + ".csv"
        metadata.writeout(PopulationAssignedBuiltupMatrix,filename)


            #for each_row in RegionalAggloLIST:
            #    for each_field in each_row:
            #        (Y,X) = each_field
            #        CellID = str(meshID)+"_"+str(Y)+"_"+str(X) #+"_"+str(DistributionMap[Y][X])
            #        output_file.write(str(CellID)+",")
            #    output_file.write("\n")

    print("#####################\nPart 8 program END.\n#####################")
