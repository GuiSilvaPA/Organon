from PLT_Reader import PLT_Reader

PLT = PLT_Reader('Estudo_GOV/GOV09/ALTA/Bus9/Evento_1.plt')

for idx, name in enumerate(PLT.var_dic.keys()):
    print(idx+1, name)