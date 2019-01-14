
def readFile(num):
    data = []
    file = open("csbData.txt","r")
    for i in range(num):
        tempData = file.readline().replace('\n', '')
        tempData += file.readline().replace('\n', '')
        dataArr = tempData.split(' ')
        dataArr = list(filter(None, dataArr))
        xtmp = []
        xtmp.append(dataArr[0])
        xtmp.append(dataArr[1])
        xtmp.append(dataArr[2])
        xtmp.append(dataArr[3])
        xtmp.append(dataArr[4])
        xtmp.append(dataArr[5])
        xtmp.append(dataArr[6])
        xtmp.append(dataArr[7])

        x = []
        for xi in xtmp:
            #print(xi)
            x.append(float(xi))
        
        ytmp = []
        ytmp.append(dataArr[8])
        ytmp.append(dataArr[9])

        y = []
        for yi in ytmp:
            y.append(float(yi))
        
        data.append(tuple((x, y)))
    return data

#print(readFile(500))

    
