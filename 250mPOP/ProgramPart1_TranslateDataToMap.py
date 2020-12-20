print("#####################\nPart 1 program START.\n#####################")

import metadata

def check_cell_position(YX):
    (y,x) = YX
    #print("y=",y,"\t","x=",x)

    if y ==0 and x == 0:
        return "upper_left"
    elif y ==0 and x == 319:
        return "upper_right"
    elif y ==319 and x == 0:
        return "bottom_left"
    elif y ==319 and x == 319:
        return "bottom_right"
    elif y ==0 and ( x !=0 and x !=319):
        return "top"
    elif y ==319 and ( x !=0 and x !=319):
        return "bottom"
    elif ( y !=0 and y != 319 ) and x == 0:
        return "left"
    elif ( y !=0 and y != 319 ) and x == 319:
        return "right"
    elif ( y !=0 and y != 319 ) and ( x !=0 and x !=319):
        return "normal"

def check_adjcent_cell(cellYX,cell_position,checkfrom):
    (y,x) = cellYX
    #print("y=",y,"\t","x=",x,"\t",cell_position)
    AdjcentCellLIST = []
    ValidAdjcentCell = []
    
    if cell_position == "upper_left":
        AdjcentCellLIST = [(y,x+1),(y+1,x),(y+1,x)]
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
    #meshID = input("Please Enter a Valid Lv1 MeshID : ") 
    
        DistributionMap = metadata.call_population_distribution_map(meshID)
        
        # 1.4 Prepare for obtaining data of Lv2 mesh
        lv1mesh_prefex = "tblT000876Q"

        # 1.6 Obtain Lv2 mesh data according to valid IDs
        for valid_id in DistributionMap:
            file_name = lv1mesh_prefex + valid_id
            temporary_2lvmesh_matrix = [ ["0" for i in range(320)] for j in range(320) ]
        
        
        with open("data/"+str(valid_id)+".csv" , "r") as input_file:
            
        
        # 1.7 Extract population data of each mesh
            for rows in temporary.readtolist(file_name):
            # land_id = rows[0]
            # population = row[4]
            # first define all usable variables
                land_id = str(rows[0])
                population = int(rows[4])

                a = int(land_id[4])
                b = int(land_id[5])
                c = int(land_id[6])
                d = int(land_id[7])
                e = int(land_id[8])
                f = int(land_id[9])

                if e == 1:
                    forth_y = 1
                    forth_x = 0
                elif e == 2:
                    forth_y = 1
                    forth_x = 1
                elif e == 3:
                    forth_y = 0
                    forth_x = 0
                else:
                    forth_y = 0
                    forth_x = 1

                if f == 1:
                    fifth_y = 1
                    fifth_x = 0
                elif f == 2:
                    fifth_y = 1
                    fifth_x = 1
                elif f == 3:
                    fifth_y = 0
                    fifth_x = 0
                else:
                    fifth_y = 0
                    fifth_x = 1

                # formula for y-axis coordinate:
                # 40(7-a) + 4(9-c) + 2(forth_y) + 1(fifth_y)
                # formula for x-axis coordinate:
                # 40(b) + 4(d) + 2(forth_x) + 1(fifth_x)
                y_axis = 40*(7-a) + 4*(9-c) + 2*(forth_y) + 1*(fifth_y)
                x_axis = 40*(b) + 4*(d) + 2*(forth_x) + 1*(fifth_x)

        # 1.8 Writing population data into temporary matrix
                temporary_2lvmesh_matrix[y_axis][x_axis] = population
                    
        with open("data/regional_agglomeration_data/agglomeration_"+str(meshID)+".csv" , "w") as output_file:
            for each_row in RegionalAggloLIST:
                for each_field in each_row:
                    (Y,X) = each_field
                    CellID = str(meshID)+"_"+str(Y)+"_"+str(X)+"_"+str(DistributionMap[Y][X])
                    output_file.write(str(CellID)+",")
                output_file.write("\n") 
            
    print("#####################\nPart 1 program END. All level 2 mesh population data are output.\n#####################")                             
