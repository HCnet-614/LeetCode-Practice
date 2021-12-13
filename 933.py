
class RecentCounter:
    def __init__(self):
        self.q = deque()  # 定义队列
    def ping(self, t: int) -> int:
        # 添加元素
        self.q.append(t)   
         # 判断条件
        while(len(self.q)!= 0 and t - self.q[0]>3000):   
             # 删除最早的元素
            self.q.popleft()   
        # 返回现有的队列长度
        return len(self.q)
