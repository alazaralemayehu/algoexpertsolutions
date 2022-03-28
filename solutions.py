
# https://leetcode.com/problems/two-sum/
def twoNumberSum(array, targetSum):
    for i in array:
        for j in array:
            if (i + j == targetSum and j != i):
                return [i, j]
    return []


# https://leetcode.com/problems/is-subsequence/
def isValidSubsequence(array, sequence):
    i = 0
    sequence_max_index = len(sequence)
    for j in array: 
        if (sequence[i] == j):
            i +=1 
        if (i == sequence_max_index):
            return True
    return False

# https://leetcode.com/problems/3sum/
def threeNumberSum(array, targetSum):
    # Write your code here.
    sumDictionary = {array[i]: i for i in range(len(array)-1)}
    sumList = []

    length = len(array)
    for i in range(length):
        for j in range(i+1, length):
            print(i, j)
            firstNumber = array[i]
            secondNumber = array[j]	
            thirdNumber = targetSum -(firstNumber + secondNumber )

            if thirdNumber in sumDictionary:
                thirdIndex = sumDictionary[thirdNumber]
                if (thirdIndex != i and thirdIndex != j):	
                    tripplets = sorted([firstNumber,secondNumber,thirdNumber])
                    if (tripplets not in sumList):
                        print(firstNumber, secondNumber, thirdNumber)

                        sumList.append(tripplets)
    return sorted(sumList)

# https://leetcode.com/problems/coin-change/
def nonConstructibleChange(coins):
    # Write your code here.
	coins.sort()
	
	currentChange = 0
	
	for coin in coins:
		if coin > currentChange + 1:
			return currentChange + 1
		currentChange += coin
	
	return currentChange + 1


# dynamic programming
# https://leetcode.com/discuss/interview-question/702177/apple-phone-maximum-sum-of-non-adjacent-elements
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) < 1:
        return 0
    elif len(array) == 1:
        return array[0]
    listOfSum = array[:]
    listOfSum[1] = max(array[0], array[1])
    for i in range(2,len(array)):
        listOfSum[i] = max(listOfSum[i-1], listOfSum[i-2] + listOfSum[i])
    return listOfSum[len(array) - 1]

# https://www.hackerrank.com/challenges/balanced-brackets/problem
def balancedBrackets(string):
    # Write your code here.
	stack = []
	openingBracket = ["(","[","{"]
	closingBracket = [")","]","}"]
	for i in string:
		if i in openingBracket:
			stack.append(i)
		elif i in closingBracket:
			if len(stack) == 0:
				return False
			poppedElement = stack.pop()
			if openingBracket.index(poppedElement) != closingBracket.index(i):
				return False
		else:
			continue
    if len(stack) == 0:
        return True
    return False
