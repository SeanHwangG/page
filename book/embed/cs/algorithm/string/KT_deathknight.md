{% tabs %}
{% tab title='KT_deathknight.md' %}

* 첫줄에 N이 주어진다.
* 다음 각각 N줄에 문자가 주어지는데, 이 때 CD를 포함하지 않는 줄의 수를 구하여라.

{% endtab %}
{% tab title='KT_deathknight.py' %}

```py
n = int(input())
ret = 0
for _ in range(n):
    if input().find('CD') == -1:
        ret += 1
print(ret)
```

{% endtab %}
{% endtabs %}