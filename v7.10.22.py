import time
import asyncio
#import await

movie_list = ['今天.mp4',"后天.mp4","前天.avi","蜘蛛侠.mp4"]
muisc_list = ['快乐.mp3',"爱心.mp3","漂洋过海来看你.mp3"]
movie_format = ['mp4','avi']
muisc_format = ['mp3']
@asyncio.coroutine
def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("现在看的是电影：{}".format(i))
            #yield time.sleep(1)
            #await asyncio.sleep(1)
        elif i.split(".")[1] in muisc_format:
            print("现在听的是{}".format(i))
            #yield time.sleep(1)
            #await asyncio.sleep(1)
        else:
            print("none")
loop = asyncio.get_event_loop()
task = [play(movie_list),play(muisc_list)]
loop.run_until_complete(asyncio.wait(task))