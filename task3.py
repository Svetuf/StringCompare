givenString = input()
M = [[]]
palindrome = []

for i in range(len(givenString)):
    palindrome.append("")

for i in range(len(givenString)):
    M.append([])
    for j in range(len(givenString)):
        M[i].append(0)


def fillMatrix(l, r):
    if M[l][r] == -1:
        if givenString[l] == givenString[r]:
            M[l][r] = fillMatrix(l + 1, r - 1) + 2
        else:
            M[l][r] = max(fillMatrix(l + 1, r), fillMatrix(l, r - 1))
    return M[l][r]


def FindSubPolinome(l, r, lBorder, rBorder):
    while l <= r:
        if l == r and M[l][r] == 1:
            palindrome[lBorder] = givenString[l]
            lBorder += 1
            l += 1
        else:
            if givenString[l] == givenString[r]:
                palindrome[lBorder] = givenString[l]
                lBorder += 1
                l += 1
                palindrome[rBorder] = givenString[r]
                rBorder -= 1
                r -= 1
            else:
                if M[l + 1][r] > M[l][r - 1]:
                    l += 1
                else:
                    r -= 1


for i in range(len(givenString)):
    for j in range(len(givenString)):
        if i == j:
            M[i][j] = 1
        if i > j:
            M[i][j] = 0
        if i < j:
            M[i][j] = -1

ans = fillMatrix(0, len(givenString) - 1)
FindSubPolinome(0, len(givenString) - 1, 0, len(givenString) - 1)
ansString = str()

for x in palindrome:
    if x != "": ansString += x

print(ansString)
