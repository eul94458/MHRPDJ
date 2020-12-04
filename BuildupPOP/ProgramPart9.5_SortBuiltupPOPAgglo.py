print("#####################\nPart 9.5 program START.\n#####################")

import metadata

if __name__ == "__main__":

    valid_Lv1meshID = metadata.call_populated_lv1mesh()

    for meshID in valid_Lv1meshID:
    #meshID = input("Please Enter a Valid Lv1 MeshID : ")
    
        RegionalAggloDATA = []
    
        with open("data/step9_regional_builtuppop/regional_builtuppop_"+str(meshID)+".csv" , "r" , encoding="utf-8") as input_file:
            for line in input_file:
                NewLine = line.strip()
                #NewLine = NewLine[:-1]
                NewLine = NewLine.strip().split(",")
                RegionalAggloDATA.append(NewLine)
                
        meshDATA = []
        
        for RegionalAgglo in RegionalAggloDATA:
        
            RegionalAggloPopulation = 0
            RegionalAggloNewLIST = []
            
            for CellID in RegionalAgglo:
            
                CellINFO = CellID.split("_")
                
                mesh = int(CellINFO[0])
                Y = int(CellINFO[1])
                X = int(CellINFO[2])
                P = float(CellINFO[3])
                
                RegionalAggloPopulation += P
                
                buffer = CellID
                RegionalAggloNewLIST.append(buffer)
            
            RegionalAggloNewLIST.insert(0,RegionalAggloPopulation)
            meshDATA.append(RegionalAggloNewLIST)            
        
        meshDATA.sort(reverse=True)
        
        for index in range(len(meshDATA)):
            meshDATA[index].insert(0,index)        
  
        
        filename = "data/step9_regional_builtuppop/regional_builtuppop_sorted_" + str(meshID) + ".csv"
        metadata.writeout(meshDATA,filename)
        
        #with open("data/step2_regional_agglomeration_data/agglomeration_sorted_"+str(meshID)+".csv" , "w" , encoding="utf-8") as output_file:
        #    for each_row in meshDATA:
        #        for each_field in each_row:
        #            output_file.write(str(each_field)+",")
        #        output_file.write("\n")
            
    print("#####################\nPart 9.5 program END.\n#####################")  