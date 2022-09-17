<!--
 * @Author: Vincent Young
 * @Date: 2022-09-15 14:18:33
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-09-15 15:38:31
 * @FilePath: /FuckSheepGame/README.md
 * @Telegram: https://t.me/missuo
 * 
 * Copyright © 2022 by Vincent, All Rights Reserved. 
-->
# FuckSheepGame
羊了个羊刷通关次数

## 更新日志
### 2022年9月17日
- 修改接口为最新的 `map_info_new` 

## 写在前面
- 本 Repo 仅供学习使用，禁止用于任何盈利为目的的用途。如有任何后果，作者概不负责。
- 如果您没有开发的基础，可能对您来说会相对困难一些，当然也鼓励您尝试一下本通关方案。
- 由于需要篡改 HTTPS 的请求，所以必须要在你的手机上安装证书，并且在关于本机 - 证书信任设置里面信任证书。
- QuanX 需要安装并且信任证书后，开启MITM和Rewrite。
- HTTP Catcher 需要开启解密HTTPS流量，并且开启重写列表。
- 截止到2022年9月17日21点43分依然可用，如果遇到无法进入游戏，可能是服务器崩溃。（我会每天更新可用情况）
- 如有任何疑问，请在 [Issues](https://github.com/missuo/FuckSheepGame/issues/new) 中提问，我会尽快为您解答。

## 第二关过关方式
使用 `MITM` 篡改请求，将 `map_id` 的 `90014` 修改为 `80001` 即可。这样子你的第二关地图也会变成第一关的地图。
> iOS上可以使用 `QuanX`、`Surge`、`HTTP Catcher`，Android上 **没试过** 。

### `Surge` 模块

开发中...

### `QuanX` 脚本(**强烈推荐**)
```
# 羊了个羊 通关
https://raw.githubusercontent.com/missuo/FuckSheepGame/main/sheep.js
, tag=Sheep, update-interval=172800, opt-parser=true, enabled=true
```
复制上面的代码，粘贴到`QuanX`配置文件的`[rewrite_remote]`下。如果没有添加过资源解析器，请在`[general]`下添加以下代码。

```
# 资源解析器，自定义各类远程资源的转换
resource_parser_url=https://cdn.jsdelivr.net/gh/KOP-XIAO/QuantumultX@master/Scripts/resource-parser.js
```

### `HTTP Catcher` 重写规则
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
      "path" : "\/sheep\/v1\/game\/map_info_new"
    }
  ]
}
```


## 刷通关次数
修改 `t` 为你自己的 `cookies` ，运行脚本，运行一次通关一次。 `Cookies` 可以使用 `Stream` `HTTP Catcher` `Proxyman` 等工具安装信任证书开启解密HTTPS后打开游戏抓取。
```python
pip3 install requests
python3 sheep.py
```
