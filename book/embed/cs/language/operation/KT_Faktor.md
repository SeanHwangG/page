{% tabs %}
{% tab title='KT_Faktor.md' %}

* a, b, c 는 모두 정수이다.
* ceil(c / a) = b 이다. ceil(1) = 1, ceil(1.1) = 2, ceil(0.9) = 1
* a, b가 주어졌을때 c의 최솟값을 구하여라.

{% endtab %}
{% tab title='KT_Faktor.py' %}

```py
a, b = map(int, input().split())
print((b - 1) * a + 1)
```

{% endtab %}
{% endtabs %}