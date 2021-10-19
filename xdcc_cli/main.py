import urllib.request, json, pandas as pd, sys, os, re

def xdcc_get():
    search = input('Search Query: ')
    search = re.sub(' ', '%20', search)
    url = "https://sunxdcc.com/deliver.php?sterm=" + search
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    df = pd.DataFrame(data)

    channels = ['#Batcave', '#ELITEWAREZ', '#moviegods']
    df = df[df['channel'].isin(channels)].reset_index()
    df = df[['network', 'channel', 'bot', 'packnum', 'gets', 'fsize', 'fname']]
    print(df)

    try:
        selection = int(input('Choose which file to download: '))
    except:
        print('Non-integer input')
        sys.exit()

    print(df.iloc[selection])

    channel = df.iloc[selection]['channel']
    bot = df.iloc[selection]['bot']
    packnum = re.sub('#', '', df.iloc[selection]['packnum'])

    os.system(f'xdcc -c \'{channel}\' \'{bot}\' send \'{packnum}\'')

if __name__ == "__main__":
    xdcc_get()





