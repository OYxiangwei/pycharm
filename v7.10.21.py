import threading
import time
import multiprocessing

movie_list = ['今天.mp4',"后天.mp4","前天.avi","蜘蛛侠.mp4"]
muisc_list = ['快乐.mp3',"爱心.mp3","漂洋过海来看你.mp3"]
movie_format = ['mp4','avi']
muisc_format = ['mp3']
def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("现在看的是电影：{}".format(i))
            time.sleep(1)
        elif i.split(".")[1] in muisc_format:
            print("现在听的是{}".format(i))
            time.sleep(1)
        else:
            print("none")

class MyThread(threading.Thread):
    def __init__(self,playlist):
        super(MyThread, self).__init__()
        self.playlist = playlist
    def run(self):
        play(self.playlist)
if __name__ == "__main__":
    """m1 = MyThread(movie_list)
    m2 = MyThread(muisc_list)
    m1.start()
    m2.start()"""
    t1 = multiprocessing.Process(target=play,args=(movie_list,))
    t2 = multiprocessing.Process(target=play,args=(muisc_list,))
    t1.start()
    t2.start()