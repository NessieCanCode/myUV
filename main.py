import sys
import requests


user_zip = sys.argv[1]


def get_parse(arg):
    url = "https://enviro.epa.gov/enviro/efservice/getEnvirofactsUVDAILY/ZIP/"+arg+"/JSON"
    response = requests.get(url)
    data = response.json()
    uv_index = data[0]['UV_INDEX']
    return uv_index


if __name__ == '__main__':
    print(get_parse(user_zip))
