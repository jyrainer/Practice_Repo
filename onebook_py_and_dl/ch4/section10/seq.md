## 시퀀스 자료형 - 리스트
    cmp(list1, list2) 두 리스트의 요소를 비교합니다.
    len(list)  리스트의 전체 길이
    max(list) 리스트에서 최대 값을 가진 항목을 반환
    min(list)  리스트에서 최대 값을 가진 항목을 반환
    list(seq)  튜플을 리스트로으로 변환
    list.append(obj)  obj 오브젝트를리스트에 추가
    list.count(obj) 리스트에 obj가 발생한 횟수를 반환
    list.extend(seq)  리스트에 seq의 내용을 추가    # seq는 시퀀스 자료형
    >>> a
        [0, 1, 2, 3, 4]
    >>> a.extend([3,4])
    >>> a
        [0, 1, 2, 3, 4, 3, 4]
    >>> a.append([3,4])
    >>> a
        [0, 1, 2, 3, 4, 3, 4, [3, 4]]
    list.index(obj) obj가 나타나는 리스트 내의 가장 작은 인덱스를 리턴
    list.insert(index, obj) 리스트에 객체 obj를 오프셋 index 위치에 삽입
    list.pop(obj=list[-1]) 리스트에서 마지막 객체 또는 obj를 제거하여 반환.
    list.remove(obj)  오브젝트 obj를 리스트로부터 삭제
    list.reverse()  리스트의 대상을 반전
    list.sort([func]) 리스트의 객체를 정렬하고, 주어진 compare [func]를 사용합니다.

## 딕셔너리
    cmp(dict1, dict2) : 두 dictionary의 요소를 비교합니다.
    len(dict) : Dictionary의 전체 길이를 제공합니다. 이것은 dictionary에 있는 항목의 수와 같습니다.
    str(dict) : dictionary의 인쇄 가능한 문자열 표현을 생성합니다.
    type(variable) : 전달된 변수의 유형을 반환합니다.
    dict.clear() : dictionary dict의 모든 요소를 제거합니다.
    dict.copy() : dictionary dict의 얕은 복사본을 반환합니다.
    dict.fromkeys() : seq의 키와 값을 value로 설정하여 새 dictionary를 만듭니다.
    dict.get(key, default=None) : 키에 해당 하는 값을 리턴, 키가 dictionary에 없는 경우 default를 리턴
    dict.has_key(key) : dictionary dict에 key가 있으면 true 그렇지 않으면 false를 반환합니다.
    dict.items() : dict (키, 값) 튜플 쌍의 목록을 반환
    dict.keys() : dict의 키 리스트를 반환
    dict.setdefault(key, default=None) : get ()과 유사하지만 키가 dict에 없는 경우 dict [key] = default로 설정
    dict.update(dict2) : dictionary dict2의 키 - 값 쌍을 dict에 추가
    dict.values() : dictionary dict의 값 목록을 반환