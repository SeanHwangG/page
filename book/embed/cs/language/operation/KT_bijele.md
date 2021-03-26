{% tabs %}
{% tab title='KT_bijele.md' %}

* 체스에는 킹, 퀸은 1개, 룩, 비숍, 나이트는 2개, 폰은 8개가 있다.
* 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어질 때, 더 필요한 개수를 한줄로 각각 출력하라. (빼야 한다면 -)

{% endtab %}
{% tab title='KT_bijele.py' %}

```py
a, b, c, d, e, f = map(int, input().split())
print(1 - a, 1 - b, 2 - c, 2 - d, 2 - e, 8 - f)
```

{% endtab %}
{% endtabs %}