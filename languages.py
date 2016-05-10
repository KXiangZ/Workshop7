from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

output="The dynamically typed languages are:\n"

language_list=[ruby,python,vb]
for element in language_list:
    if ProgrammingLanguage.is_dynamic(element.typing):
      output+=element.name+"\n"
print(output)


