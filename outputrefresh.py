import pandas as pd
from ipcheckv2 import ipcheck
from collections import Counter

phonecsv = pd.read_csv('phone_list.csv')
phonecsv.columns = ['-----', 'mac-address', 'Ip address', 'current user', 'home user']
phonecsv.drop(columns=['-----'], axis=1, inplace=True)

ip_list = (phonecsv['Ip address'].tolist())
print(ipcheck(ip_list))


'''
ip_list = (phonecsv['Ip address'].tolist())
fin_list = ipcheck(ip_list)
order_summary = Counter(fin_list)
print(order_summary)
'''