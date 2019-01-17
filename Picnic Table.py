def printPicnic(itemsDict):
    leftWidth = 0
    rightWidth = 0
    for k, v in itemsDict.items():
        if len(k) > leftWidth:
            leftWidth = len(k) + 1
        if len(str(v)) > rightWidth:
            rightWidth = len(str(v))+ 1
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(str(k).ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems)