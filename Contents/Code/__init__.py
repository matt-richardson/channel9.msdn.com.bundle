ICON = 'icon-default.jpg'
ART = 'art-default.jpg'

####################################################################################################
def Start():

	ObjectContainer.title1 = 'channel9.msdn.com'
	DirectoryObject.thumb = R(ICON)
	DirectoryObject.art = R(ART)
	HTTP.CacheTime = CACHE_1HOUR
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

####################################################################################################
@handler('/video/channel9.msdn.com', 'channel9.msdn.com')
def MainMenu():

	oc = ObjectContainer()

	oc.add(DirectoryObject(
        key = Callback(Shows),
        title = "Shows"))

	oc.add(DirectoryObject(
        key = Callback(Series),
        title = "Series"))

	return oc

@route('/video/channel9.msdn.com/shows')
def Shows():
	oc = ObjectContainer()

	html = HTML.ElementFromURL("http://channel9.msdn.com/Browse/Shows")

	for show in html.xpath(r'//ul[@class="entries"]/li'):
		title = show.xpath("./div[@class='entry-meta']/a/text()")[0]
		summary = show.xpath("./div[@class='entry-meta']/div[@class='description']/text()")[0]
		id = show.xpath("./div[@class='entry-meta']/a")[0].get('href')
		url = id
		if url.startswith("http") == False:
			url = "http://channel9.msdn.com" + url

		image = show.xpath("./div[@class='entry-image']/img")[0].get('src')
		if image.startswith("http") == False:
			image = "http://channel9.msdn.com" + image

		oc.add(DirectoryObject(
			key = Callback(Show, id=id),
			title = title,
			summary = summary,
			thumb = image
		))

	return oc

@route('/video/channel9.msdn.com/show')
def Show(id):
	oc = ObjectContainer()

	html = HTML.ElementFromURL("http://channel9.msdn.com" + id)

	for show in html.xpath(r'//ul[@class="entries"]/li'):
		title = show.xpath("./div[@class='entry-meta']/a/text()")[0]
		summary = show.xpath("./div[@class='entry-meta']/div[@class='description']/text()")[0]
		url = show.xpath("./div[@class='entry-meta']/a")[0].get('href')
		if url.startswith("http") == False:
			url = "http://channel9.msdn.com" + url

		image = show.xpath("./div[@class='entry-image']/a/img")[0].get('src')
		if image.startswith("http") == False:
			image = "http://channel9.msdn.com" + image

		#duration = Datetime.MillisecondsFromString(show.xpath("./div[@class='entry-image']/div[@class='entry-caption']/text()")[0])
		#duration = 0
	
		oc.add(VideoClipObject(
			url = url,
			title = title,
			summary = summary,
			thumb = image
			#duration = duration
			#originally_available_at = originally_available_at
		))

	return oc

@route('/video/channel9.msdn.com/series')
def Series():
	oc = ObjectContainer()

	html = HTML.ElementFromURL("http://channel9.msdn.com/Browse/Series")

	for show in html.xpath(r'//ul[@class="entries"]/li'):
		title = show.xpath("./div[@class='entry-meta']/a/text()")[0]
		summary = show.xpath("./div[@class='entry-meta']/div[@class='description']/text()")[0]
		id = show.xpath("./div[@class='entry-meta']/a")[0].get('href')
		url = id
		if url.startswith("http") == False:
			url = "http://channel9.msdn.com" + url

		image = show.xpath("./div[@class='entry-image']/img")[0].get('src')
		if image.startswith("http") == False:
			image = "http://channel9.msdn.com" + image

		oc.add(DirectoryObject(
			key = Callback(Show, id=id),
			title = title,
			summary = summary,
			thumb = image
		))

	return oc
