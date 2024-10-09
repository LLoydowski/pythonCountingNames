def countElements(list):
    return len(list)

def countNames(names):
    namesCounter = {}

    for name in names:
        if name in namesCounter:
            namesCounter[name] += 1
        else:
            namesCounter[name] = 1
    
    return namesCounter


def getUniqueValues(names):
    dict = countNames(names)
    list = []

    for key in dict:
        if dict[key] == 1:
            list.append(key)

    return list