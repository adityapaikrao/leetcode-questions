class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = [] # (priority, task_id)
        self.task_map = {}
        for user_id, task_id, priority in tasks:
            heapq.heappush(self.tasks, [-priority, -task_id])
            self.task_map[task_id] = [priority, user_id]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.tasks, [-priority, -taskId])
        self.task_map[taskId] = [priority, userId]

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.tasks, [-newPriority, -taskId])
        self.task_map[taskId][0] = newPriority

    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]

    def execTop(self) -> int:
        while self.tasks:
            priority, task_id = heapq.heappop(self.tasks)
            priority, task_id = -priority, -task_id
            if task_id in self.task_map:
                curr_priority, user_id = self.task_map[task_id]
                if curr_priority == priority:
                    del self.task_map[task_id]
                    return user_id
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()