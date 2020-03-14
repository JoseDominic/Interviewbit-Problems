# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
merge_interval = Interval()
dummy = Interval(10**10,0)
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        count_0 =0
        for i in range(len(intervals)):
            if(intervals[i]!=0):
                for j in range(len(intervals)):
                    if(i!=j and intervals[j]!=0):
                        if(max(intervals[i].start,intervals[j].start)<=min(intervals[i].end,intervals[j].end)):
                            merge_interval.start = min(intervals[i].start,intervals[j].start)
                            merge_interval.end = max(intervals[i].end,intervals[j].end)
                            intervals[i] = merge_interval
                            intervals[j] = 0
                            count_0+=1
        new = []
        k=0
        for i in range(len(intervals)):
            if(k==0 and intervals[i]!=0):
                new.append(intervals[i])
                k+=1
                continue
            if(intervals[i]!=0):
                f =[]
                l=0
                r=0
                left = []
                right = []
                left.append(intervals[i])
                left.append(dummy)
                right = new + [dummy]
                
                for j in range(len(new)+1):
                    if(left[l].start<=right[r].start):
                        f.append(left[l])
                        l+=1
                    else:
                        f.append(right[r])
                        r+=1
                #print(f)
                new =f
                k+=1
        return new
