import pandas as pd
from ipcheck import ipcheck

phonecsv = pd.read_csv('phone_list.csv')
phonecsv.columns = ['-----', 'mac-address', 'Ip address', 'current user', 'home user']
phonecsv.drop(columns=['-----', 'home user'], axis=1, inplace=True)


'''location = ipcheck(phonecsv['Ip address'].tolist())
print(phonecsv)
print(location)'''

ip_list = (phonecsv['Ip address'].tolist())
fin_list = ipcheck(ip_list)
print(fin_list)
