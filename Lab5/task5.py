async def Map(arr, func):
    res = []
    for item in arr:
        new_item = await func(item)
        res.append(new_item)
    return res
