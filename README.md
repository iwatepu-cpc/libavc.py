# AtCoder Virtual Contest Library

## Usage

```python
import AtCoderVirtualContest as AVC

problems = list(map(AVC.Problem, [
  'https://atcoder.jp/contests/abc004/tasks/abc004_1',
  'https://atcoder.jp/contests/abc039/tasks/abc039_a',
  'https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_a'
  ]))

contest = AVC.Contest(problems)

contest.participate("<AtCoder ID>")
contest.participate("<AtCoder ID>")
contest.participate("<AtCoder ID>")

contest.start_now()

print(contest.update())

contest.end()
```
