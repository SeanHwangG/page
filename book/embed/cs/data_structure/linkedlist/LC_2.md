{% tabs %}
{% tab title='LC_2.md' %}

* Add two linked list number

{% endtab %}
{% tab title='LC_2.py' %}

```py
def addTwoNumbers(self, l1, l2):
  carry = 0
  res = n = ListNode(0)
  while l1 or l2 or carry:
    if l1:
      carry += l1.val
      l1 = l1.next
    if l2:
      carry += l2.val
      l2 = l2.next
    carry, val = divmod(carry, 10)
    n.next = n = ListNode(val)
  return res.next
```

{% endtab %}
{% endtabs %}