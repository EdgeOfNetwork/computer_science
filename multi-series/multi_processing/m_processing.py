import time
import multiprocessing

s = time.time()


def count(name):
    for i in range(1, 50001):
        print(name, " : ", i)


num_list = ['p1', 'p2', 'p3', 'p4']

if __name__ == '__main__':
    # 멀티 스레딩 pool 사용
    pool = multiprocessing.Pool(processes=4)  # process num which use current system
    pool.map(count, num_list)
    pool.close()
    pool.join()

print("------%s seconds ----" % (time.time() - s))
