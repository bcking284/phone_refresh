
from collections import Counter
def ipcheck(ip_list):
    ip_dict={
    '0':'HQ',
    '1':'HQ',
    '2':'HQ',
    '3':'HQ',
    '4':'HQ',
    '5':'HQ',
    '120': 'Princeton',
    '157': 'Mansfield, TX',
    '15': 'Mansfield, TX',
    '100': 'Loudon',
    '175': 'PNC',
    '57': 'Toledo',
    '171': 'BrentWood, TN',
    '170': 'Wichester',
    '140': 'Zellwood',
    '160': 'Nashville, TN',
    '118': 'Mobile, Al',
    '116': 'Elizabeth, NJ',
    '153': 'Hope, Arkansas',
    '137': 'Houston, TX', 
    '141': 'Leeds, AL', 
    '122': 'Emporia, VA', 
    '124': 'Memphis, TN',
    '108': 'Witchata Falls, TX',
    '17': 'Petersburg, VA',
    '125':'Accounting BHAM',
    '127': 'Patlaka, FL',
    '161': 'Dublin, GA',
    '177': 'Tuscaloosa, AL'
    }

    
    location_list = []
    locator = ''
    for ip in ip_list:
        splitip = ip.split('.')

        if len(splitip) > 1:
            locator = splitip[2]
        else:
            location_list.append("Unknown")
        if locator in ip_dict.keys():
            location_list.append(ip_dict[locator])

        locator = int(splitip[2])
        if locator in Key:
            location_list.append(Key[locator])
        else: location_list.append("Unknown")

    return Counter(location_list)







