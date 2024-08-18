class Solution:
  def minMeetingRooms(self, intervals: list[list[int]]) -> int:
    minHeap = []  

    for start, end in sorted(intervals):
      if minHeap and start >= minHeap[0]:
        heapq.heappop(minHeap)
      heapq.heappush(minHeap, end)

    return len(minHeap)