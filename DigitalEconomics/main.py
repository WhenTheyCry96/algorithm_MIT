#!usr/bin/env python2.7

cityMatrix = [[-1 for x in range(1, 8)] for y in range(1, 8)]

cityMatrix = [
    [0, 44, 170, 303, 305, 413, 386, 0],  # incheon
    [44, 0, 165, 290, 298, 401, 375, 0],  # seoul
    [17, 165, 0, 153, 168, 268, 260, 0],  # daejeon
    [303, 290, 153, 0, 210, 109, 117, 0],  # daegu
    [305, 298, 168, 210, 0, 261, 303, 0],  # gwangju
    [413, 401, 268, 109, 261, 0, 58, 0],  # busan
    [386, 375, 260, 117, 303, 58, 0, 0],   # ulsan
    [0, 0, 0, 0, 0, 0, 0, 0]  # PyeonChang
]

constructionCost = 2.5  # unit: [milion dollar/KM]

pyeongchang = [149, 126, 145, 168, 282, 250, 221, 0]  # incheon to ulsan distance


def averageDist(matrix):
    avg = 0
    count = 0
    len_row = len(matrix)
    len_col = len(matrix[0])
    for x in range(len_row):
        for y in range((len_col)):
            if matrix[x][y] is not 0:
                avg += matrix[x][y]
                count += 1
    avg /= count
    return avg


def constructHighway(cMatrix, pMatrix):
    result = {'Destination': '', 'Distance': 0, 'Construction': 0}
    tmp = [0, 0, 0]  # avgDistofAllCities, city, Distance
    avg_tmp = 1000
    for i in range(len(pMatrix)):
        print "%d iteration \n" % i
        for j in range(len(cMatrix)):
            cMatrix[j][7] = cMatrix[j][i] + pyeongchang[i]
            cMatrix[7][j] = cMatrix[j][7]
        avg_i = averageDist(cMatrix)
        print avg_i
        if avg_i < avg_tmp:
            avg_tmp = avg_i
            tmp[1] = i

    tmp[0] = avg_tmp
    tmp[2] = pMatrix[tmp[1]]
    cities = ['Incheon', 'Seoul', 'Daejeon', 'Daegu', 'Gwangju', 'Busan',
              'Ulsan']
    print "Highway to '%s' city is the cheapest" % cities[tmp[1]]
    result['Destination'] = '%s' % cities[tmp[1]]
    result['Distance'] = tmp[0]
    result['Construction'] = tmp[2]*2.5
    return result


# if __name__ is '__main__':
def main():
    test = averageDist(cityMatrix)
    print test
    print constructHighway(cityMatrix, pyeongchang)
    for i in range(len(cityMatrix)):
        print cityMatrix[i]


# main
main()
