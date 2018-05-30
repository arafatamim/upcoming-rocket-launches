#!/usr/bin/env python

import requests, datetime, time

launches_to_fetch = 5   # Max is 5
try:
    target_data = requests.get("https://launchlibrary.net/1.4/launch/next/{0}?status=1".format(launches_to_fetch)).json()
except requests.exceptions.ConnectionError:
    print("You're offline")
    exit()

launch_n = []
all_launches = []
x = 0
for launch in target_data['launches']:
    launch_n.append(target_data['launches'][x]['name']) # launch name
    launch_n.append(target_data['launches'][x]['location']['pads'][0]['name'])  # location
    launch_n.append(
        datetime.datetime.fromtimestamp(target_data['launches'][x]['netstamp'])
        .strftime('%d %B %Y, %I:%m %p'))  # datetime
    launch_n.append(target_data['launches'][x]['missions'][0]['name'])  # primary mission
    launch_n.append(target_data['launches'][x]['missions'][0]['description'])  # mission description
    launch_n.append(target_data['launches'][x]['lsp']['name'])  # launch service provider
    launch_n.append(target_data['launches'][x]['vidURLs'])  # live video url

    all_launches.append(launch_n)
    launch_n = []
    x += 1

# all_launches format:
# [name, location, estimated_datetime, mission_name, mission_desc, lsp, live_url]

print("Rocket launch tracker provided by launchlibrary.net")
print("Provided times are relative to your system time:", time.strftime("%Z"))
print()
y = 0
for item in all_launches:
    print("   +" + "-" * (len(all_launches[y][0]) + 2) + "+")
    print(str(y + 1) + ". | " + all_launches[y][0] + " |")
    print("   +" + "-" * (len(all_launches[y][0]) + 2) + "+")
    print("Estimated time          : " + all_launches[y][2])
    print("Launching from          : " + all_launches[y][1])
    print("Launch service provider : " + all_launches[y][5])
    print("Primary mission         : " + all_launches[y][3])
    print("Mission description     : " + all_launches[y][4])
    if (len(all_launches[y][6]) > 0):
        print("Livestream URL          : " + all_launches[y][6][0])
    print()
    y += 1
