
def question():
    mixed_question = [] # 최종
    dict_question = {} # 질문

    # 문제 입력
    for i in range(3):
        question = input("question : ")
        dict_question['question'] = question
        # 답변 입력
        list_answers = []
        for x in range(4):
            answer = input("answer : ")
            list_answers.append(answer)
            pass
        pass
            
        # correct, score 입력            
        correct = int(input("correct_index : "))
        score = int(input("score : "))

        dict_question['answer'] = list_answers
        dict_question['correct_index'] = correct
        dict_question['socre'] = score

            
        mixed_question.append(dict_question.copy())
    return mixed_question

result = question()
print(result)