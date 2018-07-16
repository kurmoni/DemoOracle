import csv
f=open('D://python_dir//Task1//files//temp.txt','w')
f.write('''
export ORACLE_HOME=/u01/app/oracle/products/dir/oid
export ORACLE_INSTANCE=/u01/app/oracle/config/instances/oid1
export TNS_ADMIN=$ORACLE_INSTANCE/config
export PATH=$ORACLE_HOME/bin:$ORACLE_HOME/ldap/admin:$ORACLE_HOME/bin:$PATH:.

''')

file = open('usercsv.csc','w')
data = ['username,password,organization'.split(','),
                  'lingesh,1234,oracle'.split(','),
                  'kumar,3455,oracle'.split(','),
                  'ram,8787,oracle'.split(',')]
