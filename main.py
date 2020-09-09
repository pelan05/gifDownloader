import requests
import json

if __name__ == '__main__':

    # Load file with urls
    with open('urlsBr.json') as json_file:
        data = json.load(json_file)

    for x in data['urls']:
        # Get gif name from url (specific to each cenario)
        uri = x['url']
        gifNumber = uri.split('/')[len(uri.split('/')) - 2]
        gifNumber += '_'
        gifNumber += uri.split('/')[len(uri.split('/')) - 1]

        # Save gif in the end
        with open('gifs/' + gifNumber + '.gif', 'w+b') as f:
            f.write(requests.get(uri).content)
            print('written gif ' + gifNumber)

