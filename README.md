# Paddle-Speech-Convert-Audio-to-Text-without-timeline

Paddle-Speech-Convert-Audio-to-Text-without-timeline.

这是一个使用Paddle Speech将批量音频转写为无时间轴的文本的范例代码。

# 使用教程

1.安装好Python 3.10及以下的非最新Python版本。

2.运行命令`python -m pip install -r requirements.txt`。

3.修改文件“runmovie.py”中的“[原音频所在目录]”为你存放mp3音频的目录。

4.创建文件夹“audios”并`python runmovie.py`

5.创建文件夹“change”并`python cuts.py`（经过调节参数，和上一个py文件可以同时运行。）

6.创建文件夹“texts”并`python trans2txt.py`（可与下一步同时运行，不能与上一步同时运行。）

7.创建文件夹“stexts”并`python stext.py`

以上，便可以将批量音频转换为没有时间轴的文本。

# 鸣谢

https://aistudio.baidu.com/aistudio/projectdetail/3752669
