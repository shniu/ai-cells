
## Flash Instant Message

分布式的即时通信基础服务。

IM 的核心能力放在 core 中，client 负责客户端的逻辑，server 负责服务端的逻辑

基础的抽象模型：客户端向服务端发起连接，建立一个 channel，成功之后 channel 可以通信
需要有异步编程的支持


### 协议设计

1. 通信协议：消息头+消息 payload

魔数 | 版本号 | 命令类型 | 消息序列号 | 数据 payload 长度 | 数据 payload

魔数：2 bytes, 0x1014
版本号：2 bytes 
命令类型：1 bytes, e.g. login, chat, ping
消息序列号: 4 bytes
payload 长度: 4 bytes
payload: 变长字节数组

2. 传输方式：二进制传输，把数据表编码成二进制数据，以流的方式发送出去，接收端收取到数据后解码成想要的对象
