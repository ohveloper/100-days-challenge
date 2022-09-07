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

### (의문) 객체와 인스턴스는 어떻게 다른가???

```
            (object) (Class)
- (instance) timmy = Turtle()
- (instance) tommy = Turtle()
```
- timmy와 tommy는 모두 Turtle의 객체 이지만, 서로 다른 인스턴스 입니다.
- 그리하여, 두 객체는 독립적으로 동작하며 다른 상태를 갖습니다.
