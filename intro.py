from joblib import Parallel, delayed
import multiprocessing
import time

def myfuntion(i):
    print(i)
    time.sleep(2)
    return(i)
if __name__ == '__main__' :
    start = time.time()
    for i in range(10):
        myresults = myfuntion(i)
    print("SERIAL", time.time() - start)
    num_cores = multiprocessing.cpu_count()
    print("NUmber of cores used: " + str(num_cores))
    start = time.time()
    results = Parallel(n_jobs=num_cores)(delayed(myfuntion(i)for i in range(10))
    print("PARALLEL", time.time() - start)
    print(results)

