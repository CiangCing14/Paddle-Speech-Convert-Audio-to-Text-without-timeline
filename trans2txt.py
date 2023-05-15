import paddle,os,json
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.text.infer import TextExecutor

import warnings
warnings.filterwarnings('ignore')

asr_executor = ASRExecutor()
text_executor = TextExecutor()

def audio2txt(path):

    # 返回path下所有文件构成的一个list列表
    filelist = os.listdir(path)
    # 保证读取按照文件的顺序
    filelist.sort(key=lambda x: int(x[:3]))
    # 遍历输出每一个文件的名字和类型
    words = []
    for file in filelist:
        print(path+'/'+file)
        text = asr_executor(
            audio_file=path+'/'+file,
            device=paddle.get_device())
        if text:
            result = text_executor(
                text=text,
                task='punc',
                model='ernie_linear_p3_wudao',
                device=paddle.get_device())
        else:
            result = text
        words.append(result)
    return words
p=os.listdir('change/audio')
p.sort(reverse=True)
for a in p:
    if not os.path.exists(pa:='texts/%s.txt'%a):
        tt=audio2txt('change/audio/%s'%a)
        f=open(pa,'w+');f.write(json.dumps(tt));f.close()
