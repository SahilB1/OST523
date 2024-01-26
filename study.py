import random

def L17():
    content = open("L17.txt", "r")
    txt = str(content.read())
    split_txt = txt.split("NEXT")
    
    test = {}
    for line in split_txt:
        split_line = line.split("\n")
        correct_answers = split_line[1].split(",")[1:]
        questions = split_line[3:]
        for i, q in enumerate(questions):
            complete_question = ""
            qa = q.split("?")
            question = qa[0]
            answers = qa[1].split("*")
            complete_question += (question + "?\n")
            for a in answers:
                complete_question += a + "\n"
            test[complete_question] = correct_answers[i]
    
    keys = list(test.keys())
    total_correct = 0
    for key in keys:
        print(key)
        print()
        user_answer = input("Your answer?\t")
        if user_answer.lower().strip() == test[key].lower().strip():
            print("Correct!\n\n")
            total_correct += 1
        else:
            print("Incorrect | Correct Answer:", test[key], "\n\n")
    return total_correct

def study_ost():
    content = open("input.txt", "r")
    txt = str(content.read())
    split_txt = txt.split("NEXT")
    
    test = {}
    for line in split_txt:
        split_line = line.split("\n")[:-1]
        correct_answers = split_line[1].split(",")[1:]
        questions = split_line[3:]
        for i, q in enumerate(questions):
            complete_question = ""
            qa = q.split("?")
            question = qa[0]
            answers = qa[1].split("*")
            complete_question += (question + "?\n")
            for a in answers:
                complete_question += a + "\n"
            test[complete_question] = correct_answers[i]
    
    keys = list(test.keys())
    random.shuffle(keys)
    total_correct = 0
    for i, key in enumerate(keys):
        print(key)
        print()
        user_answer = input("Your answer?\t")
        if i == len(keys) // 2:
            total_correct += L17()
        elif user_answer.lower().strip() == test[key].lower().strip():
            print("Correct!\n\n")
            total_correct += 1
        else:
            print("Incorrect | Correct Answer:", test[key], "\n\n")

    print("Grade:", str(total_correct) + "/" + str(len(keys)))
    print("Percent Correct:", str(int(100 * (total_correct/(len(keys) + 5)))) + "%")
            
if __name__ == "__main__":
    study_ost()