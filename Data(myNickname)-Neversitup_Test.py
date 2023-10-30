import inquirer


def main():
    choices=[
        'Question 1 : Permutations',
        'Question 2 : Find the odd int',
        'Question 3 : Count the smiley faces! XD'
    ]
    questions = [
        inquirer.List('Question',
            message="What part do you want to access?",
            choices=[
                'Question 1 : Permutations',
                'Question 2 : Find the odd int',
                'Question 3 : Count the smiley faces! XD',
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    if (answers["Question"] == choices[0]):
        # print("1")
        Permutations()
    elif (answers["Question"] == choices[1]):
        # print("2")
        FindTheOddInt()
    elif (answers["Question"] == choices[2]):
        # print("3")
        CountTheSmileyFaces()
    print ("End of "+answers["Question"]+"\n")
    print ("#-----------------------------#\n")
    confirm = {
        inquirer.Confirm('confirmed',
            message="Do you want to end all process?",
            default=True
        ),
    }
    confirmation = inquirer.prompt(confirm)
    if confirmation["confirmed"]:
        return
    else:
        main()

def test():
    print("Mountain")
    questions = [
    inquirer.List('Question',
            message="What part do you want to access?",
            choices=[
                'Question 1 : Permutations',
                'Question 2 : Find the odd int',
                'Question 3 : Count the smiley faces! XD',
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    print (answers["Question"])

def Permutations():
    print()
    print("Question 1 : Permutations")
    temp_input = (str(input("Input your Text : "))).strip()
    result = PermutationsAssist(temp_input)
    print("With input \'"+temp_input+"\':")
    print("Functon return => "+str(result))
    print("Functon return output count : "+str(len(result)))

def PermutationsAssist(input_str):
    if len(input_str) <= 1:
        return [input_str]

    permutations = []
    for i in range(len(input_str)):
        first_char = input_str[i]
        remaining_chars = input_str[:i] + input_str[i+1:]
        remaining_permutations = PermutationsAssist(remaining_chars)
        for perm in remaining_permutations:
            permutations.append(first_char + perm)

    return permutations

def FindTheOddInt():
    print()
    print("Question 2 : Find the odd int ")
    print("input your odds set (ex. 2,2,2,3,3 or [0,1,0,1,0])")
    print("\t concern about \",\"")
    temp_input = str(input(" : "))
    temp_input,ans_num,ans_count = FindTheOddIntAssist(temp_input)
    print(f"{temp_input} should return {ans_num} ,because it occurs {ans_count} time (which is odd).")
    '''number = int(input())
    factors = PrimeFactorsList(number)
    print(f"{number} คือ {factors}")
    questions = [
    inquirer.List('Question',
            message="choice the way to input for Function",
            choices=[
                '1.) Input Number for split it be a prime number (ex. 12 split it to [2,2,3], 10 split it to [2,5])',
                '2.) Input Numbers set (ex. [7], [0,1,2,3])',
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    print (answers["Question"])'''

def FindTheOddIntAssist(temp_input):
    temp_input = [int(item.strip("[' ]")) for item in temp_input.split(",")]
    ans_num = 0
    ans_count = 0
    for _ in temp_input:
        if temp_input.count(_)%2 != 0:
            if ans_count < temp_input.count(_):
                ans_num = _
                ans_count = temp_input.count(_)
            
    return (temp_input,ans_num,ans_count)

def CountTheSmileyFaces():
    print()
    print("Question 3 : Count the smiley faces!")
    print("input your faces set (ex. [';D', ':-(', ':-)', ';~)'] or :), ;D, XD")
    print("\t concern about \",\"")
    temp = str(input(""))
    faces_list = [str(item.strip("[' ]")) for item in temp.split(",")]
    count = 0
    for _ in faces_list:
        # print(_)
        if (SmileFacesCheck(_)):
            count += 1
    print(f"{temp} have smile face about {count}")

def SmileFacesCheck(face):
    Eyes,Mouth,Valid = "","",""
    # print(len([*face]))
    if (len([*face])>=3):
        Eyes, Valid, Mouth = ([*face][0].strip("' "),[*face][1].strip("' "),[*face][2].strip("' "))
    else:
        # Eyes, Mouth = ([*face][0].strip("' "),[*face][1].strip("' "))
        Eyes = [*face][0].strip("' ")
        if (len([*face])>=2):
            Mouth = [*face][1].strip("' ")
    # print(Eyes,Valid,Mouth)
    # print(f"Eyes {Eyes}")
    # print(f"Valid {Valid}")
    # print(f"Mouth {Mouth}")
    # print(face,end=" ")
    if ((Mouth == ")") or (Mouth == "D")):
        # print("True",end=" ")
        if len(Valid) <= 1:
            # print("True",end=" ")
            if ((Eyes == ":") or (Eyes == ";")):
                # print("True",end=" ")
                return True
    return False


def PrimeFactorsList(n):
    prime_factors_list = PrimeFactors(n)
    return prime_factors_list

def PrimeFactors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors



if __name__ == '__main__':
    main()