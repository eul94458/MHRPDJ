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

valid_Lv1meshID = metadata.call_landscape_lv1mesh()

if __name__ == "__main__":

    for meshID in valid_Lv1meshID:
    #meshID = input("Please Enter a Valid Lv1 MeshID : ")

         # 1.4 Prepare for obtaining data of Lv2 mesh
        lv1mesh_prefex = "L03-b-16_"
        file_name = lv1mesh_prefex + str(meshID) + ".xml"

        DistributionMap = []

        with open("data/rawdata/rawdata2016/" + file_name , "r" , encoding="utf-8") as file:
            
            for n in range(29):
                line = file.readline()
                if line == "<gml:tupleList>" :
                    break
                
            #print("found")
            #count = 0
            for n in range(800):
                #count += 1
                #print(count)
                line = file.readline().rstrip().lstrip()
                
                if line != "</gml:tupleList>" :                    
                    new_row = line.split(" ")
                    DistributionMap.append(new_row)
                else :
                    break
             
        #print( len(DistributionMap[0] ))


        with open("data/step1_landusemesh/landuse_"+str(meshID)+".csv" , "w" , encoding="utf-8") as output_file:
            for y in range(799):
                for x in range(799):
                    readytowrite = str(DistributionMap[y][x])
                    output_file.write(readytowrite)
                    output_file.write(",")
                readytowrite = str(DistributionMap[y][799])
                output_file.write(readytowrite)
                
                output_file.write("\n")
                
            for x in range(799):
                readytowrite = str(DistributionMap[799][x])
                output_file.write(readytowrite)
                output_file.write(",")
            readytowrite = str(DistributionMap[799][799])
            output_file.write(readytowrite)
                
        print("written")
        
    print("#####################\nPart 1 program END.\n#####################")
