import threading
import time

def work(count):
    time.sleep(0.1)
    print("\nname : %s\nargument : %s\n"%(threading.currentThread().getName(), count))
    # 스레드 생성시 인자로 받은 name,count 출력

def main():
    for i in range(5):
        t = threading.Thread(target=work, name="thread %i"%i, args=(i,))
        t.start()

if __name__=="__main__":
    main()