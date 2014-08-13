VIDEO_ENDPOINT = "http://www.giantbomb.com/api/video/%d/?api_key=%s&format=json"

def Start():
    HTTP.CacheTime = CACHE_1DAY

def getJSON(video_id):
    video_id = int(video_id)
    url = VIDEO_ENDPOINT % (video_id, Prefs['api_key'])

    return JSON.ObjectFromURL(url)['results']

class GiantBombAgent(Agent.Movies):

    name = 'GiantBomb'
    languages = [Locale.Language.English]
    primary_provider = True
    accepts_from = ['com.plexapp.agents.localmedia']
    contributes_to = ['com.plexapp.agents.localmedia']

    def search(self, results, media, lang, manual):
        video_id = int(media.name.split()[0])
        obj = getJSON(video_id)
        year = obj['publish_date'].split("-")[0]

        results.Append(MetadataSearchResult(
            id=str(video_id),
            name=obj['name'],
            year=year,
            score=100,
            lang=lang
        ))

    def update(self, metadata, media, lang):
        obj = getJSON(metadata.id)

        metadata.duration = obj['length_seconds'] * 1000
        metadata.title = obj['name']
        metadata.year = int(obj['publish_date'].split("-")[0])
        metadata.summary = obj['deck']
        metadata.collections = [obj['video_type']]

        image = obj['image']['super_url']
        metadata.posters[image] = Proxy.Media(HTTP.Request(image).content)
