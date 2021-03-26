{% tabs %}
{% tab title='KT_qaly.md' %}

* 첫 줄에는 n이, 그 다음 n 번째 줄에는 a, b가 주어진다. n개의 a * b 의 합을 구하라.

{% endtab %}
{% tab title='KT_qaly.py' %}

```py
n_line = int(input())
ret = 0
for _ in range(n_line):
  a, b = map(float, input().split())
  ret += a * b
print(ret)
```

{% endtab %}
{% endtabs %}