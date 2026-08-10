# Problem Statement
# You are given a list of intervals where each interval is:
# [start, end]
# Merge all intervals that overlap.

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x:x[0])
    merged=[intervals[0]]
    for current in intervals[1:]:
        last=merged[-1]
        if current[0]<=last[1]:
            last[1]=max(current[1],last[1])
        else:
            merged.append(current)
    return merged
print(merge_intervals([
    [1,3],
    [2,6],
    [8,10],
    [9,11]
]))
print(merge_intervals([
    [1,4],
    [4,5]
]))
print(merge_intervals([
    [1,10],
    [2,3],
    [4,8]
]))