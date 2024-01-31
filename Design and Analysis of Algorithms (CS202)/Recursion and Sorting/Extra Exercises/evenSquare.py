def evenSquare(lst):
    retLst = [];
    for element in lst:
        if element % 2 == 0:
            retLst.append(element**2)

    return retLst

def main():
    print(evenSquare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if __name__ == "__main__":
    main()
