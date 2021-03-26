
{% tabs %}
{% tab title='KT_peragrams.md' %}

```md
* Peragrams은 문자를 뒤섞었을 때 Palindrome이 되는 문자다.
* 첫 줄에 문자열이 주어 졌을 때 최소 문자 몇개를 제거해야 Peragrams이 되는지 출력하라.
```

{% endtab %}
{% tab title='KT_peragrams.py' %}

```py
from collections import Counter
cnt = Counter()
for ch in input():
  cnt[ch] += 1
ret = 0
for count in cnt:
  if cnt[count] % 2 == 1:
    ret += 1
print(max(0, ret - 1))
```

{% endtab %}
{% endtabs %}
