{% tabs %}
{% tab title='KT_filip.md' %}

* a, b는 0이 포함되지 않은 3자리 정수이다.
* a, b 의 숫자를 뒤집었을 때,  426 를 뒤집으면 624
* 뒤집혀진 a, b중 큰 수를 구하라.

{% endtab %}
{% tab title='KT_filip.py' %}

```py
a, b = map(int, input().split())
ra = (a % 10) * 100 + (a // 10 % 10) * 10 + (a // 100)
rb = (b % 10) * 100 + (b // 10 % 10) * 10 + (b // 100)
print(max(ra, rb))
```

{% endtab %}
{% endtabs %}