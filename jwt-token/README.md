# README

> 目标是做出一个SSO层，传递JWT Token

## jwt

登录后得到一个JWT，访问Metabase的时候带上该JWT，登录页面解码并验证该JWT的有效性：

- 有效且为已有用户，放行
- 有效但Metabase中没有该用户，新建用户并放行
- 无效，拒绝。

不对啊，应该是Metabase全套都要用SSO层，也就是说Metabase内的逻辑也要跟着走，不过这样改动可能比较大。


