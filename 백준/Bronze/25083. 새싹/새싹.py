# print("         ,r'\"7")
# print("r`-_   ,\'  ,/")
# print(" \\. \". L_r\'")
# print("   `~\\/")
# print("      |")
# print("      |")

# ' 또는 " 또는 \를 출력하기 위해서는 \표시를 눌러 해당 기호들 앞에 ＼를 넣어줘야 한다는 걸 잊지 말자.
#  "r"을 추가하여 raw string으로 만들 수 있다. raw string은 이스케이프 문자를 해석하지 않고 문자 그대로 인식함
#    이 경우 print(r"   `~\/") 이렇게 작성함

# 아래처럼 해결도 가능. 아래 코드에서 r 접두사는 원시(raw) 문자열. 
# 이를 사용하면 백슬래시(\)가 이스케이프 문자로 해석되지 않고 문자열 그대로의 값 가짐
art = r'''         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |'''
print(art)
