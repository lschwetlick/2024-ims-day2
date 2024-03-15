def find_maxima(x): 
    """Find local maxima of x. 
 
    Input arguments: 
    x -- 1D list of real numbers 
 
    Output: 
    idx -- list of indices of the local maxima in x 
    """ 
    # we shuld adapt this code
    indices = [] 
    # check border condition at start 
    if x[0] > x[1]: 
        indices.append(0) 
    for i in range(1, len(x)-2): 
        if (x[i-1] < x[i]) and (x[i] > x[i+1]): 
            indices.append(i) 
    # check border condition at the end 
    if x[len(x)-1] > x[len(x)-2]: 
        indices.append(i) 
    return indices
