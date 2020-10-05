from collections import deque


class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def __repr__(self):
        return str((self.begin, self.end))

#function to remove overlaping intervals
def remove_overlaping(intervals):
    # sort the intervals in increasing order of their starting time
    intervals.sort(key=lambda x: x.begin)
    
    #case 1. non overlaping - current end less or equal to next begin
    #case 2 overlaping -- remove next --> current end <= next end
    #case 3 overlaping -- remove cuurent --> current end > next end
    #always remove larger interval - because it will overlap more element

    count = 0
    n = len(intervals)
    left = 0
    right = 1
    while(right < n):
        if(intervals[left].end <= intervals[right].begin ):  # non ovelaping
            left = right
            right +=1
        elif(intervals[left].end <= intervals[right].end) : #overlaping - rmove right
            print("overlaping element", intervals[right])
            count +=1
            right +=1
        elif(intervals[left].end > intervals[right].end):
            print("overlaping element", intervals[left])
            count +=1
            left = right
            right +=1
    
    print("Overlaping count ", count)

def merge_ovelaping(intervals):
    # sort the intervals in increasing order of their starting time
    intervals.sort(key=lambda x:x.begin)

    #create an empty stack
    stack = deque()

    # do for each interval
    for curr in intervals:
        # if stack is empty or top interval in stack do not overlap
		# with current interval, push it to the stack
        if not stack or curr.begin > stack[-1].end:
            stack.append(curr)
        
        # if top interval of stack overlap with current interval,
		# merge two intervals by updating ending of top interval
		# to ending of current interval
        if stack[-1].end < curr.end:
            stack[-1].end = curr.end
    
    print("All merged interval")
    print(stack)

#Activitity selection
#Find maximum number of activities that can be performed by single person
#Step 1 : sort the activities by finishing time
#Step 2 : non overlaping - current end less or equal to next begin
def activity_selection(intervals):
    #sorting
    intervals.sort(key=lambda x: x.end)
    out = set()
    left = 0
    for right in range(1,len(intervals)):
        if intervals[left].end <= intervals[right].begin:
            print(intervals[left])
            out.add(intervals[right])
            left =right
            
    print("All max Activitity selection")
    print(out)

    # k keeps track of the index of the last selected activity
    '''k = 0

    # set to store the selected activities index
    out = set()

    # select 0 as first activity
    out.add(0)

    # start iterating from the second element of
    # vector up to its last element
    for i in range(1, len(activities)):

        # if start time of i'th activity is is greater or equal
        # to the finish time of the last selected activity, it
        # can be included in activities list
        if activities[i][0] >= activities[k][1]:
            out.add(activities[k])
            k = i  # update i as last selected activity
    
    print(out)'''

if __name__ == "__main__":
    intervals = [Interval(1, 5),Interval(8, 10), Interval(2, 3), Interval(4, 6),
                Interval(7, 8),  Interval(12, 15)]
    #intervals = [Interval(0, 3),Interval(1, 2), Interval(2, 6), Interval(5, 6)]
    remove_overlaping(intervals)
    merge_ovelaping(intervals)
    intervals = [Interval(1, 4),Interval(3, 5), Interval(0, 6), Interval(5, 7)
            , Interval(3, 8), Interval(5, 9), Interval(6, 10), Interval(8, 11)
            , Interval(8, 12), Interval(2, 13), Interval(12, 14)]
    activity_selection(intervals)
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
                    (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

    # Sort the activities according to their finishing time
    activities.sort(key=lambda x: x[1])
    #activity_selection(activities)
    #activity_selection(intervals)

    
