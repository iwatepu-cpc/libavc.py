import requests
import bs4
import datetime
import re

def __time_from_row(row):
    t = row.select('.fixtime')[0].text
    t = t.replace(' ', 'T')
    t = re.sub(r'\+([0-9]{2})([0-9]{2})', r'+\1:\2', t)
    return datetime.datetime.fromisoformat(t)

def __status_from_row(row):
    s = row.select('.label')[0].text
    return s

def __lang_from_row(row):
    l = row.select('td')[3].text
    return l

def submissions(url, task, user):
    params = {
        'f.Task': task,
        'f.Language': None,
        'f.Status': None,
        'f.User': user
        }
    q = requests.get(url+'/submissions', params=params)
    if q.status_code == requests.codes.ok:
        html = bs4.BeautifulSoup(q.text, 'html.parser')
        rows = html.select('tbody > tr')
        results = list(map(lambda row: {
            'lang': __lang_from_row(row),
            'status': __status_from_row(row),
            'time': __time_from_row(row)
            }, rows))
        return results
    else:
        return []
