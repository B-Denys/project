Ordinary_dict = {"звичайній_ключ1": "Hello World", "звичайній_ключ2": 1.2, "звичайній_ключ3": [1, 2, 3], "звичайній_ключ4": True, "звичайній_ключ5": None}
Main_dict = {"ключ1": "Hello World", "ключ2": 12, "ключ3": Ordinary_dict, "ключ4": [10, 20, 30]}
Type_dict = {"ключ1": type(Main_dict["ключ1"]), "ключ2": type(Main_dict["ключ2"]), "ключ3": type(Main_dict["ключ3"]), "ключ4": type(Main_dict["ключ4"])}
Ordinary_type_dict = {"звичайній_ключ1": type(Ordinary_dict["звичайній_ключ1"]), "звичайній_ключ2": type(Ordinary_dict["звичайній_ключ2"]), "звичайній_ключ3": type(Ordinary_dict["звичайній_ключ3"]), "звичайній_ключ4": type(Ordinary_dict["звичайній_ключ4"]), "звичайній_ключ5": type(Ordinary_dict["звичайній_ключ5"])}
print("Головній та звичайній словник:", Main_dict)
print("Словник з типами даних головного словника:", Type_dict)
print("Словник з типами даних звичайного словника:", Ordinary_type_dict)