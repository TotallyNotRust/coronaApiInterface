import urllib.request, urllib.error, json, os
from todayToTommorow import getDateTime

'''
Data from https://covid19api.com
'''

while True:
    try:
        file = open("file.txt", "a")
        populations = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json').read().decode())
        with urllib.request.urlopen((x:="https://api.covid19api.com/country/"+input("Please enter a country: ")+"/status/confirmed/live" + getDateTime())) as url:
            print("Data from https://covid19api.com/")
            print("You can find theese numbers at:\n", x, sep = "")
            fulldata = json.loads(url.read().decode())
            print(sum([i['Cases'] for i in fulldata]))
            leng = len(sorted([i['Province' if i['Province'] else 'Country'] for i in fulldata] + [f"{i['Cases']:,}" for i in fulldata], key=len)[-1]) + 2
            for data in fulldata:
                if data['City']:
                    hasNoCity = False
                    break
                hasNoCity = True
            for data in fulldata:
                if data['Province'] or hasNoCity:
                    file.write(f"{data['Province' if data['Province'] else 'Country']}: {data['Cases']:,}\n")
                    print("-"*leng*2)
                    print(("{: <{leng}}"*2).format(data['Province' if data['Province'] else 'Country'], f"{data['Cases']:,}", leng=leng))
            print("-"*leng*2)
            print(("{: <{leng}}"*2).format("Total", f"{(x:= sum([i['Cases'] for i in fulldata if i['City'] or hasNoCity])):,}", leng=leng))
            print("{}".format(str(round(x/[i['population'] for i in populations if i['country'] in fulldata[0]['Country']][0]*1000, 2))),"per 100,000")
            print("-"*leng*2)
            file.close()
    except urllib.error.HTTPError:
        print("You entered an invalid country")
    except Exception as e:
        print(e)
        print("Too many requests are being made right now.\nPlease try again later")
input()