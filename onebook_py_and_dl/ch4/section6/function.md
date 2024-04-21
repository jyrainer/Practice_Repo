## 함수의 유용성
1. 하나의 큰 프로그램을 여러가지로 분리함으로 써 **구조적 프로그래밍**이 가능
2. 코드의 재활용
3. 함수의 기능과 내부 구현을 분리하는 캡슐화

## 함수 호출 순서
1. 루틴에서 함수가 호출된다. 함수가 가지는 특정 매개변수(parameter)에 값이 전달된다. 전달되는 값을 인자(argument)라고 한다.
2. 함수 내부의 계산을 수행한다.
3. 함수 종료 시 기존 루틴으로 돌아온다. 반한값(return)이 존재 시 해당 값을 사용하기도 한다.

## 함수의 종류
1. 내장 함수(built-in function)
    - 정의(import)가 필요하지 않다.
    - 예) abs(), hash(), sorted(), list() ...
2. 외장 함수
    - import 문을 사용하여 외부의 라이브러리에서 제공하는 함수
    - 기본 라이브러리들은 파이썬 설치시 사용 가능함
    - 예) sys, pickle, os, glob, time ...
3. 사용자 정의 함수(User defined fuction)
4. Pass by reference vs value
    - 파이썬의 모든 매개변수는 참조(reference)로 전달된다.
    - 함수 내에서 매개변수가 참조하는 것을 변경하면 변경 내용은 호출된 함수에 다시 반영된다.   
        ```
        # Function definition is here
        def changeme(mylist):
            "This changes a passed list into this function"
            mylist.append([1,2,3,4]);
            print "Values inside the function: ", mylist
            return
        # Now you can call changeme function
        mylist = [10,20,30];
        changeme(mylist);
        print "Values outside the function: ", mylist
        ```   
        ` Values inside the function:  [10, 20, 30, [1, 2, 3, 4]] `   
        ` Values outside the function:  [10, 20, 30, [1, 2, 3, 4]] `

5. 람다식(Lambda, Anonymous Functions)
    - 일반적인 함수는 객체를 만들고, 재사용을 위해 함수를 메모리에 할당하지만, 람다(익명함수)는 한번 쓰이고 다음줄로 넘어가면 메모리 영역에서 사라진다.
        ```
        def cube(y):
            return y * y * y;
        
        g = lambda x: x * x * x
        
        print(g(7))
        print(cube(5))