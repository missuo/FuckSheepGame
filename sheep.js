/*
 * @Author: Vincent Young
 * @Date: 2022-09-15 15:21:34
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-09-15 15:21:49
 * @FilePath: /FuckSheepGame/sheep.js
 * @Telegram: https://t.me/missuo
 * 
 * Copyright © 2022 by Vincent, All Rights Reserved. 
 */
/*
[rewrite_local]
# > Fuck Sheep Game
^https?:\/\/cat-match\.easygame2021\.com\/sheep\/v1\/game\/map_info url script-request-header https://raw.githubusercontent.com/missuo/FuckSheepGame/main/sheep.js
[mitm] 
hostname = cat-match.easygame2021.com
*/

path =  "/sheep/v1/game/map_info_new?map_id=80001"

$done({path});
