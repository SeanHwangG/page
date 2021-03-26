{% tabs %}
{% tab title='KT_quickestimate.md' %}

* 첫번째 줄에는 N이 그 다음 N 줄에는 x가 주어진다. 이때 각 줄마다 x의 자리수를 출력하라.

{% endtab %}
{% tab title='KT_quickestimate.py' %}

```py
n_line = int(input())
for _ in range(n_line):
    x = input()
    print(len(x))
```

{% endtab %}
{% endtabs %}