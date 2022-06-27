import json
import requests


def lambda_handler(event, context):
#UV index Scale:
#1 - 2  1 Low (Green) No protection needed. You can safely stay outside using minimal sun protection.
#3 - 5  2 Moderate (Yellow) Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.
#6 - 7  3 High (Orange) Protection needed. Seek shade during late morning through mid-afternoon. When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, and wear protective clothing, a wide-brimmed hat, and sunglasses.
#8 - 10 4 Very High (Red) Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of  SPF-15, broad-spectrum sunscreen on exposed skin.
#11+    5 Extreme (Purple) Extra protection needed. Be careful outside, especially during late morning through mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, a wide-brimmed hat, and sunglasses, and generously apply a minimum of  SPF-15, broad-spectrum sunscreen on exposed skin.
    users_zip = event['queryStringParameters']['users_zip']
    url = "https://enviro.epa.gov/enviro/efservice/getEnvirofactsUVDAILY/ZIP/" + users_zip + "/JSON"
    
    response = requests.get(url)
    data = response.json()
    uv_index = data[0]['UV_INDEX']
    uv_alert = data[0]['UV_ALERT']
    if uv_index in range(0, 3):
        uv_icon = 37949
        uv_recommend="You can safely enjoy being outside. Wear sunglasses on bright days. If you burn easily, cover up and use sunscreen SPF 30+. In winter, reflection off snow can nearly double UV strength."
    elif uv_index in range(2, 6):
        uv_icon = 37950
        uv_recommend="Take precautions if you will be outside, such as wearing a hat and sunglasses and using sunscreen SPF 30+. Reduce your exposure to the sun's most intense UV radiation by seeking shade during midday hours."
    elif uv_index in range(5, 8):
        uv_icon = 37951
        uv_recommend="Protection against sun damage is needed. Wear a wide-brimmed hat and sunglasses, use sunscreen SPF 30+ and wear a long-sleeved shirt and pants when practical. Reduce your exposure to the sun's most intense UV radiation by seeking shade during midday hours."
    elif uv_index in range(7, 11):
        uv_icon = 37952
        uv_recommend="Protection against sun damage is needed. If you need to be outside during midday hours between 10 a.m. and 4 p.m., take steps to reduce sun exposure. A shirt, hat and sunscreen are a must, and be sure you seek shade. Beachgoers should know that white sand and other bright surfaces reflect UV and can double UV exposure."
    elif int(uv_index) >= 11:
        uv_icon = 37953
        uv_recommend="Protection against sun damage is needed. If you need to be outside during midday hours between 10 a.m. and 4 p.m., take steps to reduce sun exposure. A shirt, hat and sunscreen are a must, and be sure you seek shade. Beachgoers should know that white sand and other bright surfaces reflect UV and can double UV exposure."
    else:
        uv_icon = 8524
        uv_recommend="...There might be something wrong."
    api_response = {
    "frames": [
        {
            "text": "Daily forecasted UV index: "+ str(uv_index) + ", Sun Protection Messages: " + str(uv_recommend),
            "icon": uv_icon
        }
    ]
}
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(api_response)

    return response_object
