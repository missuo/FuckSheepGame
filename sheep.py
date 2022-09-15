'''
Author: Vincent Young
Date: 2022-09-15 12:22:40
LastEditors: Vincent Young
LastEditTime: 2022-09-15 12:31:02
FilePath: /FuckSheepGame/sheep.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''

import requests, json

# Clearance time
rank_time = 12

# User Cookies
t = "MODIFY_HERE"

url = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time={}&rank_role=1&skin=1".format(str(rank_time))

headers = {'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c25) NetType/WIFI Language/en", "t": t}

r = requests.get(url = url, headers = headers).text
rj = json.loads(r)
print(rj)