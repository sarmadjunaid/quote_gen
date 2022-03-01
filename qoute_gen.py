import requests

def get_random_qoute():
    try:
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']

            print(data[0]['quoteText'])
        else:
            print('Error while getting quote')
    except:
        print('Something went wrong! Try Again')

get_random_qoute()