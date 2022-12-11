import datetime
from threading import Thread
from multiprocessing import Process


def count_ticket(start, end):
    count = 0
    for i in range(start, end):
        num = str(i).rjust(6, '0')
        if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
            count += 1
    print(f'${count}$')
    return count

if __name__ == '__main__':
    time_start = datetime.datetime.now()
    count_ticket(0, 1000000)
    print(f'#{datetime.datetime.now() - time_start}#')
    print('-------------')

    time_start = datetime.datetime.now()
    race_1 = Thread(target=count_ticket, args=[0, 250000])
    race_2 = Thread(target=count_ticket, args=[250000, 500000])
    race_3 = Thread(target=count_ticket, args=[500000, 750000])
    race_4 = Thread(target=count_ticket, args=[750000, 1000000])

    race_1.start()
    race_2.start()
    race_3.start()
    race_4.start()

    race_1.join()
    race_2.join()
    race_3.join()
    race_4.join()

    print(f'#{datetime.datetime.now() - time_start}#')
    print('-------------')
    time_start = datetime.datetime.now()
    race_1 = Process(target=count_ticket, args=(0, 250000))
    race_2 = Process(target=count_ticket, args=(250000, 500000))
    race_3 = Process(target=count_ticket, args=(500000, 750000))
    race_4 = Process(target=count_ticket, args=(750000, 1000000))

    race_1.start()
    race_2.start()
    race_3.start()
    race_4.start()

    race_1.join()
    race_2.join()
    race_3.join()
    race_4.join()

    print(f'#{datetime.datetime.now() - time_start}#')


