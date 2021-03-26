{% tabs %}
{% tab title='HR_text-processing-paste-1.md' %}

* join all rows with ;

{% endtab %}
{% tab title='HR_text-processing-paste-1.sh' %}

```sh
# -d
# Use one or more of the provided characters to replace the newline characters instead of the default tab.
# -s
# Concatenate all of the lines of each separate input file in command line order.
paste -sd ';'
```

{% endtab %}
{% endtabs %}