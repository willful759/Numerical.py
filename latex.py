def augmatToTex(mat):
    res = "\n\\begin{bmatrix}["
    for i in range(len(mat[0]) - 1):
        res += "c"
    res += "|c]\n"
    for i in range(len(mat)):
        for j in range(len(mat[0]) - 1):
            res += f"{mat[i][j]} & "
        res += f"{mat[i][len(mat[0]) - 1]} \\\\\n"
    res += "\\end{bmatrix}\n"
    return res


def matToTex(mat):
    res = "$$\n\\begin{bmatrix}["
    for i in range(len(mat[0])):
        res += "c"
    res += "]\n"
    for i in range(len(mat)):
        for j in range(len(mat[0]) - 1):
            res += f"{mat[i][j]} & "
        res += f"{mat[i][len(mat[0]) - 1]} \\\\\n"
    res += "\\end{bmatrix}\n"
    return res

def vecToTex(vec):
    res = "\\begin{bmatrix}["
    for i in range(len(vec)):
        res += "c"
    res += "]\n"
    for i in range(len(vec) - 1):
        res += f"{vec[i]} & "
    res += f"{vec[i]} \\\\\n\\end{bmatrix}\n"
    return res
