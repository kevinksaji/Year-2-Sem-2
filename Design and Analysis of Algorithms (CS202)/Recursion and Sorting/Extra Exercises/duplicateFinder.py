def duplicateFinder(input):
    input.sort()
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            return True;
    return False


# main function for testing
def main():
    print(duplicateFinder([1, 3, 5, 2, 6, 4]))

if __name__ == "__main__":
    main()
