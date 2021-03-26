{% tabs %}
{% tab title='HR_text-processing-grep-2.md' %}

* Use grep to display all those lines that contain the word the in them.
* The search should NOT be sensitive to case.

{% endtab %}
{% tab title='HR_text-processing-grep-2.sh' %}

```sh
# -i, --ignore-case
# Perform case insensitive matching.  By default, grep is case sensitive.
# -w, --word-regexp
# The expression is searched for as a word
grep -iw "the"
```

{% endtab %}
{% endtabs %}