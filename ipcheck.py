def ipcheck(ip_list):

    location_list = []

    for ip in ip_list:
        if '.120' in ip:
            location_list.append('Princeton')
            '''
        
        elif '172.16.0.0' or '172.16.1' or '172.16.2' or '172.16.3' or '172.16.4' or '172.16.5' in ip:
                location_list.append('HQ')
            '''
        elif '.15' or '.157' in ip:
            location_list.append('Mansfield, TX')

        elif '.100' in ip:
            location_list.append('Loudon')

        elif '.175' in ip:
            location_list.append('PNC')

        elif '.57' in ip:
            location_list.append('Toledo')

        elif '.171' in ip:
            location_list.append('Brentwood, TN')

        elif '.170' in ip:
            location_list.append('Winchester')

        elif '.140' in ip:
            location_list.append('Zellwood')

        elif '.160' in ip:
            location_list.append('Nashville, TN')

        elif '.118' in ip:
            location_list.append('Mobile, AL')

        elif '.116' in ip:
            location_list.append('Elizabeth, NJ')

        elif '.153' in ip:
            location_list.append('Hope, Arkansas')

        elif '.137' in ip:
            location_list.append('Houston, TX')

        elif '.141' in ip:
            location_list.append('Leeds, AL')

        elif '.122' in ip:
            location_list.append('Emporia, VA')

        elif '.124' in ip:
            location_list.append('Memphis, TN')

        elif '.108' in ip:
            location_list.append('Witchata Falls, TX')

        elif '.17' in ip:
            location_list.append('Petersburg, VA')

        elif '.125' in ip:
            location_list.append('Accounting BHAM')

        elif '.127' in ip:
            location_list.append('Patlaka, FL')

        elif '.161' in ip:
            location_list.append('Dublin, GA')

        elif '.177' in ip:
            location_list.append('Tuscaloosa, AL')

        elif '.131' in ip:
            location_list.append('Columbiana, OH')

        elif '.129' in ip:
            location_list.append('McWayne Building')

        else:
            location_list.append('unknown')

    return location_list