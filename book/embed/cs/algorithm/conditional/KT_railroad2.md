{% tabs %}
{% tab title='KT_railroad2.md' %}

* a와 b가 주어진다.
* b가 짝수이면 possible 홀수이면 impossible을 출력한다.

{% endtab %}
{% tab title='KT_railroad2.py' %}

```py
a, b = map(int, input().split())
if b % 2 == 0:
  print("possible")
else:
  print("impossible")
```

{% endtab %}
{% endtabs %}