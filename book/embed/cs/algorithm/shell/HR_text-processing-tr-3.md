{% tabs %}
{% tab title='HR_text-processing-tr-3.md' %}

* Replace all sequences of multiple spaces with just one space.

{% endtab %}
{% tab title='HR_text-processing-tr-3.sh' %}

```sh
# -s, --squeeze-repeats
# replace each input sequence of a repeated character that is listed in SET1 with a single occurrence of that character

tr -s " "
```

{% endtab %}
{% endtabs %}