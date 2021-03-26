{% tabs %}
{% tab title='HR_text-processing-grep-3.md' %}

* Use grep to remove all those lines that contain the word 'that'
* The search should NOT be sensitive to case

{% endtab %}
{% tab title='HR_text-processing-grep-3.py' %}

```sh
# -v   : Invert the sense of matching
grep -viw 'that'
```

{% endtab %}
{% endtabs %}