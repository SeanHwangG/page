{% tabs %}
{% tab title='LC_1.md' %}

* Find two index that sums up to target

{% endtab %}
{% tab title='LC_1.py' %}

```py
def twoSum(self, nums, target):
  d = {}
  for i, num in enumerate(nums):
    if target - num in d:
      return d[target - num], i
    d[num] = i
```

{% endtab %}
{% endtabs %}