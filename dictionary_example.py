'''
#Find the average,grade(a/b/c/d/e/f),result(pass/fail) for every student
#id name  average grade result
'''
data = [{"id":101,"name":"ravi","p":15,"c":20,"m":56},
        {"id":102,"name":"sahil","p":15,"c":20,"m":56},
        {"id":103,"name":"manish","p":40,"c":63,"m":56},
        {"id":104,"name":"Ram","p":10,"c":20,"m":5},
        {"id":105,"name":"dev","p":95,"c":90,"m":96}]
for item in data:
    avg = (item["p"]+item["c"]+item["m"])//3
    grade = None
    if avg>80:
        grade = 'A'
    elif avg>60:
        grade = "B"
    elif avg>45:
        grade="C"
    elif avg>33:
        grade="D"
    else:
        grade="F"
    result = "PASS" if (avg>33) else "FAIL"
    data[data.index(item)]["avg"]=avg
    data[data.index(item)]["result"]=result



import pandas as pd
df = pd.DataFrame(data)
print(df)
