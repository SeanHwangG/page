{% tabs %}
{% tab title='HR_text-processing-awk-1.md' %}

* For each student, if one or more of the three scores is missing
  * display Not all scores are available for [Identifier]

{% endtab %}
{% tab title='HR_text-processing-awk-1.sh' %}

```sh
awk '{if (NF < 4){print "Not all scores are available for "$1}}'
```

{% endtab %}
{% endtabs %}