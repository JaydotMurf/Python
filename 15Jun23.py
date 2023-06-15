import time
import concurrent.futures


def queue_time(customers, n):
    start = time.perf_counter()

    def execution_duration(duration):
        print(f"Started sleeping duration of {duration} ")
        time.sleep(duration)
        print(f"Done Sleeping duration of {duration} ")

    with concurrent.futures.ThreadPoolExecutor(n) as executor:
        results = [
            executor.submit(execution_duration, wait_time) for wait_time in customers
        ]

    finish = time.perf_counter()

    print(f"Total duration: {round(finish-start)}")
    return round(finish - start)


queue_time([2, 3, 10], 2)
