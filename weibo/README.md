# 微博爬虫
使用前需要有自己的代理池，在settings.py中填入
mongo数据库uri连接
MONGO_URI = ''
存储的数据库名称
MONGO_DATABASE = ''
代理连接获得的格式是ip:port
PROXY_URL = ''

### 配置完后使用命令scrapy crawl weibocn 开始爬虫

