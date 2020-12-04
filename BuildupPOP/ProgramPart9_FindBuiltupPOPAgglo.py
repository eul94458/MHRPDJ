print("#####################\nPart 9 program START.\n#####################")

import metadata

def check_cell_position(YX):
    (y,x) = YX
    #print("y=",y,"\t","x=",x)

    if y ==0 and x == 0:
        return "upper_left"
    elif y ==0 and x == 799:
        return "upper_right"
    elif y ==799 and x == 0:
        return "bottom_left"
    elif y ==799 and x == 799:
        return "bottom_right"
    elif y ==0 and ( x !=0 and x !=799):
        return "top"
    elif y ==799 and ( x !=0 and x !=799):
        return "bottom"
    elif ( y !=0 and y != 799 ) and x == 0:
        return "left"
    elif ( y !=0 and y != 799 ) and x == 799:
        return "right"
    elif ( y !=0 and y != 799 ) and ( x !=0 and x !=799):
        return "normal"

def check_adjcent_cell(cellYX,cell_position,checkfrom):
    (y,x) = cellYX
    #print("y=",y,"\t","x=",x,"\t",cell_position)
    AdjcentCellLIST = []
    ValidAdjcentCell = []
    
    if cell_position == "upper_left":
        AdjcentCellLIST = [(y,x+1),(y+1,x),(y+1,x+1)]
    elif cell_position == "upper_right":
        AdjcentCellLIST = [(y,x-1),(y+1,x-1),(y+1,x)]
    elif cell_position == "bottom_left":
        AdjcentCellLIST = [(y-1,x),(y-1,x+1),(y,x+1)]
    elif cell_position == "bottom_right":
        AdjcentCellLIST = [(y-1,x-1),(y-1,x),(y,x-1)]
    elif cell_position == "top":
        AdjcentCellLIST = [(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
    elif cell_position == "bottom":
        AdjcentCellLIST = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1)]
    elif cell_position == "left":
        AdjcentCellLIST = [(y-1,x),(y-1,x+1),(y,x+1),(y+1,x),(y+1,x+1)]
    elif cell_position == "right":
        AdjcentCellLIST = [(y-1,x-1),(y-1,x),(y,x-1),(y+1,x-1),(y+1,x)]
    elif cell_position == "normal":
        AdjcentCellLIST = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
    
    #print("AdjcentCellLIST\t" , AdjcentCellLIST)
    for element in AdjcentCellLIST:
        if (element in checkfrom) == True:
            new_element = element
            ValidAdjcentCell = ValidAdjcentCell + [new_element]
    
    #print("ValidAdjcentCell\t" , ValidAdjcentCell)
    return ValidAdjcentCell
                    
valid_Lv1meshID = metadata.call_populated_lv1mesh()    

if __name__ == "__main__":

    for meshID in valid_Lv1meshID:
    
        #while True:
        #meshID = input("Please Enter a Valid Lv1 MeshID : ")
            #if meshID == "exit" :
            #    break
            #else :
        DistributionMap = metadata.call_builtuppop_map(meshID)
        #print(type(DistributionMap[0][0]))

        ValidCellLIST = set() ############

        RegionalAggloLIST = []

        for rows in range(800):
            for fields in range(800):

                if float(DistributionMap[rows][fields]) != 0:

                    CellYX = (rows,fields)
                    ValidCellLIST.add(CellYX)

        ScannedCells = set() ############
        

        for CellYX in ValidCellLIST:   

            RegionalAgglo = set() ############
            #print(1, CellYX)

            if (CellYX in ScannedCells) == False :
                
                ScanLIST = []
                CurrentCellYX = CellYX
            
                ScanLIST.append(CurrentCellYX)
                
                while len(ScanLIST) != 0:                
                    for element in ScanLIST:
                        if (element in ScannedCells) == False:

                            #print(2, element)
                            
                            ThisElement = element
                        
                            CellPosition = check_cell_position(ThisElement) 
                            
                            ValidAdjcentCell = check_adjcent_cell(ThisElement,CellPosition,ValidCellLIST)
                            #print(2, ValidAdjcentCell)
                            
                            for items in ValidAdjcentCell:
                                if (items in  ScanLIST) == False:
                                    NewItemNeedScan = items
                                    ScanLIST.append(NewItemNeedScan)
                            ScanLIST.remove(ThisElement)
                            
                            ScannedCells.add(ThisElement)
                            
                            RegionalAgglo.add(ThisElement)
                            for items in ValidAdjcentCell:
                                if (items in  ScanLIST) == False:  
                                    NewCellOfRegionalAgglo = items
                                    RegionalAgglo.add(NewCellOfRegionalAgglo)
                            
                        else:
                            ScanLIST.remove(element)

                        #print(3, ScanLIST)
                        #print(4, ScannedCells)
                        #print(5, RegionalAgglo)
                        #print(6, RegionalAggloLIST)
                            
                RegionalAggloLIST.append(RegionalAgglo)

                #print(7, RegionalAggloLIST)
        
        Final_RegionalAggloLIST = []
        for rows in RegionalAggloLIST :
            templist = []
            for each_field in rows:
                (Y,X) = each_field 
                CellID = str(meshID)+"_"+str(Y)+"_"+str(X)+"_"+str(DistributionMap[Y][X])
                templist.append(CellID)
            Final_RegionalAggloLIST.append(templist)
                
        
        filename = "data/step9_regional_builtuppop/regional_builtuppop_" + str(meshID) + ".csv"
        metadata.writeout(Final_RegionalAggloLIST,filename)
                
                    
            #for each_row in RegionalAggloLIST:
            #    for each_field in each_row:
            #        (Y,X) = each_field
            #        CellID = str(meshID)+"_"+str(Y)+"_"+str(X) #+"_"+str(DistributionMap[Y][X])
            #        output_file.write(str(CellID)+",")
            #    output_file.write("\n") 
                
    print("#####################\nPart 9 program END.\n#####################")                                    
