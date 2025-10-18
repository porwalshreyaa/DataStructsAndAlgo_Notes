def binary_search(v, L):
    if L == []:
        return (False)
    mid = len(L)//2
    if v == L[mid]:
        return (True)
    if v < L[mid]:
        return (binary_search(v,L[:mid]))
    else:
        return (binary_search(v,L[mid+1:]))