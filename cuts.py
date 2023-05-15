import auditok
import os,time


def qiefen(path, ty='audio', mmin_dur=1, mmax_dur=49000, mmax_silence=1, menergy_threshold=65):

    file = path

    audio_regions = auditok.split(
        file,
        min_dur=mmin_dur,  # minimum duration of a valid audio event in seconds
        max_dur=mmax_dur,  # maximum duration of an event
        # maximum duration of tolerated continuous silence within an event
        max_silence=mmax_silence,
        energy_threshold=menergy_threshold  # threshold of detection
    )

    for i, r in enumerate(audio_regions):
        # Regions returned by `split` have 'start' and 'end' metadata fields
        print(
            "Region {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r))

        epath = ''
        file_pre = str(epath.join(file.split('.')[0].split('/')[-1]))

        mk = './change'
        if (os.path.exists(mk) == False):
            os.makedirs(mk)
        if(os.path.exists(mk+'/'+ty) == False):
            os.makedirs(mk+'/'+ty)
        if(os.path.exists(mk+'/'+ty+'/'+file_pre) == False):
            os.makedirs(mk+'/'+ty+'/'+file_pre)

        num = i
        # 为了取前三位数字排序
        s = '000000'+str(num)

        file_save = mk+'/'+ty+'/'+file_pre + '/' + \
            s[-3:]+'-'+'{meta.start:.3f}-{meta.end:.3f}'+'.wav'

        filename = r.save(file_save)
        print("region saved as: {}".format(filename))

    return mk+'/'+ty+'/'+file_pre
n=0
while True:
    for a in os.walk('audios'):
        a[2].sort(reverse=True)
        for b in a[2]:
            if not os.path.exists('change/audio/%s'%b.split('.')[0]):
                qiefen('%s/%s'%(a[0],b))
    n+=1
    print('循环%d结束……'%n)
    time.sleep(10)
