{% tabs %}
{% tab title='CC_COOK127B.md' %}

![](images/20210322_013658.png)

{% endtab %}
{% tab title='CC_COOK127B.py' %}

```py
from functools import reduce

def solution(a, b, c):
  xors = []
  count = 0
  for i in range(2, a + b + 1):
    if a >= i - 1 and b >= i - 1:
      count += 1
    elif a < i - 1 and b < i - 1:
      count -= 1
    if count % 2 == 1:
      xors.append(c + i)
  return reduce(lambda x, y: x ^ y, xors)


for _ in range(int(input())):
  a, b, c = map(int, input().split())
  print(solution(a, b, c))
```

{% endtab %}
{% endtabs %}