import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://youtu.be/lgoB3_-ejnI?si=27e64xLjXJ5wqADM"
  response = requests.get(URL)
  open("instagram.mp4", "wb").write(response.content)

  
async def function2():
  print("func 2") 
  URL = "https://youtu.be/lgoB3_-ejnI?si=27e64xLjXJ5wqADM"
  response = requests.get(URL)
  open("instagram2.mp4", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://youtu.be/lgoB3_-ejnI?si=27e64xLjXJ5wqADM"
  response = requests.get(URL)
  open("instagram3.mp4", "wb").write(response.content)

async def main():
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
asyncio.run(main())


