{% tabs %}
{% tab title='HR_matching-range-of-characters.md' %}

* The string's length is .
* The first character must be a lowercase English alphabetic character.
* The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
* The third character must not be a lowercase English alphabetic character.
* The fourth character must not be an uppercase English alphabetic character.
* The fifth character must be an uppercase English alphabetic character.

{% endtab %}
{% tab title='HR_matching-range-of-characters.py' %}

```py
import re
pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}