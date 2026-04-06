import time

q = {}

def highest_priority(obj):
        highest = None
        for key, data in obj.items():
            if highest is None or data["priority"] > obj[highest]["priority"]:
                highest = key
        return highest
    
def lowest_priority(obj):
    lowest = None
    for key, data in obj.items():
        if lowest is None or data["priority"] < obj[lowest]["priority"]:
            lowest = key
    return lowest
    
def oldest(obj):
    oldest_item = None
    for key, data in obj.items():
        if oldest_item is None or data["time"] < obj[oldest_item]["time"]:
            oldest_item = key
    return oldest_item
    
def newest(obj):
    newest_item = None
    for key, data in obj.items():
        if newest_item is None or data["time"] > obj[newest_item]["time"]:
            newest_item = key
    return newest_item

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
