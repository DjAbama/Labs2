import time

q = {}

def enqueue(queue, item, priority):
    if item in queue:
        print(item, "is already in the queue")
        return
    else:
        queue[item] = {
            "priority": priority,
            "time": time.time()
        }
    return queue

enqueue(q, "task1", 1)
enqueue(q, "task2", 2)
