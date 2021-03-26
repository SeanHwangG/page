{% tabs %}
{% tab title='KT_pot.md' %}

* 첫 줄에 N이 다음 N줄에는 x가 주어진다
* 이 때 x의 마지막 자리는 지수이다. (Ex. 35 = 35)
* x의 합을 구하라.

{% endtab %}
{% tab title='KT_pot.py' %}

```py
n_line = int(input())
ret = 0
for _ in range(n_line):
    n = int(input())
    ret += (n // 10) ** (n % 10)
print(ret)
```

{% endtab %}
{% endtabs %}
