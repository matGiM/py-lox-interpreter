import importlib
from token import Token

"""
Import TokenType from 'token' directory
"""
file_path = 'py-lox-interpreter/token/token_type.py'
spec = importlib.util.spec_from_file_location("token_type", file_path)
token_type = importlib.util.module_from_spec(spec)
importlib.sys.modules["token_type"] = token_type
spec.loader.exec_module(token_type)

class Scanner:
  def __init__(self, isource):
    self.source = isource
    self.tokens = []
    self.start = 0
    self.current = 0
    self.line = 1
  
  """
  Loop over the source code and add tokens to the tokens list
  until there are no more characters in the source code  
  """
  def scan_tokens(self):
    while not self._is_at_end():
      self.start = self.current
      self._scan_token
      #TODO implement _scan_token function
      
    #At the end add an EOF token for cleaner parser
    self.tokens.append(Token(token_type.EOF, "", None, self.line))
    return self.tokens

  def _is_at_end(self):
    return self.current >= len(self.source)