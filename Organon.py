import pandas as pd
import numpy as np

class NetworkData():
    
    def __init__(self, path):
        
        self.path = path
        self.time = 15.0
        
        with open(path) as f:
            self.lines = f.readlines()

        self.f_bus = 4

        for idx, line in enumerate(self.lines):

            if 'END OF BUS DATA'  in line: self.l_bus  = idx - 1

            if 'BEGIN LOAD DATA'  in line: self.f_load = idx + 2
            if 'END OF LOAD DATA' in line: self.l_load = idx - 1

            if 'BEGIN GENERATOR DATA'  in line: self.f_gen = idx + 2
            if 'END OF GENERATOR DATA' in line: self.l_gen = idx - 1

        self.getBusDataFrame()
        self.getLoadDataFrame()
        self.getGenDataFrame()

    ### ==========================================================================================================================
    '''
    Function to create a Pandas DataFrame for BUS data    
    '''
    ### ==========================================================================================================================

    def getBusDataFrame(self):

        columns = ['BUS_ID', 'BUS_NAME', 'VBASEKV', 'TP', 'S', 'GSHT_MW', 'BSHMVAR', 'ARE', 'ZON',
                  'MODV_PU', 'ANGV_DEG', 'VMXN_PU', 'VMNN_PU', 'VMXE_PU', 'VMNE_PU', 'OWN', 'SUB', 'ARG']
        data    = []

        for i in range(self.f_bus, self.l_bus + 1):
            bus_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(',', ' ').split()
            data.append(bus_info)

        self.DF_bus = pd.DataFrame(data, columns=columns)

        type_dict = {'BUS_ID'   : 'int32',
                     # 'BUS_NAME' :,
                     'VBASEKV'  : 'float64',
                     'TP'       : 'int32',
                     'S'        : 'int32',
                     'GSHT_MW'  : 'float64',
                     'BSHMVAR'  : 'float64',
                     'ARE'      : 'int32',
                     'ZON'      : 'int32',
                     'MODV_PU'  : 'float64',
                     'ANGV_DEG' : 'float64',
                     'VMXN_PU'  : 'float64',
                     'VMNN_PU'  : 'float64',
                     'VMXE_PU'  : 'float64',
                     'VMNE_PU'  : 'float64',
                     'OWN'      : 'int32',
                     'SUB'      : 'int32',
                     'ARG'      : 'int32'}

        self.DF_bus = self.DF_bus.astype(type_dict)

        
    ### ==========================================================================================================================
    '''
    Function to create a Pandas DataFrame for LOAD data    
    '''
    ### ==========================================================================================================================

    def getLoadDataFrame(self):

        columns = ['BUS_ID' ,'ID', 'ST', 'PL_MW', 'QL_MVAR', 'IPL_MW', 'IQL_MVAR', 'ZPL_MW', 'ZQL_MVAR', 'OWN', 'R0', 'X0', 'Name']
        data    = []

        for i in range(self.f_load, self.l_load + 1):
            load_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(',', ' ').split()
            data.append(load_info)

        self.DF_load = pd.DataFrame(data, columns=columns)
        # print(data[0])

        type_dict = {'BUS_ID'   : 'int32',
                     # 'ID'       :, 
                     'ST'       : 'int32', 
                     'PL_MW'    : 'float64', 
                     'QL_MVAR'  : 'float64', 
                     'IPL_MW'   : 'float64', 
                     'IQL_MVAR' : 'float64', 
                     'ZPL_MW'   : 'float64', 
                     'ZQL_MVAR' : 'float64', 
                     'OWN'      : 'int32', 
                     'R0'       : 'float64', 
                     'X0'       : 'float64', 
                     # 'Name'     :
                     }

        self.DF_load = self.DF_load.astype(type_dict)

    ### ==========================================================================================================================
    '''
    Function to create a Pandas DataFrame for GENERATION data    
    '''
    ### ==========================================================================================================================

    def getGenDataFrame(self):

        columns = ['BUS_ID', 'ID', 'PG_MW', 'QG_MVAR', 'QMX_MVAR', 'QMN_MVAR', 'VSPECPU', 'BCO_ID',
                   'BASE_MVA', 'RTRF_PU', 'XTRF_PU', 'TAP_PU', 'ST', 'FP%', 'PMAX_MW', 'PMIN_MW',
                   'GRP', 'BLOCKED', 'OWNER', 'CONECTION', 'R1', 'X1', 'R2', 'X2', 'R0', 'X0', 'RGRD',
                   'XGRD', 'XQ', 'SF', 'MAXANG', 'TYPE', 'NAME', 'NMAX', 'NON']
        data    = []

        for i in range(self.f_gen, self.l_gen + 1):
            gen_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(',', ' ').split()
            data.append(gen_info)

        self.DF_gen = pd.DataFrame(data, columns=columns)
        # print(data[0])

        type_dict = {'BUS_ID'    : 'int32',
                     # 'ID'        :, 
                     'PG_MW'     : 'float64', 
                     'QG_MVAR'   : 'float64', 
                     'QMX_MVAR'  : 'float64', 
                     'QMN_MVAR'  : 'float64', 
                     'VSPECPU'   : 'float64', 
                     'BCO_ID'    : 'int32',
                     'BASE_MVA'  : 'float64', 
                     'RTRF_PU'   : 'float64', 
                     'XTRF_PU'   : 'float64', 
                     'TAP_PU'    : 'float64', 
                     'ST'        : 'int32', 
                     'FP%'       : 'float64', 
                     'PMAX_MW'   : 'float64', 
                     'PMIN_MW'   : 'float64',
                     'GRP'       : 'int32', 
                     'BLOCKED'   : 'int32', 
                     'OWNER'     : 'int32', 
                     'CONECTION' : 'int32', 
                     'R1'        : 'float64', 
                     'X1'        : 'float64', 
                     'R2'        : 'float64', 
                     'X2'        : 'float64', 
                     'R0'        : 'float64', 
                     'X0'        : 'float64', 
                     'RGRD'      : 'float64',
                     'XGRD'      : 'float64', 
                     'XQ'        : 'float64', 
                     'SF'        : 'float64', 
                     'MAXANG'    : 'float64', 
                     'TYPE'      : 'int32', 
                     # 'NAME'      :, 
                     'NMAX'      : 'int32', 
                     'NON'       : 'int32'
                     }

        self.DF_gen = self.DF_gen.astype(type_dict)

        self.DF_gen['PMAX_MW'] = self.DF_gen['PG_MW']*1.25

    def networkInfo(self):

        self.total_PL_MW   = self.DF_load['PL_MW'].sum()   
        self.total_QL_MVAR = self.DF_load['QL_MVAR'].sum() 
        # print(self.total_PL_MW, self.total_QL_MVAR)

        self.total_PG_MW   = self.DF_gen['PG_MW'].sum()    
        self.total_QG_MVAR = self.DF_gen['QG_MVAR'].sum() 
        # print(self.total_PG_MW, self.total_QG_MVAR)

        self.total_PMAX_MW = self.DF_gen['PMAX_MW'].sum()  
        self.total_PMIN_MW = self.DF_gen['PMIN_MW'].sum()
        # print(self.total_PMAX_MW, self.total_PMIN_MW)

        self.reserva_total   = self.total_PMAX_MW - self.total_PG_MW
        self.reserva_per_gen = self.DF_gen['PMAX_MW'] - self.DF_gen['PG_MW']

        self.total_PG_RENEW = self.DF_gen[self.DF_gen['TYPE'] == 4]['PG_MW'].sum() 
        self.total_PG_SYNC  = self.total_PG_MW - self.total_PG_RENEW
        # print(self.total_PG_RENEW, self.total_PG_SYNC)

        self.total_PMAX_MW_unblock = self.DF_gen[self.DF_gen['BLOCKED'] == 0]['PMAX_MW'].sum() 
        print('UNBLOCKED:', self.total_PMAX_MW_unblock)



        # np.asarray([float(i) for i in self.DF_gen['PMAX_MW'].values]) - np.asarray([float(i) for i in self.DF_gen['PG_MW'].values])

        # for idx, i in enumerate(self.reserva_per_gen):
        #     print(idx+1, i)

    def blockGen(self, value):
        self.networkInfo()

        threshold = self.total_PL_MW * value

        sort = self.DF_gen.sort_values(by=["PMAX_MW"])
        sort = sort[sort['TYPE'] != 4]

        removed_gen = 0
        generators  = []

        for gen in sort['BUS_ID'].values:

            current_gen = self.DF_gen[self.DF_gen['BUS_ID'] == gen]['PMAX_MW'].values[0]

            print(f'{gen:2d} : {current_gen}')

            teste = self.total_PMAX_MW - removed_gen - current_gen

            if teste >= threshold:
                removed_gen += current_gen
                generators.append(gen)

            else:
                break

        generators_idx = np.asarray(generators) - 1

        print(threshold, generators, generators_idx)

        self.DF_gen.loc[generators_idx, 'BLOCKED'] = 1 

        self.networkInfo()

        print(sort['BUS_ID'].values)



if __name__ == '__main__':
    path = 'C:/Users/Scarlet/Desktop/bus68/bus68.ntw'

    ND = NetworkData(path)

    # print(OPG.l_bus, OPG.f_load, OPG.l_load, OPG.f_gen, OPG.l_gen)

    # for i in range(OPG.f_load, OPG.l_load + 1):
    #     print(OPG.lines[i].strip())

    # for bus in OPG.data:
    #     print(bus)

    # print(ND.DF_gen['BLOCKED'])
    # ND.networkInfo()

    ND.blockGen(1.1)

    print(ND.DF_gen['BLOCKED'])

    # ND.DF_bus = ND.DF_bus.astype({'BUS_ID': 'int32'})

    # print(type(ND.DF_load['BUS_ID'][0]))