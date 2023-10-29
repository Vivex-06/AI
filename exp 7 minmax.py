import math
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if (curDepth == targetDepth):
        return scores[nodeIndex]
    if (maxTurn):
        left = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        print(f"Maximizing player at depth {curDepth} chose {max(left, right)}")
        return max(left, right)
    else:
        left = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        print(f"Minimizing player at depth {curDepth} chose {min(left, right)}")
        return min(left, right)
scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)
print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))