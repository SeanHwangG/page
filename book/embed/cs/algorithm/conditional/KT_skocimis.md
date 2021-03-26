{% tabs %}
{% tab title='KT_skocimis.md' %}

* 캥거루 a, b, c가 한 선 위에 순서대로 있다.
* 캥거루 a, c가 b 양옆으로 점프를 하는데, 이 때 더 긴 점프의 길이를 출력하라.

{% endtab %}
{% tab title='KT_skocimis.py' %}

```py
a, b, c = map(int, input().split())
print(max(c - b - 1, b - a - 1))
```

{% endtab %}
{% endtabs %}