


def getMax(data):
    dataCopy = data[:]
    dataCopy.sort()
    return dataCopy[-1]

def getMin(data):
    dataCopy = data[:]
    dataCopy.sort()
    return dataCopy[0]


def hist(data:list[float], buckets:int) -> list[int]:
    maximum = getMax(data)
    minimum = getMin(data)

    bucketSize = (maximum - minimum) / buckets

    #acc = [] 
    #for i in range(buckets):
    #    acc.append(0)

    acc = [0] * buckets 

    dataCopy = data[:]

    while len(dataCopy) > 0:
        dataPoint = dataCopy.pop(0)

        for i in range(buckets):

            if minimum + i * bucketSize <= dataPoint <= minimum + (i+1) * bucketSize:
                acc[i] += 1

    return acc

print(hist([1,2,3,3,3,4,7,9], 3))