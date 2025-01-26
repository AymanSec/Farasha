import threading

a = 1,2,3,4,5
b = []

for i in a:
 
 b.append(i)
    
t1 = threading.Thread(print("subd:",b[-1]))
t1.start()
t1.join()
    




