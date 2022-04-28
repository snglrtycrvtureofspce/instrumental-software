import urllib.parse, webbrowser

domain = 'https://kbp.by/'
url = 'rasp/timetable/view_beta_kbp/?cat=group&id=62'
full = urllib.parse.urljoin(domain, url, allow_fragments=True)
print(full)
webbrowser.open(full)