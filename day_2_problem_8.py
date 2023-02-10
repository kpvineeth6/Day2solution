def findTheSum(alpha):
    score = 0
    for i in range(0, len(alpha)):
        if (ord(alpha[i]) >= ord('A') and ord(alpha[i]) <= ord('Z')):
            score += ord(alpha[i]) - ord('A') + 1
        else:
            score += ord(alpha[i]) - ord('a') + 1
    return score
if __name__ == "_main_":
 
    S = "python"
    print(findTheSum(S)) 
           