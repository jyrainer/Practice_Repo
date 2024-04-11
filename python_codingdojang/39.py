# 표준 입력으로 정수 세 개가 입력됩니다
# (첫 번째 정수는 시작하는 초, 두 번째 정수는 반복을 끝낼 초, 세 번째 정수는 인덱스이며 입력되는
# 초의 범위는 0~100000, 입력되는 인덱스의 범위는 0~10입니다).
# 다음 소스 코드에서 시간 값을 생성하는 이터레이터를 만드세요.

# 시간 값은 문자열이고 시:분:초 형식입니다. 만약 숫자가 한 자리일 경우 앞에 0을 붙입니다(예: 12:01:08).
# 1초는 00:00:01입니다. 23:59:59를 넘길 경우 00:00:00부터 다시 시작해야 합니다.
# 시간은 반복을 끝낼 초 직전까지만 출력해야 합니다(반복을 끝낼 초는 포함되지 않음).
# judge_iterator.py

###

class TimeIterator:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else :
            time_str = self.decord(self.current)
            self.current += 1
            return time_str
    
    def __getitem__(self, index):
        if index < self.stop - self.start:
            current_time = self.decord(self.start + index)
            return current_time
        else :
            raise IndexError

    @staticmethod
    def decord(second):
        """
        초를 00:00:00으로 decord, 23:59:59다음에는 0으로 초기화.
        """
        hours, minutes, seconds = [0,0,0]
        hours,left_seconds = (second // 3600)%24 , second % 3600
        minutes, left_seconds = (left_seconds // 60), left_seconds % 60
        seconds = left_seconds % 60
        if hours < 10:
            hours = f"0{hours}"
        if minutes< 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        return f"{hours}:{minutes}:{seconds}"



###
start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')

# 예
# 입력
# 0 3 2
# 결과
# 00:00:00
# 00:00:01
# 00:00:02

# 00:00:02
# 입력
# 88234 88237 1
# 결과
# 00:30:34
# 00:30:35
# 00:30:36

# # 00:30:35