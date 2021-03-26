{% tabs %}
{% tab title='KT_yinyangstones.md' %}

* W와 B의 개수가 같으면 1 아니면 0을 출력하라.

{% endtab %}
{% tab title='KT_yinyangstones.py' %}

```py
from collections import Counter
cnt = Counter(input())
print(1 if cnt['W'] == cnt['B'] else 0)
```

{% endtab %}
{% endtabs %}