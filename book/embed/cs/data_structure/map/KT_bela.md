{% tabs %}
{% tab title='KT_bela.md' %}

* 첫 줄의 N과 B이 주어진다.
* 그 다음 N줄에 Value, Suit 이 주어지는데,
* Suit 이 B와 같을 시 Dominant, 다를 시 Not dominant 점수를 얻는다. 총 합을 출력하라.

{% endtab %}
{% tab title='KT_bela.py' %}

```py
n_line, suit = input().split()
n_line = int(n_line)
dic = {'A': (11, 11), 'K': (4, 4), 'Q': (3, 3), 'J':(20, 2), 'T': (10, 10), '9': (14, 0), '8' : (0, 0), '7': (0, 0)}
ret = 0
for _ in range(n_line * 4):
  card = input()
  if card[1] == suit:
    ret += dic[card[0]][0]
  else:
    ret += dic[card[0]][1]
print(ret)
```

{% endtab %}
{% endtabs %}