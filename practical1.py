#-*-coding:utf-8-*-
# b = []
# a = [1,4,5,2,2,6,4,34]
# for i in range(len(a)):
#     b.append(min(a))
#     a.remove(min(a))
# print(b)

def myself_sort(a):
    b = []
    for i in range(len(a)):
        b.append(min(a))
        a.remove(min(a))
    return b

def selection_sort(a):
    b = []
    for i in range(len(a)):
        b.append(min(a))
        a.remove(min(a))
    return b

def bubble_sort(a):
    #a[0],a[1] = a[1],a[0]
    for n in range(1000):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

def insertion_sort(a):
    new=[]
    new.append(min(a))
    new.append(max(a))
    a.remove(min(a))
    a.remove(max(a))
    for i in range(0,len(a)):
        print(i)
        for n in range(len(new)-1):
            if (a[i]>new[n] and a[i]<=new[n+1]):
                m=a[i]
                new.insert(n+1, m)
    return new

if __name__ == '__main__':

    a = [4,1,3,4,90,90,3,5,7]
    #b = myself_sort(a)
    #b = selection_sort(a)
    #b = bubble_sort(a)
    b = insertion_sort(a)
    print(b)


