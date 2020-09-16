from youtube_transcript_api import YouTubeTranscriptApi
import matplotlib.pyplot as plt
import numpy as np
import os, glob
import math


vf=[]
af=[]
w=[0]
t=[0]
tseg=[]
n=0
m=0
j=0
count=0
trim=list()
s=''
con=""
wps=int(input('input your desired words/second\n'))

script=YouTubeTranscriptApi.get_transcript('rqSeutfwb2Q')
# print(script)
for segs in script: #create two lists, one with the number of words in each segment, the other for the time for each segment (to plot the wps graph)
    words=0
    x=segs['text'].split()
    # print(x)
    for num in x:
        words+=1
    # print(words)
    y=float(segs['start'])
    # print(y)
    w.append(words)
    t.append(y)
print(w,len(w),t,len(t))


# del(t[1])
length=len(t)-1
while n < length:
    tseg.append(t[n+1]-t[n])
    n+=1
# print(t,tseg)
# del(tseg[0])
del(w[len(w)-1])
# print(t,tseg)
# print(len(w),len(tseg),len(t))
print(w,len(w),tseg,len(tseg))
while j < len(tseg):
    try:
        1/w[j]
        # vf.append(w[j]/(tseg[j]*wps))
        vf.append(wps*tseg[j]/w[j])
    except:
        vf.append(1)
    try:
        af.append(1/vf[j])
    except:
        af.append(1)
    j+=1
# del(t[0]) #delete me, only for santar
print (len(t),len(vf))
print("Time Stamps:",t,"\n","Speed Factor:",vf)

# plt.plot(tseg, w)
#
# plt.xlabel('time segment (sec)')
# plt.ylabel('# of words')
#
# plt.title('WPS Graph')
#
# plt.show()
# print ("no. of words:",w,"tseg:",tseg,"audio factor:",af,"video factor:",vf)
# print (len(w),len(tseg),len(t))

# print(t)
# while m < len(t)-1:
#     trim.append("[0:v]trim="+str(t[m])+":"+str(t[m+1])+",setpts="+str(vf[m])+"*(PTS-STARTPTS)[v"+str(m)+"];")
#     trim.append("[0:a]atrim="+str(t[m])+":"+str(t[m+1])+",asetpts="+str(af[m])+"*(PTS-STARTPTS)[a"+str(m)+"];")
#     m+=1

# del trim[0]
# del trim[0]
# print(trim[0],trim[1], trim[2])
# print(trim)

# for seg in trim:
#     try:
#         vpos=seg.find("[v")
#         math.sqrt(vpos)
#         spos=seg.find(";")
#         con=con+seg[vpos:spos]
#         count+=1
#         # print(con)
#     except:
#         apos=seg.find("[a")
#         math.sqrt(apos)
#         spos=seg.find(";")
#         con=con+seg[apos:spos]
#         # count+=1
#         # print(con)
#     s=s+seg
    # print(seg)
# print(con)
# s='"'+s
# count//=2
# print (s)


# def menu():
# 	lst = [str(n) + " " + file for n,file in enumerate(glob.glob("*.mp4"))]
# 	print(*lst, sep="\n")
# 	file = glob.glob("*.mp4")[int(input("File n."))]
# 	return file
# #print(file)
#
# # This is what it is executed below using the file input above
# file = menu()
# output = os.path.splitext(file)[0] + "_edited_" + ".mp4"
#
# cmd = f""" ffmpeg -i {file} -filter_complex  {s}{con}concat=n={str(count)}:v=1:a=1"  {output}
# pause
# """
# # print (cmd)
#
#
# # ffmpeg -i input.mkv -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" output.mkv
#
#
# os.system(cmd) # run the ffmpeg command to 4x velocity
# os.startfile(f"{output}") # runs the video
