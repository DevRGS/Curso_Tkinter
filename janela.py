from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de clientes") #Define titulo da janela
        self.root.configure(background = '#87CEFA') #define cor de fundo da janela
        self.root.geometry("700x500") #Define tamanho da janela
        self.root.resizable(True, True) #Define que tanto as dimensões de X e Y serão responsivas.
        self.root.maxsize(width=900, height=700) #Define o tamanho máximo da janela, embora seja responsiva, terá este limite máximo
        self.root.minsize(width=675, height=450) #Define o tamanho mínimo da janela, embora seja responsiva, terá este limite mínimo
        
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        
        self.frame_1.place(relx = 0.02,
                           rely = 0.02,
                           relwidth = 0.96,
                           relheight = 0.46)
        #O método place é usado exclusivamente para posicionar o widget.
        
        self.frame_1.configure(
                                bd=4, #é o border
                                bg='#708090', #é a cor de fundo do frame
                                highlightbackground='#000000', # é a cor da borda
                                highlightthickness=2) #Espessura da borda
        #Propriedades como bd, bg, highlightbackground, e highlightthickness devem ser configuradas separadamente ou diretamente no momento da criação do Frame.
        
        
        self.frame_2 = Frame(self.root)
        
        self.frame_2.place(relx = 0.02,
                           rely = 0.5,
                           relwidth = 0.96,
                           relheight = 0.46)
        #O método place é usado exclusivamente para posicionar o widget.
        
        self.frame_2.configure(
                                bd=4, #é o border
                                bg='#708090', #é a cor de fundo do frame
                                highlightbackground='#000000', # é a cor da borda
                                highlightthickness=2) #Espessura da borda
        #Propriedades como bd, bg, highlightbackground, e highlightthickness devem ser configuradas separadamente ou diretamente no momento da criação do Frame.
        
    def widgets_frame1(self):
        #criando botão de Limpar
        self.btn_limpar = Button(self.frame_1, text='Limpar')
        self.btn_limpar.configure(
                                   bd=3, 
                                   bg='#1E90FF',
                                   fg='white',
                                   font =('verdana', 8, 'bold'))
        
        self.btn_limpar.place(relx = 0.2,
                              rely = 0.1,
                              relwidth=0.1,
                              relheight= 0.15)
        
        
        #criando botão de Buscar    
        self.btn_buscar = Button(self.frame_1, text='Buscar')
        self.btn_buscar.configure(
                                   bd=3, 
                                   bg='#1E90FF',
                                   fg='white',
                                   font =('verdana', 8, 'bold'))
        
        self.btn_buscar.place(relx = 0.3,
                              rely = 0.1,
                              relwidth=0.1,
                              relheight= 0.15)
        
        
        #criando botão de Novo    
        self.btn_novo = Button(self.frame_1, text='Novo')
        self.btn_novo.configure(
                                   bd=3, 
                                   bg='#1E90FF',
                                   fg='white',
                                   font =('verdana', 8, 'bold'))
        
        self.btn_novo.place(relx = 0.6,
                              rely = 0.1,
                              relwidth=0.1,
                              relheight= 0.15)
        
        
        #criando botão de Alterar    
        self.btn_alterar = Button(self.frame_1, text='Alterar')
        self.btn_alterar.configure(
                                   bd=3, 
                                   bg='#1E90FF',
                                   fg='white',
                                   font =('verdana', 8, 'bold'))
        
        self.btn_alterar.place(relx = 0.7,
                              rely = 0.1,
                              relwidth=0.1,
                              relheight= 0.15)
        
        
        #criando botão de Apagar    
        self.btn_apagar = Button(self.frame_1, text='Apagar')
        self.btn_apagar.configure(
                                   bd=3, 
                                   bg='#1E90FF',
                                   fg='white',
                                   font =('verdana', 8, 'bold'))
        self.btn_apagar.place(relx = 0.8,
                              rely = 0.1,
                              relwidth=0.1,
                              relheight= 0.15) 
        
        #Criando label e entrada de código
        self.lb_codigo = Label(self.frame_1, text='Còdigo')
        self.lb_codigo.place(relx=0.05,
                             rely=0.045)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05,
                                rely=0.15,
                                relwidth=0.07)
        
        
        #Criando label e entrada de Nome
        self.lb_nome = Label(self.frame_1, text='Nome')
        self.lb_nome.place(relx=0.05,
                             rely=0.35)
        
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05,
                                rely=0.45,
                                relwidth=0.85)
        
        
        #Criando label e entrada de Telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone')
        self.lb_telefone.place(relx=0.05,
                             rely=0.6)
        
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05,
                                rely=0.7,
                                relwidth=0.4)
        
        
        #Criando label e entrada de Cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade')
        self.lb_cidade.place(relx=0.5,
                             rely=0.6)
        
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5,
                                rely=0.7,
                                relwidth=0.4)
app = Application()