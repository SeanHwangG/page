{% tabs %}
{% tab title='KT_Last.md' %}

* 팩토리얼을 구한 뒤 마지막 자릿 수를 구하여라.

{% endtab %}
{% tab title='KT_Last.py' %}

```py
n_test = int(input())
for _ in range(n_test):
  n = int(input())
  ret = 1
  for i in range(1, n + 1):
    ret *= i
  print(ret % 10)
```

{% endtab %}
{% endtabs %}