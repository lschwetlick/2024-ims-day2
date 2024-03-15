def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    unique = [x[i] for i in range(len(x)) if (i==0) or x[i] != x[i-1]]
    old_indices = [i for i in range(len(x)) if (i==0) or x[i] != x[i-1]]
   
    maxima = []
    if len(unique) >= 2 and unique[1] < unique[0]:
        maxima.append(0)
    for i in range(1, len(x) - 1):
        if unique[i] > unique[i - 1] and unique[i] > unique[i + 1]:
            maxima.append(old_indices[i])

    if len(unique) >= 2 and unique[-1] > unique[-2]:
        maxima.append(len(unique) - 1)
    return maxima