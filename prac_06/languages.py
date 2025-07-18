from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
             ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
             ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

dynamic_languages = [language for language in languages if language.is_dynamic()]
for language in dynamic_languages:
    print(language)