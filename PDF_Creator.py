from fpdf import FPDF
import os

class ReportCreator():

    def __init__(self, path=None):

        self.pdf         = FPDF('L', 'mm', 'A4')
        self.title       = 'Comparação entre GOV09 e GOV17'
        self.event_title = ['Step Up de carga: 10 MW e 10 Mvar',
                            'Step Up de carga: 20 MW e 20 Mvar',
                            'Step Up de carga: 30 MW e 30 Mvar',
                            'Step Up de carga: 40 MW e 40 Mvar',
                            'Step Up de carga: 50 MW e 50 Mvar',
                            'Step Up de carga: 75 MW e 75 Mvar',
                            'Step Up de carga: 80 MW e 80 Mvar',
                            'Step Up de carga: 100 MW e 100 Mvar',
                            'Step Up de carga: 120 MW e 120 Mvar',
                            'Step Up de carga: 150 MW e 150 Mvar',
                            'Step Up de carga: 200 MW e 200 Mvar',
                            'Perda do Gerador 1',
                            'Perda do Gerador 2']

        self.generateReport()

        



        

    def generateReport(self):

        # Title

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=36)
        self.pdf.cell(0, 150, self.title, align='C')

        '''

        # ===================================================================== GOV09

        # Potência Elétrica - GOV09

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Eventos - GOV09 - Potência Elétrica', align='C')
        self.evtPlot('Plots/Event/Pe/GOV09/')

        # Potência Mecânica - GOV09

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Eventos - GOV09 - Potência Mecânica', align='C')
        self.evtPlot('Plots/Event/Pm/GOV09/')

        # ===================================================================== GOV17

        # Potência Elétrica - GOV17

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Eventos - GOV17 - Potência Elétrica', align='C')
        self.evtPlot('Plots/Event/Pe/GOV17/')

        # Potência Mecânica - GOV17

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Eventos - GOV17 - Potência Mecânica', align='C')
        self.evtPlot('Plots/Event/Pm/GOV17/')

        # ===================================================================== COMPARAÇÃO

        # Potência Elétrica

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Comparação - Potência Elétrica', align='C')
        self.evtPlot('Plots/Comparation/Pe/')

        # Potência Mecânica

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Comparação - Potência Mecânica', align='C')
        self.evtPlot('Plots/Comparation/Pm/')

        # Frequência

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Comparação - Frequência', align='C')
        self.evtPlot('Plots/Comparation/Freq/')

        # ===================================================================== MIX

        # Potência Elétrica

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Comparação Sobreposta - Potência Elétrica', align='C')
        self.evtPlot('Plots/Mix/Pe/')

        # Potência Mecânica

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Comparação Sobreposta - Potência Mecânica', align='C')
        self.evtPlot('Plots/Mix/Pm/')

        '''

        # ===================================================================== COMPARAÇÃO

        # Potência Elétrica

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Variação de Potência Elétrica', align='C')
        self.evtPlot('Plots/Delta/Comparation/Pe/')

        # Potência Mecânica

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=30)
        self.pdf.cell(0, 150, 'Variação de Potência Mecânica', align='C')
        self.evtPlot('Plots/Delta/Comparation/Pm/')


        

        



        self.save('DeltaReport.pdf')


    def evtPlot(self, path):       

        files = ['Evento_' + str(i) + '.png' for i in range(1, 14)]

        for idx, plot in enumerate(files):

            self.page_title(self.event_title[idx]) 
            self.pdf.image(path+plot, x=10, y=40, w=270)





    def params(self, font='times', tipo='', size=16):
        self.pdf.set_font(font, tipo, size)

    def save(self, name):
        self.pdf.output(name, 'F')

    def page_title(self, name):

        self.pdf.add_page()
        # self.header()
        self.params(tipo='B', size=22)
        self.pdf.cell(0, 50, name, align='C')


if __name__ == '__main__':

    RC = ReportCreator()