import random

# define criteria
numbers = '012345689'
special_characters = '!@#$%&*'
characters_lowercase = 'abcdefghijklmnoprtuwxyz'
characters_uppercase = characters_lowercase.upper()


# correct user's answer if out of range

# for numbers in range
def limited_answer_range(prompt, down=None, up=None):       
    answer = input(prompt)

    # is it integer or not?
    try:                                                    
        answer = int(answer)
    except:
        return limited_answer_range(f'You entered wrong type of data. Please enter a number: ', down)
    
    # if yes, check if it is in range
    if int(answer) < down:                                                                              
        return limited_answer_range(f'Your password should have at least {down} characters: ', down)
    else:
        return answer


# for particular words
def limited_answer(prompt, valid_input):
    answer = input(prompt)
    if answer not in valid_input:
        limited_answer(f"Please enter valid data: ", valid_input)
    else:
        return answer


# ask for criteria
len = limited_answer_range('How long your password should be? (min 5 characters) ', 5)
include_numbers = limited_answer('do you want to include numbers? [y/n] ', ['y', 'n'])
include_special_characters = limited_answer('do you want to include special characters? [y/n] ', ['y', 'n'])
include_characters_lowercase = limited_answer('do you want to include lowercase? [y/n] ', ['y', 'n'])
include_character_uppercase = limited_answer('do you want to include uppercase? [y/n] ', ['y', 'n'])

# create list with criteria
criteria = []

if include_numbers == 'y':
    criteria.append(numbers)
if include_special_characters == 'y':
    criteria.append(special_characters)
if include_characters_lowercase == 'y':
    criteria.append(characters_lowercase)
if include_character_uppercase == 'y':
    criteria.append(characters_uppercase)


# generate
def generate(elements, lenght):
    password = []
    limit = 0

    while limit < lenght:
        for x in elements:
            if limit < lenght:
                limit += 1
                password.append(random.choice(x))
            else:
                pass

    random.shuffle(password)

    return ''.join(password)  


print(generate(criteria, len))











