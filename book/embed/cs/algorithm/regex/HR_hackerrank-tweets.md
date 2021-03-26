{% tabs %}
{% tab title='HR_hackerrank-tweets.md' %}

* Print the total number of tweets that has hackerrank (case insensitive) in it

{% endtab %}
{% tab title='HR_hackerrank-tweets.py' %}

```py
import re
input_ = ' '.join([input() for _ in range(int(input()))])
print(len(re.findall(r'hackerrank', input_, re.IGNORECASE)))
# print(sum('HACKERRANK' in input().upper() for i in range(int(input()))))
```

{% endtab %}
{% endtabs %}