prompt = "Please give your height so we can calculate your BMI"
prompt += "\nWhat is your height: "

height = input(prompt)
Con_height = int(height)

if Con_height <= 40:
    print(f"you are short for basketball, consider football!")
elif Con_height <= 20:
    print(f"you are very short, consider another career")
else:
    print(f"you are eligible to apply to the team")
