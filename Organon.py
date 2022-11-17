import pandas as pd
import numpy as np

class NetworkData():
    
    def __init__(self, path, other=False):
        
        self.path  = path
        self.time  = 15.0
        self.other = other
        
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
        
        if self.other:
            columns = ['BUS_ID', 'BUS_NAME', 'VBASEKV', 'TP', 'S', 'GSHT_MW', 'BSHMVAR', 'ARE', 'ZON',
                       'MODV_PU', 'ANGV_DEG', 'VMXN_PU', 'VMNN_PU', 'OWN', 'SUB']
        
        
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
        
        if self.other:
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
                         'OWN'      : 'int32',
                         'SUB'      : 'int32'}

        self.DF_bus = self.DF_bus.astype(type_dict)

        
    ### ==========================================================================================================================
    '''
    Function to create a Pandas DataFrame for LOAD data    
    '''
    ### ==========================================================================================================================

    def getLoadDataFrame(self):

        columns = ['BUS_ID' ,'ID', 'ST', 'PL_MW', 'QL_MVAR', 'IPL_MW', 'IQL_MVAR', 'ZPL_MW', 'ZQL_MVAR', 'OWN', 'R0', 'X0', 'Name']
        
        if self.other:
            columns = ['BUS_ID' ,'ID', 'ST', 'descobrir-A', 'descobrir-B', 'PL_MW', 'QL_MVAR', 'IPL_MW', 'IQL_MVAR', 'ZPL_MW', 'ZQL_MVAR', 'OWN']
        
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
        
        if self.other:
            type_dict = {'BUS_ID'   : 'int32',
                         # 'ID'       :, 
                         'ST'       : 'int32', 
                         'PL_MW'    : 'float64', 
                         'QL_MVAR'  : 'float64', 
                         'IPL_MW'   : 'float64', 
                         'IQL_MVAR' : 'float64', 
                         'ZPL_MW'   : 'float64', 
                         'ZQL_MVAR' : 'float64', 
                         'OWN'      : 'int32'}


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
        
        if self.other:
            columns = ['BUS_ID', 'ID', 'PG_MW', 'QG_MVAR', 'QMX_MVAR', 'QMN_MVAR', 'VSPECPU', 'BCO_ID',
                       'BASE_MVA', 'RTRF_PU', 'XTRF_PU', 'TAP_PU', 'ST', 'FP%', 'PMAX_MW', 'PMIN_MW',
                       'GRP', 'BLOCKED']
        
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
        
        if self.other:
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
                         'BLOCKED'   : 'int32'}

        self.DF_gen = self.DF_gen.astype(type_dict)

        self.DF_gen['PMAX_MW'] = self.DF_gen['PG_MW']*1.25

    def networkInfo(self, show=False):

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

        self.total_PMAX_MW_unblock  = self.DF_gen[self.DF_gen['BLOCKED'] == 0]['PMAX_MW'].sum() 
        self.total_PG_MW_unblock    = self.DF_gen[self.DF_gen['BLOCKED'] == 0]['PG_MW'].sum() 
        
        self.total_headroom_unblock = self.total_PMAX_MW_unblock - self.total_PG_MW_unblock
        
        
        self.total_headroom        = self.total_PMAX_MW - self.total_PG_MW
        # print('UNBLOCKED:', self.total_PMAX_MW_unblock)
        
        self.penetration = self.total_PG_RENEW / self.total_PG_MW
        
        if show:
            
            print(' ====================== Network Info ====================== ')
            print(' ======================== GENERATOR ======================= \n')
            print(f' Total Active Power:   {self.total_PG_MW:.4f} MW')
            print(f' Total Reactive Power: {self.total_QG_MVAR:.4f} MVar\n')
            
            print(f' Total Max Active Power: {self.total_PMAX_MW:.4f} MW')
            print(f' Total Min Active Power: {self.total_PMIN_MW:.4f} MW\n')
            
            print(f' Total Renew Active Power: {self.total_PG_RENEW:.4f} MW')
            print(f' Total Sync Active Power:  {self.total_PG_SYNC:.4f} MW\n')
            
            print(f' Total Headroom:             {self.total_headroom:.4f} MW')
            print(f' Total Max Unblocked Power:  {self.total_PMAX_MW_unblock:.4f} MW')
            print(f' Total Head Unblocked Power: {self.total_headroom_unblock:.4f} MW\n')
            
            print(f' Renweable Penetration: {self.penetration*100:.4f} %\n')
            
            print(' ========================== LOAD ========================== \n')
            print(f' Total Active Power:   {self.total_PL_MW:.4f} MW')
            print(f' Total Reactive Power: {self.total_QL_MVAR:.4f} MVar\n\n')

    def changeLoad(self, param, multi, spec=None, arre=2, keepFP=False):
        
        
        ite = spec if spec else [i for i in range(len(self.DF_load))]
        
        if keepFP:
            for i in ite:      
                
                kw, kvar = self.DF_load['PL_MW'].values[i], self.DF_load['QL_MVAR'].values[i]
                FP       = np.cos(np.arctan(kvar/kw))
                
                kw_new   = kw*multi
                kvar_new = np.tan(np.arccos(FP))*kw_new
                
                self.DF_load.loc[i, 'PL_MW']   = kw_new
                self.DF_load.loc[i, 'QL_MVAR'] = kvar_new
                
                
                
#                 MW, MVAR = float(self.DF_load['PL_MW'][i]), float(self.DF_load['QL_MVAR'][i])                    
#                 FP       = MW / np.sqrt(MW**2 + MVAR**2)
                    
#                 new_MW   = MW*multi
#                 new_MVAR = np.sqrt((new_MW/FP)**2 - new_MW**2)
                    
#                 self.DF_load['PL_MW'][i]   = round(new_MW,   arre) 
#                 self.DF_load['QL_MVAR'][i] = round(new_MVAR, arre)                  

        else:      
            for i in ite:
                self.DF_load[param][i] = round(float(self.DF_load.iloc[i][param])*multi, arre)    
                
        self.cargaTotal = 0
        for i in self.DF_load['PL_MW'].values:
            self.cargaTotal += float(i)
            
    def changeGenType(self, gen_index, new_type):
        self.DF_gen.loc[gen_index, 'TYPE'] = new_type

    def blockGen(self, value):
        self.networkInfo()

        threshold = self.total_PL_MW * value

        sort = self.DF_gen.sort_values(by=["PMAX_MW"])
        sort = sort[sort['TYPE'] != 4]

        removed_gen, generators = 0, []

        for gen in sort['BUS_ID'].values:

            current_gen = self.DF_gen[self.DF_gen['BUS_ID'] == gen]['PMAX_MW'].values[0]

            # print(f'{gen:2d} : {current_gen}')

            teste = self.total_PMAX_MW - removed_gen - current_gen

            if teste >= threshold:
                removed_gen += current_gen
                generators.append(gen)

            else:
                break

        generators_idx = np.asarray(generators) - 1

        # print(threshold, generators, generators_idx)

        self.DF_gen.loc[generators_idx, 'BLOCKED'] = 1 

        self.networkInfo()

        # print(sort['BUS_ID'].values)

    def save(self, save_path):
        
        # GEN
        
        for idx, i in enumerate(range(self.f_gen, self.l_gen+1)):
            
            new_line = ''
            for j in range(len(self.DF_gen.iloc[idx])):
                if j != len(self.DF_gen.iloc[idx])-1:
                    
                    if len(str(self.DF_gen.iloc[idx, j])) < 5:
                        new_line += f'{str(self.DF_gen.iloc[idx, j]): >6}' + ','
                    elif len(str(self.DF_gen.iloc[idx, j])) >= 5 and len(str(self.DF_gen.iloc[idx, j])) < 10:
                        new_line += f'{str(self.DF_gen.iloc[idx, j]): >11}' + ','
                    else:
                        new_line += f'{str(self.DF_gen.iloc[idx, j]): >14}' + ','
                    
                    
                    
                    #new_line += str(self.DF_gen.iloc[idx, j]) + ','
                else:
                    new_line += '  ' + str(self.DF_gen.iloc[idx, j]) + '/'
                
            self.lines[i] = new_line + ' \n'
            
        # LOAD
            
        for idx, i in enumerate(range(self.f_load, self.l_load+1)):
            
            new_line = ''
            for j in range(len(self.DF_load.iloc[idx])):
                if j != len(self.DF_load.iloc[idx])-1:
                    
                    if len(str(self.DF_load.iloc[idx, j])) < 5:
                        new_line += f'{str(self.DF_load.iloc[idx, j]): >6}' + ','
                    elif len(str(self.DF_load.iloc[idx, j])) >= 5 and len(str(self.DF_load.iloc[idx, j])) < 10:
                        new_line += f'{str(self.DF_load.iloc[idx, j]): >11}' + ','
                    else:
                        new_line += f'{str(self.DF_load.iloc[idx, j]): >14}' + ','
                    
                else:
                    new_line += '  ' + str(self.DF_load.iloc[idx, j]) + '/'
                
            self.lines[i] = new_line + ' \n'
            
        # SAVE
            
        with open(save_path, 'w') as f:
            for line in self.lines:
                f.write(line)


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

    ND.blockGen(0.5)

    # print(ND.DF_gen['BLOCKED'])
    ND.save('bb.ntw')

    # ND.DF_bus = ND.DF_bus.astype({'BUS_ID': 'int32'})

    # print(type(ND.DF_load['BUS_ID'][0]))