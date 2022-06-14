import collections
import heapq


#Question 1
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.heap)

    def add(self,val):
        heapq.heappush(self.heap, val)

        if len (self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


#Question 2
def smallest(stones):
    stones = [-s for s in stones] #make Max Heap
    heapq.heapify(stones) #making a heap outof stones

    while len(stones) > 1: #as long as we have stones
        first =  heapq.heappop(stones)
        second = heapq.heappop(stones)

        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0) #append the first - second value to the stones
    return abs(stones[0])


#Question 3
def closestPoint(points, k):
    pts = [] #create a minHeap
    for x, y in points: #calculate the distance from origin [0,0]
        dist = (abs(x-0)**2) + (abs(y - 0)**2)
        pts.append([dist, x, y])

    res = []
    heapq.heapify(pts)
    for i in range(k):
        dist, x, y = heapq.heappop(pts) #pop from the heap in increasing order cuz its a meanHeap
    res.append([x,y]) #to get the point as requested in the question
    return res



#Question 4
def Kthlargest(nums, k):

    #Approach 1: MaxHeap ##build maxheap by putting negative sign on num so the the largest number becomes the smallest number and is the first for minsheap. since we want the kth largest so we pop k-1 times and the next pop will return the kth largest
    maxheap = [-num for num in nums]
    heapq.heapify(maxheap)

    for _ in range(k-1):
        heapq.heappop(maxheap)
    return heapq.heappop(maxheap)*-1

     #Approach2: MinHeap
def largest(nums, k):
    minheap = []
        
    for num in nums:
        heapq.heappush(minheap, -num)
        
    for _ in range(k-1):
        heapq.heappop(minheap)
        
    return -minheap[0]

    #Approach 3: MinHeap
def largest(nums, k):
    heapq.heapify(nums)

    while len(nums)>k:
        heapq.heappop(nums)

    return nums[0]


#Question 5
def smallest(tasks, n):
    count = collections.Counter(tasks) #simple counter to get the number of each task, same as having a dictionary or hash map
    maxheap = [-cnt for cnt in count.values()]  #bc we wanna have from most-least frequencies of the tasks
    heapq.heapify(maxheap) #build heap from the above list via heapify

    time = 0 #initially we start processing at time zero
    q = collections.deque() #pair [-cnt, idle time]
     
    while maxheap or q: #if we have either one then we need to process a task which based on the question takes 1 unit of time so;
        time += 1

        if maxheap: #if we have maxheap which is not empty
            cnt = 1 + heapq.heappop(maxheap) #we add 1 since we negate earlier

            if cnt: # if this cnt is not Zero then go n append it to the q
                q.append([cnt, time + n])  #push it to the queue and check the time to whether reach the time of getting it back to the heap

        if q and q[0][1] == time: #equal to currernt time, time to push back to heap to start the process of that letter again!
            heapq.heappush(maxheap, q.popleft()[0]) #its gonna pop the first "pair" but we only care abt the cnt, so we wanna the index 0, then we wanna push it back to the heap!
    
    return time
             