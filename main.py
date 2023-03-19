# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threadCount = n
    threads = []
    while threadCount:
        threads.append(0)
        threadCount -= 1

    jobs = m
    jobList = data

    for j in range(0, jobs):
        current = min(threads)
        currentIndex = threads.index(current)

        
        output.append([currentIndex, threads[currentIndex]])
        threads[currentIndex]=threads[currentIndex]+jobList[j]
            


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    I = input()
    data = list(map(int, I.split()))
    n = data[0]
    m = data[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    I = input()
    data = list(map(int, I.split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
