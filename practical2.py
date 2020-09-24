#-*-coding:utf-8-*-
import csv


def method1():
    with open("/Users/cuijiajun/Desktop/BMI3/practical2/example5.csv", "r") as f:
        reader = csv.reader(f)
        ls = list(reader)
        N = ls[0][0]
        M = int(ls[0][1])
        extra = float(ls[0][2])
        c19data = ls
        c19data.pop(0)
        survival = []
        druglist = [0]*len(c19data)
        norepdata = []
        times = []
        surnumbers = []
        results = []
        for i in range(len(c19data)):
            druglist[i] = c19data[i][0:M]
            if druglist[i] not in norepdata:
                norepdata.append(druglist[i])
            if c19data[i][M]!="0":
                survival.append(c19data[i][0:M])

        for i in range(len(norepdata)):
            time = druglist.count(norepdata[i])
            times.append(time)
            surnumber = survival.count(norepdata[i])
            surnumbers.append(surnumber)
            results.append(surnumber/(time+extra))
        reslist = []

        for i in range(len(norepdata)):
            if results[i] == max(results):
                reslist.append(norepdata[i])
        for i in range(len(reslist)):
            reslist[i] = [int(x) for x in reslist[i]]
        print(reslist)
        print(max(results))
if __name__ == '__main__':
        method1()
#space complexity: O(n)
#time complexity: O(n)

