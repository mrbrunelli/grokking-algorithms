def binary_search(lst, tgt):
    lef = 0
    rig = len(lst) - 1
    while lef <= rig:
        mid = (lef + rig) // 2
        attp = lst[mid]
        if attp == tgt:
            return mid
        if attp > tgt:
            rig = mid - 1
        else:
            lef = mid + 1
    return None

