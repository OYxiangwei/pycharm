import _thread as thread
import time
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

def thread_run():
    thread.start_new_thread(play,(movie_list,))
    thread.start_new_thread(play,(muisc_list,))

if __name__ =="__main__":
    thread_run()
    time.sleep(6)