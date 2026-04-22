async def Map_promise(arr, func):
    res = []
    for item in arr:
        new_item = await func(item)
        res.append(new_item)
    return res

async def Map_callback(arr, func, callback_final):
    res = []
    
    def Function(index):
        
        if index < len(arr):

            def callback(new_item):
                res.append(new_item)
                Function(index + 1)

            func(arr[index], callback)

        else:
            callback_final(res)


    Function(0)

array = [18, 52, 67, 228, 45, 90, 123, 11]

def add(item):
    return item + 100

def add_callback(item, callback):
    callback(item + 100)

print(Map_promise(array, add))  
print(Map_callback(array, add_callback))    