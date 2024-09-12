from collections import Counter
Greeting = "Hello World"
Name = "Денис"
Number = 1
Types_List = [type(Greeting), type(Name), type(Number)]
Use_Types_List = [type(StrInt) for StrInt in Types_List]
type_counts = Counter(Use_Types_List)
Most_Type = type_counts.most_common(1)[0][0]
print("Найчастіше зустрічається тип даних:",Most_Type)