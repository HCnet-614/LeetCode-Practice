
class RecentCounter {
    Queue<Integer> q;  // 定义队列
    public RecentCounter() {
        q= new LinkedList<>();
    }
    public int ping(int t) {
         // 添加元素
        q.add(t);   
        // 判断条件
        while(!q.isEmpty() && t - q.peek() > 3000 ){ 
             // 删除最早的元素 
            q.poll();   
        }
        // 返回现有的队列长度
        return q.size();  
    }
}
