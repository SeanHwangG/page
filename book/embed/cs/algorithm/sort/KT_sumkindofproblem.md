{% tabs %}
{% tab title='KT_sumkindofproblem.md' %}

* 첫 줄에 n이 주어진다.
* 그 다음 n 줄에 k, m이 주어지는데, 이 때 k 와 첫 m개의 자연수, 홀수, 짝수 의 합을 구하라.

{% endtab %}
{% tab title='KT_sumkindofproblem.py' %}

```py
n = int(input())
for i in range(n):
  k, n = map(int, input().split())
  print(k, n * (n + 1) // 2, n * (n + 1) - n, n * (n + 1))
```

{% endtab %}
{% endtabs %}