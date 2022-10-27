import pandas as pd

class RST_Reader():
    
    def __init__(self, path, names):

        # Creating dictionaries

        self.variaveis = {"STAB" : ["index", "bus1", "bus2", "bus3", "island"],
                          "DAMP" : ["damp", "bus", "island"],
                          "ILVT" : ["violation", "bus", "island"],
                          "IHV"  : ["violation", "bus", "island"],
                          "TLVT" : ["violation", "bus", "island"],
                          "THVT" : ["violation", "bus", "island"],
                          "SDVT" : ["violation", "bus", "island"],
                          "SLVT" : ["violation", "bus", "island"], 
                          "SHVT" : ["violation", "bus", "island"], 
                          "UFRQ" : ["violation", "bus", "island"],
                          "OFRQ" : ["violation", "bus", "island"],
                          "RCOF" : ["violation", "bus", "island"],
                          "NDRC" : ["hz", "time", "inertia"],
                          "NDRB" : ["hz", "time"], 
                          "INRT" : ["s"], 
                          "PGTM" : ["value0", "value1", "value4", "valuef"],
                          "LDSH" : ["value"], 
                          "THRM" : ["loading", "branch", "island"]}

        self.columns = [# "OP", "Gerador", "Hora", "contingence",
                        "File", "Event",
                        "STAB_index", "STAB_bus1", "STAB_bus2", "STAB_bus3", "STAB_island",
                        "DAMP_damp", "DAMP_bus", "DAMP_island",
                        # "RCOF",
                        "NDRC_hz", "NDRC_time", "NDRC_inertia",
                        "INRT_s",
                        "PGTM_value0", "PGTM_value1", "PGTM_value4", "PGTM_valuef"]

        self.names = names
        self.path  = path

        self.data_estab = {}
        for name in names:

            # Read the .rst file

            current_path = path + name + '.rst'            

            with open(current_path) as f: self.lines = f.readlines()
            number_of_events = int(self.lines[2].strip())

            # Identify the stability of events

            dict_estab = {}
            for i in range(4 + number_of_events, len(self.lines)):
                
                current_line = self.lines[i].strip().split()
                if current_line[1] == 'STAB':
                    dict_estab[current_line[0]] = 'INSTAVEL' if float(current_line[2]) == 1 else 'ESTAVEL'

            self.data_estab[name] = dict_estab


    def createCenarios(self):
        
        cenarios = {}
        for name in self.names:

            current_path = self.path + name + '.rst'
            with open(current_path) as f: lines = f.readlines()

            number_of_events = int(lines[2].strip())  
            event_names      = [lines[i].strip().split()[1] for i in range(3, number_of_events+3)]
            current_line     = 4 + number_of_events

            total = {}
            for event in range(1, number_of_events+1):
                var = {}

                if self.data_estab[name][str(event)] == 'ESTAVEL':
                    while(lines[current_line].strip().split()[0] == str(event)):

                        t = lines[current_line].strip().split()
                        a = self.variaveis[lines[current_line].strip().split()[1]]

                        inter = {a[i] : (float(t[2+i]) if t[2+i] != '**********' else '**********') for i in range(len(a))}

                        current_line += 1

                        m = 0
                        while t[1] + str(m) in var: m += 1
                        var[t[1] + str(m)] = inter

                    total[event_names[event-1]] = var

            cenarios[name] = total

        # print(cenarios['bus68']['GL-1'])

        matrix = []
        for name in cenarios.keys():
            for event in cenarios[name].keys():
                # print(event)
                
                matrix.append([name,
                               event,
                               cenarios[name][event]["STAB0"]["index"],
                               str(int(cenarios[name][event]["STAB0"]["bus1"])),
                               str(int(cenarios[name][event]["STAB0"]["bus2"])),
                               str(int(cenarios[name][event]["STAB0"]["bus3"])),
                               str(int(cenarios[name][event]["STAB0"]["island"])),
                               cenarios[name][event]["DAMP0"]["damp"],
                               str(int(cenarios[name][event]["DAMP0"]["bus"])),
                               str(int(cenarios[name][event]["DAMP0"]["island"])),
                               # cenarios[name][event]["RCOF0"]["violation"],
                               cenarios[name][event]["NDRC0"]["hz"],
                               cenarios[name][event]["NDRC0"]["time"],
                               cenarios[name][event]["NDRC0"]["inertia"],
                               cenarios[name][event]["INRT0"]["s"],
                               cenarios[name][event]["PGTM0"]["value0"],
                               cenarios[name][event]["PGTM0"]["value1"],
                               cenarios[name][event]["PGTM0"]["value4"],
                               cenarios[name][event]["PGTM0"]["valuef"]])


        df = pd.DataFrame(matrix, columns=self.columns)

        return cenarios, df

            
if __name__ == '__main__':

    RST = RST_Reader('', ['bus68', 'bus68_2'])
    cenarios, df = RST.createCenarios()

    # print(df.head())