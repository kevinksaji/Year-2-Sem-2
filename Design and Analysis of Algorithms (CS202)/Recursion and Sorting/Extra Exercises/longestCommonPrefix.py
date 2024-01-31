# function to find the smallest string in the input list
def smallestString(input):
    smallest = len(input[0])
    for i in input:
        if (len(i) < smallest):
            smallest = len(i)

    return smallest

# function to check for matching prefix based on the index, passed in the num parameter
def prefixMatch(input, num):
    for i in range(len(input)-1):
        if input[i][:num] != input[i+1][:num]:
            return False
    return True

def longestCommonPrefix(input):
    smallest = smallestString(input)

    # initialise index to 1 as the index itself is not included in the slicing in the prefixMatch function
    index = 1

    # while loop that increments index as long as the value of index is smaller than the smallest string in input and prefixMatch returns true
    while(index<= smallest and prefixMatch(input, index)):
        index = index + 1
    
    # if index is 1 it means that the first letters of all strings in input do not match, hence no common prefix at all
    if (index == 1):
        return ""
    # return longest common prefix
    else:
        return input[0][:index-1]
    
# main function for testing
def main():
    print(longestCommonPrefix(["flower","power","chowder"]))

if __name__ == "__main__":
    main()

