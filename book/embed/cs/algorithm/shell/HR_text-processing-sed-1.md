{% tabs %}
{% tab title='HR_text-processing-sed-1.md' %}

* For each line in a given input file, transform the first occurrence of the word 'the' with 'this'
* The search and transformation should be strictly case sensitive.

{% endtab %}
{% tab title='HR_text-processing-sed-1.sh' %}

```sh
# \< and > in regex world (sed syntax) represents words boundaries
sed -e 's/\<the\>/this/'
```

{% endtab %}
{% endtabs %}