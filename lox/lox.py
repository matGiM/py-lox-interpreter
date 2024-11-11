import sys

class Lox:
  def __init__(self):
    self.had_error = False
    
  """
  Running lox source code through cmd-line using path to file
  """
  def run_file(self, path):
    file = open(path, "r")
    code = file.read()
    file.close()
    self.run(code)

  """
  Implementing the REPL method
  """
  def run_prompt(self):
    while True:
      user_inp = input("> ")
      if user_inp == "<exit REPL>":
        break
      self.run(user_inp)
    
  """
  Implementing the run method to execute lox code
  """  
  def run(self, code):
    local_scanner = scanner.Scanner(code, self)
    tokens = list(local_scanner.scan_tokens())
    
    for token in tokens:
      print(token)
    
#--------------------------------------Main-method-----------------------------------------#
"""
Setting up the main function for lox
"""
number_of_arguements = len(sys.argv)
args = sys.argv

lox_interpreter = Lox()

if __name__ == '__main__':
  if number_of_arguements > 2:
    print("Usage: pylox [script]")
    sys.exit(64)
  elif number_of_arguements == 2:
    lox_interpreter.run_file(args[1])
  else:
    lox_interpreter.run_prompt()
      
      