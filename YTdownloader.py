#Developed and coded by Mohammad Reza Maleki 
#Used library in this code is Pytube version 3 
#follow me on all Social media's : @momalekiii




from pytube import YouTube


myVideo = YouTube("Paste Your video url here ! ")

print("\n")
print("*********** Title **********")

# get videos title
print("Video's Title : "+myVideo.title)

print("\n")
print("*********** Thumbnail image **********")
# get videos thumbnail
print(myVideo.thumbnail_url)




print("\n")
print("***********  Download Video **********")
print("***** Wait until download finish *****")

# download video
myVideo.streams.first().download()

print("Video is downloaded successfuly")