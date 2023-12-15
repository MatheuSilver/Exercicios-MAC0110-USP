debug_num

def arithmetic_arranger(problems, show_solutions=False):
  number_of_lines = 3
  if show_solutions:
    number_of_lines +=1 #add the result line.

  arranged_problems = ''
  line = 0
  while line < number_of_lines:
    new_line = ''
    for problem in problems:
      problem = problem.strip().split()
      max_size = get_max_size(problem)
      counter = 0
      
      print(line)
      while counter < max_size - len(problem[line]) + 2:
        if len(problem[line]) < 1:
          new_line += problem[line]
          line += 1
          counter +=1
        new_line += ' '
        counter +=1
        
      new_line += problem[line] + '    '
      line -= 1
    new_line.rstrip()
    arranged_problems += new_line + '\n'
    
    line +=1
  print(arranged_problems)
  return arranged_problems

def get_max_size(array):
  size = 0
  for member in array:
    if len(member) > size:
      size = len(member)

  return size

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])