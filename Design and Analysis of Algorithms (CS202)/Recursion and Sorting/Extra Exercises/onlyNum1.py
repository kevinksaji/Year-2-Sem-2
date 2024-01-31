def onlyNum1(num1, num2):
    retList = []
    for i in num1:
        # can use in and not in keyword to find elements in or not in a list
        if i not in num2:
            retList.append(i);
    return retList


# main function for testing
def main():
    print(onlyNum1([1, 3, 5, 2, 6, 4], [3, 4, 1, 6]))

if __name__ == "__main__":
    main()
