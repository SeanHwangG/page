{% tabs %}
{% tab title='HR_matching-zero-or-more-repetitions.md' %}

* begin with 1 or 2 digits.
* After that, 3 or more letters (both lowercase and uppercase).
* end with up to 3 symbol(s)

{% endtab %}
{% tab title='HR_matching-zero-or-more-repetitions.py' %}

```py
import re
pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}