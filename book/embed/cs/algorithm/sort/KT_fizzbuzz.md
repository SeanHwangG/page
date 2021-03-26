{% tabs %}
{% tab title='KT_fizzbuzz.md' %}

* X, Y, N이 첫줄에 주어진다.
* 1부터 N까지의 자연수 중 X 의 배수는 Fizz, Y의 배수는 Buzz, X, Y의 동시의 배수는 FizzBuzz,
* 그 외에는 숫자를 출력하라.

{% endtab %}
{% tab title='KT_fizzbuzz.py' %}

```py
x, y, n_line = map(int, input().split())
for i in range(1, n_line + 1):
  if i % x == 0 and i % y == 0:
    print("FizzBuzz")
  elif i % x == 0:
    print("Fizz")
  elif i % y == 0:
    print("Buzz")
  else:
    print(i)
```

{% endtab %}
{% endtabs %}