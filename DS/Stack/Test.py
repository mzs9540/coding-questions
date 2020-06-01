from multiprocessing import Process


def table(var, times):
    print(var*times)


if __name__ == "__main__":  # confirms that the code is under main function
    procs = []
    # instantiating process with arguments
    for i in range(2, 11):
        # print(name)
        proc = Process(target=table, args=(2, i))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
