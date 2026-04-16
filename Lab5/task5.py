async def Map_promise(arr, func):
    res = []
    for item in arr:
        new_item = await func(item)
        res.append(new_item)
    return res

async def Map_callback(arr, func, callback_final):
    res = []
    
    def Function(index):
        
        while (index < len(arr)):
            def callback(new_item):
            res.append(new_item)
            Function(index + 1)
            func(arr[index], callback)

    callback_final(res) 
    return
    Function(0)
