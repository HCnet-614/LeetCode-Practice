class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int result = 0;        //设置计数器和结果初始值 / Set counter and result initial values
        for (int i =0; i<nums.length; i++){
            if(nums[i] == 1){
                count++;       //见1就给计数器加1 / add 1 to the counter when see 1
            }                           
            else{
                result = Math.max(result,count);   //见0就比较计数器和结果，取最大值 / See 0 to compare the counter with the result, take the maximum value
                count = 0;      //计数器清零，（准备后面的计数） / Clear the counter, (prepare the subsequent count)
            }
        } 
        return Math.max(result,count);
    }
}
