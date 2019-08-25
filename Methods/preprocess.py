def login(email, password, Client):
    try:
        client = Client(email,password,session_cookies=cookies)
    except:
        client = Client(email,password)
    return client