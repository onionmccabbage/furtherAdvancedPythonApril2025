import asyncio

# we use async and await together
async def handleRequests(reader, writer):
    '''This server will expect to receive requests from clients
    Responses will be simple'''
    data = await reader.read(1024) # read in the first 1024 bytes from the incoming data stream
    message = data.decode() # convert the bytes to a string
    addr = writer.get_extra_info('peername')
    print(f'Received {message} from {addr}')

async def main():
    '''start the microservice server'''
    server = await asyncio.start_server(handleRequests, 'localhost', 8889) # localhost is 127.0.0.1
    print('Server started')
    # the server needs to run endlessly
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run( main() )