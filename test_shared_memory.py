# SuperFastPython.com
# example of using a barrier with processes
# from time import sleep
# from random import random
# from multiprocessing import Process
# from multiprocessing import Barrier
 
# # target function to prepare some work
# def task(barrier, number):
#     # generate a unique value
#     value = random() * 10
#     # block for a moment
#     sleep(value)
#     # report result
#     print(f'Process {number} done, got: {value}', flush=True)
#     # wait on all other processes to complete
#     barrier.wait()
 
# # entry point
# if __name__ == '__main__':
#     # create a barrier
#     barrier = Barrier(5 + 1)
#     # create the worker processes
#     for i in range(5):
#         # start a new process to perform some work
#         worker = Process(target=task, args=(barrier, i))
#         worker.start()
#     # wait for all processes to finish
#     print('Main process waiting on all results...')
#     barrier.wait()
#     # report once all processes are done
#     print('All processes have their result')

########################################

# SuperFastPython.com
# example of using an event object with processes
# from time import sleep
# from random import random
# from multiprocessing import Process
# from multiprocessing import Event
 
# # target task function
# def task(event, number):
#     # wait for the event to be set
#     print(f'Process {number} waiting...', flush=True)
#     event.wait()
#     # begin processing
#     value = random()
#     sleep(value)
#     print(f'Process {number} got {value}', flush=True)
 
# # entry point
# if __name__ == '__main__':
#     # create a shared event object
#     event = Event()
#     # create a suite of processes
#     processes = [Process(target=task, args=(event, i)) for i in range(5)]
#     # start all processes
#     for process in processes:
#         process.start()
#     # block for a moment
#     print('Main process blocking...')
#     sleep(2)
#     # trigger all child processes
#     event.set()
#     # wait for all child processes to terminate
#     for process in processes:
#         process.join()

########################################

# SuperFastPython.com
# example of using a semaphore
# from time import sleep
# from random import random
# from multiprocessing import Process
# from multiprocessing import Semaphore
 
# # target function
# def task(semaphore, number):
#     # attempt to acquire the semaphore
#     with semaphore:
#         # simulate computational effort
#         value = random()
#         sleep(value)
#         # report result
#         print(f'Process {number} got {value}')
 
# # entry point
# if __name__ == '__main__':
#     # create the shared semaphore
#     semaphore = Semaphore(2)
#     # create processes
#     processes = [Process(target=task, args=(semaphore, i)) for i in range(10)]
#     # start child processes
#     for process in processes:
#         process.start()
#     # wait for child processes to finish
#     for process in processes:
#         process.join()

########################################

# SuperFastPython.com
# example of wait/notify with a condition for processes (Process Condition Variable)
# from time import sleep
# from multiprocessing import Process
# from multiprocessing import Condition
 
# # target function to prepare some work
# def task(condition):
#     # block for a moment
#     sleep(1)
#     # notify a waiting process that the work is done
#     print('Child process sending notification...', flush=True)
#     with condition:
#         condition.notify()
#     # do something else...
#     sleep(1)
 
# # entry point
# if __name__ == '__main__':
#     # create a condition
#     condition = Condition()
#     # wait to be notified that the data is ready
#     print('Main process waiting for data...')
#     with condition:
#         # start a new process to perform some work
#         worker = Process(target=task, args=(condition,))
#         worker.start()
#         # wait to be notified
#         condition.wait()
#     # we know the data is ready
#     print('Main process all done')

########################################
    
# SuperFastPython.com
# example of a reentrant lock for processes
# from time import sleep
# from random import random
# from multiprocessing import Process
# from multiprocessing import RLock
 
# # reporting function
# def report(lock, identifier):
#     # acquire the lock
#     with lock:
#         print(f'>process {identifier} done')
 
# # work function
# def task(lock, identifier, value):
#     # acquire the lock
#     with lock:
#         print(f'>process {identifier} sleeping for {value}')
#         sleep(value)
#         # report
#         report(lock, identifier)
 
# # entry point
# if __name__ == '__main__':
#     # create a shared reentrant lock
#     lock = RLock()
#     # create processes
#     processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
#     # start child processes
#     for process in processes:
#         process.start()
#     # wait for child processes to finish
#     for process in processes:
#         process.join()

########################################

# SuperFastPython.com
# example of a mutual exclusion (mutex) lock for processes
# from time import sleep
# from random import random
# from multiprocessing import Process, Lock
 
# # work function
# def task(lock, identifier, value):
#     # acquire the lock
#     with lock:
#         print(f'>process {identifier} got the lock, sleeping for {value}')
#         sleep(value)
 
# # entry point
# if __name__ == '__main__':
#     # create the shared lock
#     lock = Lock()
#     # create a number of processes with different sleep times
#     processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
#     # start the processes
#     for process in processes:
#         process.start()
#     # wait for all processes to finish
#     for process in processes:
#         process.join()

########################################

# # SuperFastPython.com
# # example of reporting the number of logical cpu cores
# from multiprocessing import cpu_count
# # get the number of cpu cores
# num_cores = cpu_count()
# # report details
# print(num_cores)

########################################

# SuperFastPython.com
# list all active child processes
# from time import sleep
# from multiprocessing import active_children
# from multiprocessing import Process
 
# # function to execute in a new process
# def task():
#     # block for a moment
#     sleep(1)
 
# # entry point
# if __name__ == '__main__':
#     # create a number of child processes
#     processes = [Process(target=task) for _ in range(5)]
#     # start the child processes
#     for process in processes:
#         process.start()
#     # get a list of all active child processes
#     children = active_children()
#     # report a count of active children
#     print(f'Active Children Count: {len(children)}')
#     # report each in turn
#     for child in children:
#         print(child)

########################################

# # SuperFastPython.com
# # example of extending the Process class and adding shared attributes
# from time import sleep
# from multiprocessing import Process
# from multiprocessing import Value
 
# # custom process class
# class CustomProcess(Process):
#     # override the constructor
#     def __init__(self):
#         # execute the base constructor
#         Process.__init__(self)
#         # initialize integer attribute
#         self.data = Value('i', 0)
 
#     # override the run function
#     def run(self):
#         # block for a moment
#         sleep(1.5)
#         print(f'Child initial value: {self.data.value}')
#         # store the data variable
#         self.data.value = 99
#         # report stored value
#         print(f'Child stored: {self.data.value}')
 
# # entry point
# if __name__ == '__main__':
#     # create the process
#     process = CustomProcess()
#     # start the process
#     process.start()
#     # wait for the process to finish
#     print('Waiting for the child process to finish')
#     # block until child process is terminated
#     process.join()
#     # report the process attribute
#     print(f'Parent got: {process.data.value}')

########################################
        
# import time
# from multiprocessing import Pool
# from multiprocessing import Manager


# def test(test_list,i):
#     test_list.remove(i)
#     print("intest : ", test_list)
    

# if __name__ == '__main__':
#     with Manager() as manager:
#         A = manager.list(["leo", "kiki", "eden"])
#         B = ["eden", "kiki"]

#         print("Start : ", A)
#         pool = Pool(processes=2)
#         pool.starmap(test, [(A, K) for K in B])
#         pool.close()
#         pool.join()
#         print("Final : ", A)


########################################
        
# from multiprocessing import Pool
# import time
# A = ["leo", "kiki", "eden", "hello", "toodles", "poodles"]
# B = ["eden", "kiki", "toodles", "poodles"]


# def test(i):
#     global A
#     A.remove(i)
#     print("intest : ",A)


# if __name__ == '__main__':
#     # global A
#     pool = Pool(processes=2)
#     pool.map(test ,B)
#     pool.close()
#     pool.join()
#     print("final : ",A)

########################################

# example of a shared dict in multiprocessing
from multiprocessing import Process, Manager
from time import sleep

def worker(shared_dict, lock, key, value):
    # Simple write (atomic operation - no lock needed)
    shared_dict[key] = value

    print(f"process {key} got the value {value}", flush=True)
    
    # Compound operation: requires a lock
    with lock:
        shared_dict['count'] += 1  # Safely increment

    sleep(20)

if __name__ == '__main__':
    with Manager() as manager:
        # Create shared dictionary and lock
        shared_dict = manager.dict()
        shared_lock = manager.Lock()
        
        # Initialize values
        shared_dict['count'] = 0
        
        # Start worker processes
        processes = []
        for i in range(20):
            p = Process(target=worker, args=(shared_dict, shared_lock, f'key_{i}', i*10))
            processes.append(p)
            p.start()
        
        # Wait for all processes to finish
        for p in processes:
            p.join()
        
        # Print results
        print("Final shared_dict:", dict(shared_dict))
