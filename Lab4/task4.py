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
    oldest_item = list(obj.keys())[0] 
    return oldest_item
    
def newest(obj):
    newest_item = list(obj.keys())[-1]
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

enqueue(q, "a", 2)
enqueue(q, "b", 0)
enqueue(q, "c", 6)
enqueue(q, "d", 3)
enqueue(q, "e", 1)
enqueue(q, "f", 8)

def peek(queue, strategy):
    match strategy:
        case "highest":
            return highest_priority(queue)
        case "lowest":
            return lowest_priority(queue)
        case "oldest":
            return oldest(queue)
        case "newest":
            return newest(queue)
        
print(peek(q, "highest"))
print(peek(q, "lowest"))    
print(peek(q, "oldest"))
print(peek(q, "newest"))




