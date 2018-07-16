import csv


def inputdata(file,data):
    for i in data:
        print(i)

def writedatatofile(file,data):
    pencil = pen.writer(file,delimiter(','))
    for j in pencil:
        pen.writerow(i)



file = open('samepleuser.txt','w')
data = ['username,password,organization'.split(','),
                  'lingesh,1234,oracle'.split(','),
                  'kumar,3455,oracle'.split(','),
                  'ram,8787,oracle'.split(',')]
inputdata(file,data)
writedatatofile(file,data)



