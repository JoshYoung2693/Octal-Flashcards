import random
octal_bin = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
bin_octal = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
reverse = lambda a: 'octal' if a == 'bin' else 'bin'
def random_octal():
    return random.choice(list(octal_bin))
def random_bin():
    return random.choice(list(bin_octal))
def randomize_what_question_that_they_are_asked():
    return random.choice(['bin', 'octal'])
while octal_bin != {} or bin_octal != {}:
    yo = True
    while yo:
        question = randomize_what_question_that_they_are_asked()
        try:
            exec('new_question = random_'+question+'()')
            yo = False
        except:
            yo = True
    answer = input('What is '+new_question+' in '+ reverse(question))
    print(answer == octal_bin[new_question] if question == 'octal' else answer == bin_octal[new_question])
    exec(('octal_bin' if question == 'octal' else 'bin_octal') + '.pop(new_question)')
    
