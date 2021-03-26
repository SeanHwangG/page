{% tabs %}
{% tab title='KT_pieceofcake2.md' %}

* 정수 a, b, c 가 주어진다. 한 변의 길이가 a이고 높이가 4인  정사각형의 케익이 있다.
* 가로로 b, 세로로 c의 위치에서 케익을 자른다. 이때 가장 큰 조각의 부피를 구해라.

{% endtab %}
{% tab title='KT_pieceofcake2.py' %}

```py
a, b, c = map(int, input().split())
print(max(a - b, b) * max(a - c, c) * 4)
```

{% endtab %}
{% endtabs %}