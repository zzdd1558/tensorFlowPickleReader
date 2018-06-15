### tensorflow를 활용하기위해 Math관련 digit, operator로 구성된 pickle Reader

> features와 label로 구성되어 있으며

> Vector값으로 구성되어있음 28 * 28인 총 784개로 구성되어있으며. 0 ~ 1로 gray scale처리가 되어있다.

> 사용할 경우 28 * 28로 reshape해서 사용해야 할것이다.

> Label은 one_hot으로 구성되어있다.

#### 직접 사용하기 위해서는 class를 통해 객체를 생성하고 메소드에 파일 경로를 넣어주고 실행하면 된다.
