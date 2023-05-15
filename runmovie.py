import moviepy.editor as mp
import os
# 采样率16k 保证和paddlespeech一致
def extract_audio(videos_file_path):   
     my_clip = mp.AudioFileClip(videos_file_path,fps=16000)
     if (videos_file_path.split(".")[-1] == 'MP3' or videos_file_path.split(".")[-1] == 'mp3'):
          p = videos_file_path.split('.mp3')[0]
          my_clip.write_audiofile(op:='audios/%s'%p.split('/')[-1] + '_video.mp3')
          print(op)
for a in os.walk('[原音频所在目录]'):
    a[2].sort(reverse=True)
    for b in a[2]:
        p = ('%s/%s'%(a[0],b)).split('.mp3')[0]
        op='audios/%s'%p.split('/')[-1] + '_video.mp3'
        if not os.path.exists(op):
            extract_audio('%s/%s'%(a[0],b))
