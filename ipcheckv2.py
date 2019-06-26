def ipcheck(ip_list, Key):
    ip_list = list(filter(lambda x: len(x) > 2, arr))

    location_list = []

    for ip in out:
        splitip = ip.split('.')
        locator = int(splitip[3])
        if locator in Key:
            location_list.append(Key[locator])

    return location_list









