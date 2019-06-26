import pandas as pd
from ipcheck import ipcheck

Key = {
    0:'HQ',
    1:'HQ',
    2:'HQ',
    3:'HQ',
    4:'HQ',
    5:'HQ',
    120: 'Princeton',
    157: 'Mansfield, TX',
    15: 'Mansfield, TX',
    100: 'Loudon',
    175: 'PNC',
    57: 'Toledo',
    171: 'BrentWood, TN',
    170: 'Wichester',
    140: 'Zellwood',
    160: 'Nashville, TN',
    118: 'Mobile, Al',
    116: 'Elizabeth, NJ',
    153: 'Hope, Arkansas',
    137: 'Houston, TX', 
    141: 'Leeds, AL', 
    122: 'Emporia, VA', 
    124: 'Memphis, TN',
    108: 'Witchata Falls, TX',
     17: 'Petersburg, VA',
    125:'Accounting BHAM',
    127: 'Patlaka, FL',
    161: 'Dublin, GA',
    177: 'Tuscaloosa, AL'
    }

phonecsv = pd.read_csv('phone_list.csv')
phonecsv.columns = ['-----', 'mac-address', 'Ip address', 'current user', 'home user']
phonecsv.drop(columns=['-----', 'home user'], axis=1, inplace=True)


'''location = ipcheck(phonecsv['Ip address'].tolist())
print(phonecsv)
print(location)'''

ip_list = (phonecsv['Ip address'].tolist())
fin_list = ipcheck(ip_list, Key)
print(fin_list)
