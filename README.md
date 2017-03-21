# danmuspider

本项目初期只是好奇想统计大家发弹幕的内容以及送礼的关系,爬取数据用作分析.



### 环境配置(python2.7)
	pip install douyu
	pip install DBUtils
	pip install mysql-python


### 使用方法:

	修改Config.py中数据库(数据库创建时请设置utf-8编码)
	运行 "python weijia.py 房间号 备注"开始爬虫(会自动建表)
		其中房间号仅为数字,备注可有可无,仅供自己方便识别
		输入命令(linux环境)如: nohup python weijia.py 1275878 暴走漫画直播间 &
		    即可在后台抓取弹幕礼物信息

### 数据演示图片请看 img 目录:

![弹幕](https://coding.net/u/yanweijia/p/danmuspider/git/raw/master/img/chatpic.png)
![礼物](https://coding.net/u/yanweijia/p/danmuspider/git/raw/master/img/giftpic.png)
![抓取](https://coding.net/u/yanweijia/p/danmuspider/git/raw/master/img/shell.png)
![运行截图](https://coding.net/u/yanweijia/p/danmuspider/git/raw/master/img/run.png)