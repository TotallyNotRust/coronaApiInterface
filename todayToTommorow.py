import datetime

def getDateTime():
    x = datetime.datetime.now() - datetime.timedelta(1)
    y = datetime.datetime.now()
    return "?from=" + x.strftime("%Y-%m-%d") + "T00:00:00Z" + "&to=" + y.strftime("%Y-%m-%d") + "T00:00:00Z"

if __name__ == "__main__":
    print(getDateTime())