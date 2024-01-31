# Take in a list and output a list that returns a dictionary that maps each element in the original list to the number of times it appears in the list (the values)
def checkDuplicates(lst):
    counts = {}
    retList = []

    # Count the occurrences of each item using a dictionary
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    return counts

# Trying the function out
def main():
    print(checkDuplicates([1, 1, 2, 4, 2, 3]))

if __name__ == "__main__":
    main()
