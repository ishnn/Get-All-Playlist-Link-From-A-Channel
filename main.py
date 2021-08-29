import googleapiclient.discovery

channel_id = "channel id here"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "YOUR_API_KEY")


request = youtube.playlists().list(
    part = "snippet",
    channelId = channel_id,
    maxResults = 50
)
response = request.execute()

playlists = []
while request is not None:
    response = request.execute()
    playlists += response["items"]
    request = youtube.playlists().list_next(request, response)

for i in range(len(playlists)):
    link = list(playlists[i].values())[2]
    link = "https://www.youtube.com/playlist?list="+link
    print(link)
