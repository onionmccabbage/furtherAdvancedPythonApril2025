import requests

def getWeather(buf_str='aachen'):
    url_template = f'http://api.openweathermap.org/data/2.5/weather?q={buf_str}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
    print(f'server is trying {url_template}')
    response = requests.get(url_template)
    data = response.json()
    print(f'Server received {data}')
    # read one part of the weahter report
    descr = data['weather'][0]['description']
    # send a response to the client
    # response = buf.upper()
    # client.send(response)
    return descr.encode()