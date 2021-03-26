{% tabs %}
{% tab title='KT_pet.md' %}

* 5명의 사람이 요리 대결을 한다.
* 최고점을 받은 사람의 줄 수와 총점을 출력하라

{% endtab %}
{% tab title='KT_pet.py' %}

```py
from collections import Counter
cnter = Counter()
for i in range(5):
  cnter[i + 1] = sum(map(int, input().split()))
print(*cnter.most_common(1)[0])
```

{% endtab %}
{% endtabs %}