school_dict={'Alice':55,'Snoop':64,'Kim':75,'Jay':98}
#prompts the user to input the student name
name= input("Enter the name of the student:")
if name in school_dict.keys():
    print(f"{name}'s mark is:{school_dict[name]}")
else:
    print(f"Student Not Found.")