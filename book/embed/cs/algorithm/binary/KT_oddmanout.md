{% tabs %}
{% tab title='KT_oddmanout.md' %}

* n_test개의 줄에 N과 N개의 정수가 주어진다.
* 이때 짝이 없는 정수를 출력하라.

{% endtab %}
{% tab title='KT_oddmanout.py' %}

```py
n_test = int(input())
for test in range(1, n_test + 1):
    N = int(input())
    ret = 0
    for x in map(int, input().split()):
        ret ^= x
    print(f"Case #{test}: {ret}")
```

{% endtab %}
{% endtabs %}