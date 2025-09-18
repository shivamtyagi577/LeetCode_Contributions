class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Maps taskId to (userId, priority)
        self.task_info = {}

        # Max heap of (-priority, -taskId)
        self.max_heap = []

        for userId, taskId, priority in tasks:
            self.task_info[taskId] = (userId, priority)
            heapq.heappush(self.max_heap, (-priority,-taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId,priority)
        heapq.heappush(self.max_heap, (-priority,-taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId,newPriority)
        heapq.heappush(self.max_heap, (-newPriority,-taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.max_heap:
            priority, taskId = heapq.heappop(self.max_heap)
            taskId = -taskId
            priority = -priority
            if taskId in self.task_info and self.task_info[taskId][1] == priority:
                userId = self.task_info[taskId][0]
                del self.task_info[taskId]
                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()