def average(datalist):
    sum = datalist.sum()
    length = len(datalist)
    aver = sum / length
    return aver

def correlation_coefficient(xlist,ylist,xmean,ymean):

    numerator = 0
    #分子
    denominator = 0
    #分母


    for i in range(len(xlist)):
        x = xlist[i] - xmean
        y = ylist[i] - ymean
        numerator += x * y
    

    xcache = 0
    ycache = 0
    for i in range(len(xlist)):
        x1 = xlist[i] - xmean
        y1 = ylist[i] - ymean
        xcache += x1 ** 2
        ycache += y1 ** 2
    
    xcache = xcache ** 0.5
    ycache = ycache ** 0.5

    denominator += xcache * ycache


    r = numerator / denominator
    return r