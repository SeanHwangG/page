{% tabs %}
{% tab title='KT_R2.md' %}

* a, b, c 는 모두 정수이다.
* (a + c) / 2 = b 이다.
* a, b가 주어졌을때 c의 값을 구하여라.

{% endtab %}
{% tab title='KT_R2.py' %}

```py
a, b = map(int, input().split())
print((2 * b) - a)
```

{% endtab %}
{% endtabs %}