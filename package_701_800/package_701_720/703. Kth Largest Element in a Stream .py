"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
"""
import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        初始化堆的过程，让堆的数量正好为K个
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) #采用库函数进行排序
        while len(self.nums) > k:
            heapq.heappop(self.nums) #如果小顶堆的数量超过了k个，就要把小顶堆出堆，让数量正好为K


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # 如果堆的数量小于K个，则推入数字
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:  #如果当前值比堆顶数字要大，那么替换小顶堆的堆顶元素
            heapq.heapreplace(self.nums, val)
        return self.nums[0] #返回小顶堆的第一个元素


class KthLargest2(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            self.nums.append(val)
        else:
            pass

        if len(self.nums) >= self.k:
            self.heapfy(self.nums, self.k, 0)
            if val > self.nums[0]:
                self.nums[0] = val #如果比最小的元素大，把最小的元素替换，重新排列堆
                self.heapfy(self.nums, self.k, 0)
            return self.nums[0]

    def heapfy(self, arr, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        small = i
        if l < n and arr[l] < arr[i]:  # l <n 的顺序不能反
            small = l
        if r < n and arr[r] < arr[small]:
            small = r
        if small != i:
            arr[i], arr[small] = arr[small], arr[i]
            self.heapfy(arr, n, small)

# Your KthLargest object will be instantiated and called as such:
if __name__ == '__main__':
    k = 3
    nums = [5, -1]
    val = 13
    # Your KthLargest object will be instantiated and called as such:
    obj = KthLargest(k, nums)
    param_1 = obj.add(2)
    param_2 = obj.add(1)
    param_3 = obj.add(-1)
    param_4 = obj.add(3)
    param_5 = obj.add(4)
    print(param_1)
    print(param_2)
    print(param_3)
    print(param_4)
    print(param_5)