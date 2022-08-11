#First real project. Wish me luck & any help is appreciated!

from pytube import YouTube
from sys import argv

link = argv[1]
ytvideo = YouTube(link)

print("Title: ", ytvideo.title)

print("Views: ", yt.views)

ydvid = ytvideo.streams.get_highest_resolution

yd.download('D:\Video making and such\Funny Videos')