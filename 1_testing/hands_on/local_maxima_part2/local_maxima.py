def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    idx = []
    up = False
    down = False
    for i in range(len(x)):
        if i == 0 or x[i - 1] < x[i]:
            up = True
            up_idx = i
        elif x[i - 1] > x[i]:
            up = False

        # if x[i-1] == x[i], no change

        if i + 1 == len(x) or x[i + 1] < x[i]:
            down = True
        elif x[i + 1] > x[i]:
            down = False

        if up and down:
            idx.append(up_idx)

    return idx
