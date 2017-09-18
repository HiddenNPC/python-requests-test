import sys
import requests
import time


def mypost(url, payload):
    start_time = time.time()
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    try:
        res = requests.post(url, data=payload)
        end_time = time.time()
        sys.stdout.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)) + "\n")
        duration = end_time - start_time
        sys.stdout.write('%s seconds!\n' % int(duration))
        sys.stdout.write(res.text)
    except Exception as e:
        if isinstance(e, requests.exceptions.ConnectionError):
            sys.stdout.write("Connection error ")
            sys.stdout.write(str(type(e)))
        elif isinstance(e, requests.exceptions.ConnectTimeout):
            sys.stdout.write("Connection timeout")
            sys.stdout.write(str(type(e)))
        else:
            print e
