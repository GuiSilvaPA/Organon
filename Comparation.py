import matplotlib.pyplot as plt
from PLT_Reader import PLT_Reader



class EventPlotComparation():


    def __init__(self):
        pass


    def innerGeneratorComparation(self, n_gen, n_var, GOV, Event):

        self.fig, self.axs = plt.subplots(nrows=2, ncols=n_gen, sharex=True, figsize=(15, 8))        

        self.plotGenerator('Estudo_GOV/'+GOV+'/ALTA/Bus9/' +Event+'.plt', n_var, multi=1, label='ALTA')
        self.plotGenerator('Estudo_GOV/'+GOV+'/MEDIO/Bus9/'+Event+'.plt', n_var, multi=1, label='MEDIO')
        self.plotGenerator('Estudo_GOV/'+GOV+'/LEVE/Bus9/' +Event+'.plt', n_var, multi=1, label='LEVE')

        title = ['Gerador 1', 'Gerador 2', 'Gerador 3']

        for idx, ax in enumerate(self.axs[0]):
            ax.set_ylabel('Pm [MW]')
            ax.set_title(title[idx])
            ax.grid()
            ax.legend()

        self.plotEvent('Estudo_GOV/'+GOV+'/ALTA/Bus9/' +Event+'.plt', n_var, 0, multi=1, label=None)
        self.plotEvent('Estudo_GOV/'+GOV+'/MEDIO/Bus9/'+Event+'.plt', n_var, 1, multi=1, label=None)
        self.plotEvent('Estudo_GOV/'+GOV+'/LEVE/Bus9/' +Event+'.plt', n_var, 2, multi=1, label=None)

        title = ['Patamar de Carga Leve', 'Patamar de Carga Media', 'Patamar de Carga Alta']

        for idx, ax in enumerate(self.axs[1]):
            ax.set_ylabel('Pm [MW]')
            ax.set_xlabel('Time [s]')
            ax.set_title(title[idx])
            ax.grid()
            ax.legend()


    def plotGenerator(self, path, n_var, multi=1, label=None):

        organon = PLT_Reader(path)

        for idx, ind in enumerate(n_var):

            self.axs[0, idx].plot(organon.var_dic['Tempo - segundos'],
                                  organon.var_dic[organon.lines[ind].rstrip()]*multi,
                                                                            
                                  label=label)

    def plotEvent(self, path, n_var, n_event, multi=1, label=None, pos=1):

        organon = PLT_Reader(path)

        for idx, ind in enumerate(n_var):

            self.axs[pos, n_event].plot(organon.var_dic['Tempo - segundos'],
                                        (organon.var_dic[organon.lines[ind].rstrip()] - organon.var_dic[organon.lines[ind].rstrip()].min())*multi,
                                                                            
                                        label=label+organon.lines[ind].rstrip()[-1])
            

    def eventGeneratorComparation(self, n_gen, n_var, Event):

        self.fig, self.axs = plt.subplots(nrows=2, ncols=n_gen, sharex=True, figsize=(15, 8))        

        self.plotEvent('Estudo_GOV/GOV09/ALTA/Bus9/' +Event+'.plt', n_var, 2, multi=1, label='G ', pos=0)
        self.plotEvent('Estudo_GOV/GOV09/MEDIO/Bus9/'+Event+'.plt', n_var, 1, multi=1, label='G ', pos=0)
        self.plotEvent('Estudo_GOV/GOV09/LEVE/Bus9/' +Event+'.plt', n_var, 0, multi=1, label='G ', pos=0)

        title = ['Patamar de Carga Leve - GOV09', 'Patamar de Carga Media - GOV09', 'Patamar de Carga Alta - GOV09']

        for idx, ax in enumerate(self.axs[0]):
            ax.set_ylabel('Δ Pm [MW]')
            ax.set_xlabel('Time [s]')
            ax.set_title(title[idx])
            ax.grid()
            ax.legend()


        self.plotEvent('Estudo_GOV/GOV17/ALTA/Bus9/' +Event+'.plt', n_var, 2, multi=1, label='G ', pos=1)
        self.plotEvent('Estudo_GOV/GOV17/MEDIO/Bus9/'+Event+'.plt', n_var, 1, multi=1, label='G ', pos=1)
        self.plotEvent('Estudo_GOV/GOV17/LEVE/Bus9/' +Event+'.plt', n_var, 0, multi=1, label='G ', pos=1)

        title = ['Patamar de Carga Leve - GOV17', 'Patamar de Carga Media - GOV17', 'Patamar de Carga Alta - GOV17']

        for idx, ax in enumerate(self.axs[1]):
            ax.set_ylabel('Δ Pm [MW]')
            ax.set_xlabel('Time [s]')
            ax.set_title(title[idx])
            ax.grid()
            ax.legend()


    def mixGeneratorComparation(self, n_gen, n_var, Event):

        color1 = ['#8c000f', '#008000', '#0000ff']
        color2 = ['#dc143c', '#15b01a', '#0343df']

        self.fig, self.axs = plt.subplots(nrows=1, ncols=n_gen, sharex=True, figsize=(15, 8))        

        self.plotMix('Estudo_GOV/GOV09/ALTA/Bus9/' +Event+'.plt', n_var, 2, multi=100, label='09-G ', color=color1, linestyle='-')
        self.plotMix('Estudo_GOV/GOV09/MEDIO/Bus9/'+Event+'.plt', n_var, 1, multi=100, label='09-G ', color=color1, linestyle='-')
        self.plotMix('Estudo_GOV/GOV09/LEVE/Bus9/' +Event+'.plt', n_var, 0, multi=100, label='09-G ', color=color1, linestyle='-')

        self.plotMix('Estudo_GOV/GOV17/ALTA/Bus9/' +Event+'.plt', n_var, 2, multi=100, label='17-G ', color=color2, linestyle='--')
        self.plotMix('Estudo_GOV/GOV17/MEDIO/Bus9/'+Event+'.plt', n_var, 1, multi=100, label='17-G ', color=color2, linestyle='--')
        self.plotMix('Estudo_GOV/GOV17/LEVE/Bus9/' +Event+'.plt', n_var, 0, multi=100, label='17-G ', color=color2, linestyle='--')

        title = ['Patamar de Carga Leve - GOV09', 'Patamar de Carga Media - GOV09', 'Patamar de Carga Alta - GOV09']

        for idx, ax in enumerate(self.axs):
            ax.set_ylabel('Pe [MW]')
            ax.set_xlabel('Time [s]')
            ax.set_title(title[idx])
            ax.grid()
            ax.legend()

        # plt.show()

    def plotMix(self, path, n_var, n_event, multi=1, label=None, color=None, linestyle=None):

        organon = PLT_Reader(path)

        for idx, ind in enumerate(n_var):

            self.axs[n_event].plot(organon.var_dic['Tempo - segundos'],
                                   organon.var_dic[organon.lines[ind].rstrip()]*multi,
                                                                            
                                   label=label+organon.lines[ind].rstrip().split('#')[0][-1],
                                   color=color[idx],
                                   linestyle=linestyle)
            




            
    def save(self, path):

        plt.savefig(path, bbox_inches='tight')
        




# n_var  = [49, 50, 51]
# GOV    = 'GOV17'
# events = ['Evento_' + str(i) for i in range(1, 14)]

# EPC = EventPlotComparation()
# EPC.mixGeneratorComparation(3, n_var, events[0])

# for event in events:
#     EPC.mixGeneratorComparation(3, n_var, event)
#     EPC.save('Plots/Event/Pm/GOV17/'+event+'.png')

n_var  = [49, 50, 51] #[2, 3, 4] #[70, 71, 72, 73, 74, 75]
events = ['Evento_' + str(i) for i in range(1, 14)]

EPC = EventPlotComparation()
for event in events:
    EPC.eventGeneratorComparation(3, n_var, event)
    # EPC.mixGeneratorComparation(3, n_var, event)
    EPC.save('Plots/Delta/Comparation/Pm/'+event+'.png')







