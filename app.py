import config
from sys import argv
from twitter import Twitter

twitter = Twitter(config)


if len(argv) == 2:
    msg = argv[1]
    twitter.postOnTimeline(msg)
else:
    print("Last tweet:")
    print(twitter.getLastTimelinePost())


