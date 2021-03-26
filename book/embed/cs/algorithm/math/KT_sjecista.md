{% tabs %}
{% tab title='KT_sjecista.md' %}

* n개의 꼭지점을 가진 다각형이 있다.
* 이 때 모든 선분의 교차점의 개수를 출력하라. 단 3개 이상의 선분은 한 점에서 만나지 않는다.

{% endtab %}
{% tab title='KT_sjecista.py' %}

```py
import math
def nCr(n,r):
    if r > n:
        return 0
    f = math.factorial
    return f(n) // f(r) // f(n-r)
n = int(input())
print(nCr(n, 4))
```

{% endtab %}
{% endtabs %}