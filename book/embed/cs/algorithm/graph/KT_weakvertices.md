{% tabs %}
{% tab title='KT_weakvertices.md' %}

* weak vertices in graphs – those vertices that is not part of any triangle

{% endtab %}
{% tab title='KT_weakvertices.py' %}

```py
from collections import defaultdict
while True:
  N = int(input())
  if N == -1:
    break
  G = defaultdict(set)
  for i in range(N):
    for j, e in enumerate(list(map(int, input().split()))):
      if e == 1:
        G[i].add(j)
  for i in range(N):
    count = 0
    for j in G[i]:
      count += sum([1 for k in G[j] if k in G[i]])
    if count == 0:
      print(i, end = ' ')
  print()
```

{% endtab %}
{% endtabs %}