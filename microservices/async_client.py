import asyncio

async def my_client(message):
    '''a simple asynchronous client
    send a message to the async server'''
    reader, writer = await asyncio.open_connection('localhost', 8889)
    print(f'Sending {message}')
    writer.write(message.encode()) # all communication over http needs to be encoded
    await writer.drain() # asynchronously wait until the writer has completed
    writer.close()

if __name__ == '__main__':
    asyncio.run(my_client('is it coffee yet'))