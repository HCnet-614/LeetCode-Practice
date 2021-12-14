class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]):
        #设置计数器和结果初始值 / Set counter and result initial values
        count = result = 0       
        for num in nums:
            #见1就给计数器加1  /  add 1 to the counter when see 1
            if num == 1:
                count += 1          
            else:
                #见0就比较计数器和结果，取最大值 / See 0 to compare the counter with the result, take the maximum value
                result = max(count,result)   
                  #计数器清零，（准备后面的计数） / Clear the counter, (prepare the subsequent count)
                count = 0          
        return max(count,result)   
