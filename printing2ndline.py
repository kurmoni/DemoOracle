import csv
def writing(fileobj,data):
    pen=csv.writer(fileobj,delimeter=',')

if __name__=='__main__':
    fileobj=open('details.txt','w')
    data=['name,class,phonenumber,address'.split(','),
          'lingeesh,1,123,hyd'.split(','),
          'kumar,2, 456, hyd'.split(', ')]
    writing(fileobj,data)
