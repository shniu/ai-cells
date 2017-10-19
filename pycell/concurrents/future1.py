
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def return_future_result(message):
    # time.sleep(1)
    return message


def thread_example():
    pool = ThreadPoolExecutor(max_workers=2)

    f1 = pool.submit(return_future_result, ('hello',))
    f2 = pool.submit(return_future_result, ('world',))

    print(f1.done())
    time.sleep(5)
    print(f2.done())

    print(f1.result())
    print(f2.result())


def process_example():
    pool = ProcessPoolExecutor(max_workers=2)

    f1 = pool.submit(return_future_result, ('hello',))
    f2 = pool.submit(return_future_result, ('world',))

    print(f1.done())
    time.sleep(5)
    print(f2.done())

    print(f1.result())
    print(f2.result())


if __name__ == '__main__':
    thread_example()
    process_example()
