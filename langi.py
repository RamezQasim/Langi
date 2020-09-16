from youtube_transcript_api import YouTubeTranscriptApi
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
url=input('Insert the video link here\n')
idpos=url.find("v=")+2
id=url[idpos:]
print(id)
script=YouTubeTranscriptApi.get_transcript(id)
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

f = open('Langi.html','w')

content ="""<!DOCTYPE html>
<html>
<body>


<video id="myVideo" width="500" height="400" controls>
    <source src="clip.mp4" type="video/mp4">
error
</video>


<script>

var vid = document.getElementById("myVideo");

function getPlaySpeed() {
  alert(vid.playbackRate);
}

function getTime() {
  alert(vid.currentTime);
}

var Stamps =%s ;
var Speed  = %s;
var i = 0;

var test = 0;
var interval;

function check_test() {
console.log( vid.currentTime );
    if(vid.currentTime >= Stamps[i] && vid.currentTime < Stamps[i+1]){
		vid.playbackRate = Speed[i];
        console.log( "Time now: " + Stamps[i] + "Speed: " + Speed[i]);
		i = i + 1;
    }
}

interval = window.setInterval( check_test, 1 );

</script>

</body>
</html>
"""%(t,vf)

f.write(content)
f.close()
