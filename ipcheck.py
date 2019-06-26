def ipcheck(ip_list):

    location_list = []

    for ip in ip_list:
        if '192.168.120' in ip:
            location_list.append('Princeton')
            
        elif '172.16.0.0' in ip:
            location_list.append('HQ')

        elif '172.16.5' in ip:
            location_list.append('HQ')

        elif '172.16.4' in ip:
            location_list.append('HQ')

        elif '172.16.3' in ip:
            location_list.append('HQ')

        elif '172.16.2' in ip:
            location_list.append('HQ')

        elif '172.16.1' in ip:
            location_list.append('HQ')
            
        elif '192.168.15' in ip:
            location_list.append('Mansfield, TX')
            
        elif '192.168.157' in ip:
            location_list.append('Mansfield, TX')

        elif '192.168.100' in ip:
            location_list.append('Loudon')

        elif '192.168.175' in ip:
            location_list.append('PNC')

        elif '192.168.57' in ip:
            location_list.append('Toledo')

        elif '192.168.171' in ip:
            location_list.append('Brentwood, TN')

        elif '192.168.170' in ip:
            location_list.append('Winchester')

        elif '192.168.140' in ip:
            location_list.append('Zellwood')

        elif '192.168.160' in ip:
            location_list.append('Nashville, TN')

        elif '192.168.118' in ip:
            location_list.append('Mobile, AL')

        elif '192.168.116' in ip:
            location_list.append('Elizabeth, NJ')

        elif '192.168.153' in ip:
            location_list.append('Hope, Arkansas')

        elif '192.168.137' in ip:
            location_list.append('Houston, TX')

        elif '192.168.141' in ip:
            location_list.append('Leeds, AL')

        elif '192.168.122' in ip:
            location_list.append('Emporia, VA')

        elif '192.168.124' in ip:
            location_list.append('Memphis, TN')

        elif '192.168.108' in ip:
            location_list.append('Witchata Falls, TX')

        elif '192.168.17' in ip:
            location_list.append('Petersburg, VA')

        elif '192.168.125' in ip:
            location_list.append('Accounting BHAM')

        elif '192.168.127' in ip:
            location_list.append('Patlaka, FL')

        elif '192.168.161' in ip:
            location_list.append('Dublin, GA')

        elif '192.168.177' in ip:
            location_list.append('Tuscaloosa, AL')

        elif '192.168.131' in ip:
            location_list.append('Columbiana, OH')

        elif '192.168.129' in ip:
            location_list.append('McWayne Building')

        else:
            location_list.append('unknown')

    return location_list