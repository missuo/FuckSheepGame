<!--
 * @Author: Vincent Young
 * @Date: 2022-09-15 14:18:33
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-09-15 15:27:39
 * @FilePath: /FuckSheepGame/README.md
 * @Telegram: https://t.me/missuo
 * 
 * Copyright © 2022 by Vincent, All Rights Reserved. 
-->
# FuckSheepGame
羊了个羊刷通关次数

## 第二关过关方式
使用 `MITM` 篡改请求，将 `map_id` 的 `90014` 修改为 `80001` 即可。这样子你的第二关地图也会变成第一关的地图。
> iOS上可以使用 `QuanX`、`Surge`、`HTTP Catcher`，Android上 **没试过** 。

`Surge` 模块

`https://raw.githubusercontent.com/missuo/FuckSheepGame/main/sheep.sgmodule`

`QuanX` 脚本
```
# 羊了个羊 通关
https://raw.githubusercontent.com/missuo/FuckSheepGame/main/sheep.js
, tag=Sheep, update-interval=172800, opt-parser=true, enabled=true
```

`HTTP Catcher` 重写规则
```json
{
  "rules" : [
    {
      "action" : "modify-query",
      "matchField" : "map_id",
      "field" : "",
      "value" : "80001",
      "matchValue" : "",
      "destiontion" : "request",
      "isRegex" : false
    }
  ],
  "enabled" : true,
  "name" : "羊羊羊",
  "description" : "羊羊羊",
  "locations" : [
    {
      "method" : "GET",
      "scheme" : "https",
      "enabled" : true,
      "port" : 0,
      "query" : "",
      "host" : "cat-match.easygame2021.com",
      "path" : "\/sheep\/v1\/game\/map_info"
    }
  ]
}
```


## 刷通关次数
修改 `t` 为你自己的 `cookies` ，运行脚本，运行一次通关一次。
```python
pip3 install requests
python3 sheep.py
```
