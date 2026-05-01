import asyncio
import aiofiles

async def read():
    async with aiofiles.open("file.txt", mode="r") as file:
        async for string in file:
            yield string




    
