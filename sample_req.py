import requests # you may need to pip install requests

def getWeather():
    '''use requests to fetch some weather'''
    url = f'http://api.openweathermap.org/data/2.5/weather?q=genoa&units=metric&APPID=957d663a2296945e39a56609740a2548'
    w = requests.get(url)
    response_obj = w.json()
    return f"{response_obj['weather'][0]['description']}"

if __name__ == '__main__':
    w=getWeather()
    print(w)