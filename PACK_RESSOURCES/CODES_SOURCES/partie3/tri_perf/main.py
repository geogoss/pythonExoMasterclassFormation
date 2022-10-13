import time
import random



def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i          #   V            m
        l[min_index] = l[unsorted_index]   #  [5, 8, 10, 2, 5]
        l[unsorted_index] = min            #  [1, 8, 10, 2, 5]


def bubble_sort(l):
    nb_permut = 1
    while nb_permut != 0:
        nb_permut = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                nb_permut += 1
                a = l[i]
                l[i] = l[i+1]
                l[i+1] = a


def quicksort(l):
    qsort_loop(l, 0, len(l)-1)

def qsort_loop(l, imin, imax):
    if imax-imin == 1:
        if l[imin] > l[imax]:
            '''c = l[imin]
            l[imin] = l[imax]
            l[imax] = c'''
            l[imin], l[imax] = l[imax], l[imin]
        return
    if imax-imin == 0:
        return

    p = l[imax]
    a = 0
    for i in range(imin, imax):
        if l[i] <= p:
            l[a+imin], l[i] = l[i], l[a+imin]
            a += 1
    l[a+imin], l[imax] = p, l[a+imin]
    if a != 0:
        qsort_loop(l, imin, a+imin-1)
    if imax > a+imin+1 :
        qsort_loop(l, a+imin+1, imax)                       


l1 = generate_random_list(1000, 0, 10000)
l2 = l1.copy()
l3 = l1.copy()
l4 = l1.copy()

t1 = time.time_ns()
selection_sort(l1)
t2 = time.time_ns()
bubble_sort(l2)
t3 = time.time_ns()
quicksort(l3)
t4 = time.time_ns()
l4.sort()
t5 = time.time_ns()

selection_t = t2-t1
bubble_t = t3-t2
quick_t = t4-t3
sortpy_t = t5-t4

print("(ms)")
print("selection:", selection_t/1000000)
print("bubble:", bubble_t/1000000)
print("quicksort:", quick_t/1000000)
print("sort():", sortpy_t/1000000)

