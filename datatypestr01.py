# 문자열 (str)은 따옴표("" 혹은 '')로 둘러싸인 문자를 의미
# 따옴표 안에 들어간 문자는 종류를 막론하고 문자열이 됨
# 파이썬은 어떤 문자라도 문자열로 사용할 수 있다
# 저장길이에도 제한 없음
# 따옴표를 문자로서 쓰고싶다면 종률가 다른 따옴표를 사용

s = '"I am hungry!"'
print(s)

# 만약 문장 내에서 "와 '를 둘다 문자로 쓰고 싶다면
# 문자로서 사용하는 따옴표 왼쪽에 \(역슬래시)를 붙인다

s2 = "\"설렁탕을 사왔는데 왜 먹지를 못하나...\""
print(s2)

s3 = '\'다이어트는 내일부터 해야지\''
print(s3)

# \를 따옴표 표시가 아닌 \ 문자 자체로 쓴다면 \\ 처럼
# 두 개를 연달아 써야 실제로는 하나가 출력된다

s4 = "\\"
print(s4)