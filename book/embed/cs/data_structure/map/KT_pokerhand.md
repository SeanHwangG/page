{% tabs %}
{% tab title='KT_pokerhand.md' %}

* 5개의 포커카드가 주어진다.
* 첫번째 문자가 카드의 랭크인데 이때 가장 많이 등장하는 랭크의 개수를 출력하라

{% endtab %}
{% tab title='KT_pokerhand.py' %}

```py
from collections import Counter
cnter = Counter()
for card in input().split():
  cnter[card[0]]+=1
print(cnter.most_common(1)[0][1])
```

{% endtab %}
{% endtabs %}