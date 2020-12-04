# coding = utf8

print("#####################\nPart 0 program START.\n#####################")

import metadata

valid_Lv1meshID = metadata.call_populated_lv1mesh()

def mergeDATA():
    requestedYear = []
    for grid in valid_Lv1meshID:
        FileName = str(FilePrefix) + str(grid) + ".csv"

        tempStorage = []

        with open("data/rawdataset/" + query + "/" + FileName , "r" , encoding="shift-jis") as input_file:
            for line in input_file:
                NewLine = line.strip()
                tempStorage.append([NewLine])
        del tempStorage[0]
        del tempStorage[0]

        requestedYear.extend(tempStorage)
    filename = "data/outputdata/step0_mergegrid/mergegrid_" + str(query) + ".csv"
    metadata.writeout(requestedYear,filename)

def mergeDATAspecial():
    requestedYear = []
    for grid in valid_Lv1meshID:
        FileName = str(FilePrefix) + str(grid) + ".csv"

        tempStorage = []

        with open("data/rawdataset/" + query + "/" + FileName , "r" , encoding="shift-jis") as input_file:
            for line in input_file:
                NewLine = line.strip()
                NewLine = NewLine.split(",")
                tempStorage.append(NewLine)
        del tempStorage[0]
        del tempStorage[0]
        
        for eachsubset in tempStorage:
            #print(eachsubset)
            TargetData = str(eachsubset[0])+","+str(eachsubset[4])+","+str(eachsubset[5])+","+str(eachsubset[6])+","+str(eachsubset[28])
            requestedYear.append([TargetData])

    filename = "data/outputdata/step0_mergegrid/mergegrid_" + str(query) + ".csv"
    metadata.writeout(requestedYear,filename)

if __name__ == "__main__":

    while True:
        query = input("Which year? : ")

        if query != "quit":

            if query != "2015":
                if query == "1995":
                    FilePrefix = "tblT000752H"
                elif query == "2000":
                    FilePrefix = "tblT000386H"
                elif query == "2005":
                    FilePrefix = "tblT000387H"
                elif query == "2010":
                    FilePrefix = "tblT000609H"

                mergeDATA()

            elif query == "2015":
                FilePrefix = "tblT000847H"
                mergeDATAspecial()



            print("Finished, next task.")

        elif query == "quit":
            break




    print("#####################\nPart 0 program END.\n#####################")
