from PIL import Image, ImageDraw
from numpy import genfromtxt 








if __name__ == "__main__":
    
    meshID = input("Please Enter a Valid Lv1 MeshID : ")
    
    for meshID in valid_Lv1meshID:
    
        RegionalAggloDATA = []
        
        with open("data/regional_agglomeration_data/agglomeration_"+str(meshID)+".csv" , "r") as input_file:
            for line in input_file:
                NewLine = line.strip()
                NewLine = NewLine[:-1]
                NewLine = NewLine.strip().split(",")
                RegionalAggloDATA.append(NewLine)
                
        meshDATA = []
        
        for RegionalAgglo in RegionalAggloDATA:
        
            RegionalAggloPopulation = 0
            RegionalAggloNewLIST = []
            
            for CellID in RegionalAgglo:
            
                CellINFO = CellID.split("_")
                
                meshID = int(CellINFO[0])
                cellY = int(CellINFO[1])
                cellX = int(CellINFO[2])
                cellPopulation = int(CellINFO[3])
                
                RegionalAggloPopulation += cellPopulation
                
                buffer = CellID
                RegionalAggloNewLIST.append(buffer)
            
            RegionalAggloNewLIST.insert(0,RegionalAggloPopulation)
            meshDATA.append(RegionalAggloNewLIST)
        
        meshDATA.sort(reverse=True)
        
        for index in range(len(meshDATA)):
            meshDATA[index].insert(0,index)
        
        with open("data/regional_agglomeration_data_sorted/regional_agglomeration_data_sorted"+str(meshID)+".csv" , "w") as output_file:
            for each_row in meshDATA:
                for each_field in each_row:
                    output_file.write(str(each_field)+",")
                output_file.write("\n")
    


    
            
    BiggestRegionalAggloDATA = meshDATA[0]
    BiggestRegionalAggloDATA = BiggestRegionalAggloDATA[1:]



    matrix = [[0 for i in range(320)] for j in range(320)]

    for element in BiggestRegionalAggloDATA:

        cellINFO = element.split("_")
        #print(element)

        matrix[int(cellINFO[1])][int(cellINFO[2])] = int(cellINFO[3])


    with open("data/matrix_"+str(meshID)+".csv" , "w") as output_file:
        for each_row in matrix:
            for each_field in each_row:
                output_file.write(str(each_field)+",")
            output_file.write("\n")



    g = open("data/matrix_"+str(meshID)+".csv" ,"r")
    temp = genfromtxt(g, delimiter = ',')
    #temp = matrix
    im = Image.fromarray(temp).convert('RGB')
    pix = im.load()
    rows, cols = im.size
    for x in range(320):
        for y in range(320):
            #print(str(x) + " " + str(y))
            pix[x,y] = (int(temp[y,x] // 256 // 256 % 256),
                        int(temp[y,x] // 256  % 256),
                        int(temp[y,x] % 256))
    im.save(g.name[0:-4] + '.tif')
        
    
