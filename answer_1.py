def find_process(start,stop,n):
    process = []
    for s,e in zip(start,stop):
        if not process:
            process.append(e)
            continue
        free_process = [i for i in process if i<=s]
        if free_process:
            process[process.index(free_process[0])] = e
        else:
            process.append(e)
    return len(process)

if __name__ == "__main__":
    start = [900,940,950,1000,1500,1600]
    stop = [910,1020,1010,1015,1620,1700]
    n = len(start)
    count = find_process(start,stop,n)
    print(count)
