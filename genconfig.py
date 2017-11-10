print("Enter the following credentials from https://apps.twitter.com")
consumerKey = input('Consumer Key: ')
consumerKeySecret = input('Consumer Key Secret: ')
accessToken = input('Access Token: ')
accessTokenSecret = input('Access Token Secret: ')


configFileData = """
def get():
    config = {
        'consumerKey': "%s",
        'consumerKeySecret': "%s",
        'accessToken': "%s",
        'accessTokenSecret': "%s"
    }

    return config

""" % (consumerKey, consumerKeySecret, accessToken, accessTokenSecret)

fileHandler = open('config.py', 'w');
fileHandler.write(configFileData)
fileHandler.close()

print("configuration file 'config.py' has been created.")