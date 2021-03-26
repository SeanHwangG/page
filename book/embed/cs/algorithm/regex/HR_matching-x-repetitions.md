{% tabs %}
{% tab title='HR_matching-x-repetitions.md' %}

* must be of length equal to 45.
* The first characters should consist of letters(both lowercase and uppercase), or of even digits.
* The last characters should consist of odd digits or whitespace characters.

{% endtab %}
{% tab title='HR_matching-x-repetitions.py' %}

```py
import re
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.
print(str(bool(re.search(pattern, input()))).lower())
```

{% endtab %}
{% endtabs %}