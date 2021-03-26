{% tabs %}
{% tab title='KT_cudoviste.md' %}

* N, M이 주어지고 N개의 라인의 주차장이 주어진다.
* 이 때 . 은 빈칸, '#' 은 건물, 'X' 는 다른 차량이다.
* 2x2의 차를 주차 할 때 0, 1, 2, 3, 4개의 차량을 치우고 댈 수 있는 가지 수를 각 라인에 출력하라.

{% endtab %}
{% tab title='KT_cudoviste.py' %}

```py
N, M = map(int, input().split())
G = []
for _ in range(N):
  G.append(input())
rets = [0, 0, 0, 0, 0]
for i in range(1, N):
  for j in range(1, M):
    spaces = [G[i - 1][j - 1], G[i - 1][j], G[i][j - 1], G[i][j]]
    if '#' in spaces:
      continue
    rets[spaces.count('X')] += 1
for ret in rets:
  print(ret)
```

{% endtab %}
{% endtabs %}