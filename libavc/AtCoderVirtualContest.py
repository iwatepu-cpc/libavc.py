import libavc.AtCoderSubmission as acs
import urllib
import requests
import datetime

__atcoder_url__ = 'https://atcoder.jp'

class Problem:
    def __init__(self, url):
        q = requests.get(url)
        if q.status_code != requests.codes.ok:
            raise ValueError(f"Error: can't open problem: {url}")
        parsed = urllib.parse.urlparse(url)
        names = parsed.path.split('/')
        self.contest = names[2]
        self.task = names[4]
        self.url = url
        self.contest_url = __atcoder_url__+f'/contests/{self.contest}'
        print(self.url)

class Contest:
    def __init__(self, problems):
        self.participants = []
        self.problems = problems
        self.start_time = None
        self.states = None

    def __exists_user(username):
        url = __atcoder_url__ + f'/users/{username}'
        q = requests.get(url)
        if q.status_code != requests.codes.ok:
            return False
        return True

    def participate(self, atcoder_id):
        if Contest.__exists_user(atcoder_id):
            self.participants.append(atcoder_id)
            return True
        else:
            return False

    def start_now(self):
        self.start_time = datetime.datetime.now().astimezone()
        self.states = {}
        for p in self.participants:
            self.states[p] = {problem.task:{
                'status': False,
                'time': None,
                'lang': None
                } for problem in self.problems}

    def update(self):
        diff = {}
        for p in self.participants:
            diff[p] = {}
            for problem in self.problems:
                task = problem.task
                if self.states[p][task]['status'] == False:
                    subl = acs.submissions(problem.contest_url, task, p)
                    subl = list(filter(lambda s:s['time'].astimezone() > self.start_time and s['status'] == 'AC', subl))
                    if len(subl) > 0:
                        s = subl[0]
                        state = {
                                'status': True,
                                'time': s['time'],
                                'lang': s['lang']
                                }
                        self.states[p][task] = state
                        diff[p][task] = state
        return diff

    def end(self):
        return self.states
