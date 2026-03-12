import time



def LFU_find(obj):
    least_used = None
    for item in obj:
        if least_used == None:
            least_used = item
        if obj[item][1] < obj[least_used][1]:
            least_used = item
    return least_used

def LRU_find(obj):
    oldest = None
    for item in obj:
        if oldest == None:
            oldest = item
        if obj[item][2] < obj[oldest][2]:
            oldest = item
    return oldest

def Time_find(obj, seconds):
    timeout = None
    for item in obj:
        if time.time() - obj[item][2] > seconds:
            if timeout == None or obj[item][2] < obj[timeout][2]:
                timeout = item
    return timeout
        



def memoizetion(eviction, limit):
    def decorator(func):
        cache = {}
    
        def wrap(*args):
            if args in cache:
                cache[args][1] += 1
                cache[args][2] = time.time()
                return cache[args][0]

            if len(cache) >= limit:
                match eviction:
                    case 'LFU':
                        cache.pop(LFU_find(cache))
                        
                    case 'LRU':
                        cache.pop(LRU_find(cache))

                if type(eviction) == float:
                    if Time_find(cache, eviction) is None:
                        cache.pop(LRU_find(cache))
                    else:
                     cache.pop(Time_find(cache, eviction))

                if callable(eviction):
                    cache.pop(eviction(cache))

            if args not in cache:
                
                res = func(*args)
                cache[args] = [res, 0, 0]
                cache[args][2] = time.time()
                
                return res
            
        return wrap
    return decorator

    
    

@memoizetion('LRU', 4)
def function(a, b):
    return a * b

print(function(1213,112))
print(function(312,3123))
print(function(234,13))
print(function(1412,67))
print(function(1213,112))
print(function(312,3123))
print(function(42,4214))
print(function(1412,67))




