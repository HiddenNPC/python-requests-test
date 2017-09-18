if __name__ == '__main__':
    import json
    from website_grabber import mypost

    url = ''
    payload = {
        '': '',
        '': ''
    }
    jsonfy_payload = json.dumps(payload)
    mypost.mypost(url, jsonfy_payload)
