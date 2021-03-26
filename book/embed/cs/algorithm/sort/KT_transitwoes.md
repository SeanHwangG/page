{% tabs %}
{% tab title='KT_transitwoes.md' %}

* 첫줄에 출발시간s, 수업시작시간t, n이 주어진다.
* 두번째 줄에는 n+1 개의 수가 주어지며 한 정거장에서 다음정거장으로 가는데 걸리는 시간을 의미.
* 세번째 줄에는 n 개의 수가 주어지며 버스타고가면서 걸리는시간을 의미.
* 네번째 줄에도 n 개의 수가 주어진다.버스가 정거장에 도착하는데 걸리는시간
* 제시간에 수업에 도착할 수 있으면 ‘yes’ 없으면 ‘no’를 출력하라

{% endtab %}
{% tab title='KT_transitwoes.py' %}

```py
cur, t, n = map(int, input().split())
D = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
for d, b, c in zip(D, B, C):
  cur += d
  cur += (cur % c)
  cur += b
if cur + D[-1] < t:
  print("yes")
else:
  print("no")
```

{% endtab %}
{% endtabs %}