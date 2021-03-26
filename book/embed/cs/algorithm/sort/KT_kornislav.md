{% tabs %}
{% tab title='KT_kornislav.md' %}

* 숫자 4개가 주어진다. 이때 만들 수 있는 가장 큰 직사각형을 구하여라. (긴 변은 직사각형을 나가도 됨)

{% endtab %}
{% tab title='KT_kornislav.py' %}

```py
a, b, c, d = sorted(map(int, input().split()))
print(a * c)
```

{% endtab %}
{% endtabs %}