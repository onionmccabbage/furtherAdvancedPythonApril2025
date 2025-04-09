import asyncio
# the asyncio library will manage threading on our behalf.
# it is also designed to work wth asynchronous code
import time

# async-await is a common pattern across many languages
async def countA():
    print('first do this...')
    await asyncio.sleep(2)
    print('then do that')

async def countB():
    print('first do this...')
    await asyncio.sleep(2)
    print('then do that')

async def main():
    # run our count functions procedurally 
    await countA()
    await countB()
    # instead we can run these as co-routines(where Python manages the threading)
    await asyncio.gather(countA(), countB(), countA(), countA(), countA())

if __name__ == '__main__':
    asyncio.run(main())