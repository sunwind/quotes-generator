# Introduction 
名人名言生成器，目前还很简单，用来玩 Python : ) 

A quote generator for learning Python

- 支持以 CGI 方式在 Apache 等服务器软件上运行
- 支持以 JSON 或者纯文本方式输出，通过 URL 的 v 参数设置. v=txt or v=json
- URL 的 t 参数可以指定某个模板号，从 0 开始。
- 可以自动生成模板和列表的 py 文件（也算一种简单的元编程吧）

## TODO
加入更多的模板
切换语言功能
完善代码结构，提高效率（不过目前来说瓶颈还在网络延迟上）
完善错误显示，邮件告知
分隔格言和人名
GUI 支持
...

英文版的准备参考 https://api.github.com/zen 来实现。
