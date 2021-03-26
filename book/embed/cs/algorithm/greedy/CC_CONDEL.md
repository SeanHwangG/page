{% tabs %}
{% tab title='CC_CONDEL.md' %}

* Choose a subarray (a contiguous subsequence) with length K
* choose two indices L and R such that 1 ≤ L ≤ R ≤ N and R − L + 1 = K
* Choose one element of that subarray and change it to 0
* The cost of this operation is the sum of this subarray before AP is changed

{% endtab %}
{% tab title='CC_CONDEL.py' %}

```py
def solution(li, width):
  cur_total = sum(li[0: width])
  mn_total = cur_total
  for l in range(len(li) - width):
    cur_total = cur_total - li[l] + li[l + width]
    mn_total = min(mn_total, cur_total)
  return sum(li) + sum(range(mn_total))

for _ in range(int(input())):
  _, width = map(int, input().split())
  li = list(map(int, input().split()))
  print(solution(li, width))
```

{% endtab %}
{% endtabs %}