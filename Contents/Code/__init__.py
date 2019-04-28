VIDEO_ENDPOINT = "https://www.giantbomb.com/api/video/%s/?api_key=%s&format=json"

def Start():
    HTTP.CacheTime = CACHE_1DAY

def getJSON(video_guid):
    video_guid = str(video_guid)
    url = VIDEO_ENDPOINT % (video_guid, Prefs['api_key'])

    return JSON.ObjectFromURL(url)['results']

class GiantBombAgent(Agent.Movies):

    name = 'Giant Bomb'
    languages = [Locale.Language.English]
    primary_provider = True
    accepts_from = ['com.plexapp.agents.localmedia']
    contributes_to = ['com.plexapp.agents.localmedia']

    def search(self, results, media, lang, manual):
        parts = media.name.split()
        video_guid = str(parts[0]) + '-' + str(parts[1])
        obj = getJSON(video_guid)
        year = obj['publish_date'].split("-")[0]

        results.Append(MetadataSearchResult(
            id=str(video_guid.split('-')[1]),
            name=obj['name'],
            year=year,
            score=100,
            lang=lang
        ))

    def update(self, metadata, media, lang):
        obj = getJSON(metadata.id)

        metadata.collections = obj['video_type'].split(', ')
        metadata.duration    = obj['length_seconds'] * 1000
        metadata.studio      = 'Giant Bomb'
        metadata.summary     = obj['deck']
        metadata.title       = obj['name']
        metadata.year        = int(obj['publish_date'].split("-")[0])

        members = cast.cast_from_deck(obj['deck'])
        for member in members:
            role = metadata.roles.new()
            role.role = 'Self'
            role.actor = member

        image = obj['image']['super_url']
        metadata.posters[image] = Proxy.Media(HTTP.Request(image).content)
