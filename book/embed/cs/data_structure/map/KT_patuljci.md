{% tabs %}
{% tab title='KT_patuljci.md' %}

* 9개의 숫자가 주어진다. 그 중 7개의 숫자의 합은 100이다. 그 7개의 숫자를 출력하라.

{% endtab %}
{% tab title='KT_patuljci.py' %}

```py
from itertools import combinations
li = []
for _ in range(9):
  li.append(int(input()))
for p in combinations(li, 7):
  if sum(p) == 100:
    print(*p, sep='\n')
    break
```

{% endtab %}
{% endtabs %}