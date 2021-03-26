{% tabs %}
{% tab title='KT_differentdistances.md' %}

* x1, x2, y1, y2이 주어진다.
* 이때 를 출력하라.
* 마지막 줄에 0이 나온다.

{% endtab %}
{% tab title='KT_differentdistances.py' %}

```py
while True:
  raw = input()
  if raw == '0':
    break
  a, b, c, d, e = map(float, raw.split())
  print((abs(a - c) ** e + abs(b - d) ** e) ** (1/e))
```

{% endtab %}
{% endtabs %}