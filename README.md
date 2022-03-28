# suda-daily-health-report
苏州大学每日健康情况自动化打卡脚本

## 环境配置
1. 此版本脚本基于`chrome`浏览器，因此需要下载`chromedriver.exe`。下载链接如下：

    - 官方：http://chromedriver.storage.googleapis.com/index.html
    - 镜像：http://npm.taobao.org/mirrors/chromedriver/
    
检查`chrome`浏览器版本后，下载对应版本的`chromedriver`压缩包，并将压缩包解压至`chrome`的安装目录。Windows系统默认为：`C:\Program Files (x86)\Google\Chrome\Application`。完成后，将该路径添加至系统环境变量`Path`中。

2. 在`info.json`中填写好必要的个人信息，如：
    
    - `account`：学号，学籍号
    - `passwd`：密码，学生系统密码
    - `current_location`：目前所在地，可选字段为："在校"，"在苏州"，"江苏省其他地区"，"在境外、在中高风险地区"，"在中高风险地区所在城市"，"在其他地区"。
    - `town_and_community`：具体地理，一般填写到社区/小区即可，确保内容准确即可，没有具体的格式要求

## 运行
1. 使用pip命令安装对应于运行版本的`selenium`包。开发时使用版本为`python3.9.6`。
2. 安装完成后，运行`main.py`，享受自动化带来的乐趣吧（逃）

## 后记
做这个项目的灵感来源于某天和丁某祥交流时的谈话。当时突然想到，也许可以用自动化的方法完成打卡，于是在某个周日的下午开始实践。第一次尝试自动化确实遇到了不少问题，但是经过强大的检索能力（指Ctrl+C && Ctrl+V），勉强完成了这个简单的项目。后期会进行更新，大家把想法写到Issues或者发email给我即可。
