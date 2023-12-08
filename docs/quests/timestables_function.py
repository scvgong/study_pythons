# - [30, 35, 20] 단 대한 출력
# - timestables_fors.py -> function 화
# - option) [30, 35, 20] 부분 사용자 입력, 'q'이면 종료

# [30,35,20] 단에 대한 출력
def multiply():
    gugu = [30, 35, 20]
    list_num = [1,2,3,4,5,6,7,8,9]

    for list_gugu in gugu:
        print("{}단 출력".format(list_gugu))

        for list_number in list_num:
            pass    
            result = print("{} * {} = {}".format(list_gugu,list_number,(list_gugu * list_number)))
    
    return result

def main():
    print("30,35,20단 출력")
    final_result = print(multiply())
    return final_result

main()

# 입력 받아서 하기
def multiply_input():
    gugu = input("30,35,20 입력해주세요 : ")
    list_num = [1,2,3,4,5,6,7,8,9]

    while True:
        if gugu == 'q':
            print("프로그램 종료")
            break
        else:
            for list_number in list_num:
                pass    
                result = int(gugu) * int(list_number)
                print("{} * {} = {}".format(gugu,list_number,result))
        gugu = input("30,35,20 입력해주세요 : ")        
        continue
    
    return

def main_input():
    
    final_result = print(multiply_input())
    return final_result

main_input()
