## Higher Order Function
- 함수를 전달 인자로 갖는 함수
- 함수를 전달하여 함수 내에서 전달받은 함수를 활용하여 연산하는 함수
- 전달인자로 전달하는 함수는 ()을 생략하고 넘긴다.

### Function Argument
- Position Arguments
  - 전달인자의 순서를 알때 사용
  - 내가 직접 장성한 함수나 순서가 명확한 함수에 사용
- Keyword Arguments
  - 전달인자의 순서를 알지 못할때 사용
  - 이미 만들어져 활용만 하는 method 사용할때 흔히 사용
  - 예)
    - onkey(key="space", fun=move_forwards)
- 각각의 상황에 맞는 방식을 사용하자