import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
#### AS TRES LINHAS ACIMA IMPORTAM AS BIBLIOTECAS QUE SERÃO UTILIZADO NO CODIGO ###




Grafico=plt.figure()



def Recepcao_dos_dados():
### Lendo os dados informados pelo TXT ###
    Dados=open("Dados.txt").read() 
    linhas = Dados.split('\n') 
    for i in linhas: 
        if "Vf" in i: 
            Vφ = eval(i[3:]) 
        if "Ra" in i: 
            Ra = eval(i[3:])
        if "Sn" in i: 
            S_nominal = eval(i[3:]) 
        if "Xs" in i: 
            Xs = eval(i[3:]) 
        if "fr" in i: 
            f = eval(i[3:]) 
        if "po" in i: 
            p = eval(i[3:])     
        if "fec" in i: 
            fechamento = eval(i[4:]) 
        if "fp" in i: 
            fp = eval(i[3:])  
        if "re" in i: 
            re = eval(i[3:]) 
        if "pn" in i: 
            P_nucleo = eval(i[3:]) 
        if "pm" in i: 
            P_mec = eval(i[3:])
        if "Sc" in i: 
            S_carga= eval(i[3:])  
        if "fg" in i: 
            fp_gerador= eval(i[3:]) 
        if "lim" in i: 
            lim_pot= eval(i[4:])
### Lendo os dados informados pelo TXT ###

### verificando fechamento###    
    if fechamento=='y':
        Vl=Vφ*np.sqrt(3)
        Vl=abs(Vl)
    else:
        Vl=Vφ
        Vl=abs(Vl)
### verificando fechamento###    


### Calculando os parametros do gerador COM DADOS NOMIINAIS###    
    Ia_n=S_nominal/(np.sqrt(3)*Vl)
    theta=np.arccos(fp_gerador)
    Ia_real=Ia_n*np.cos(theta)
    Ia_imag=Ia_n*np.sin(theta)
    Ia_n=Ia_real+Ia_imag*(-1j)
    jXsIa_n=(Xs*Ia_n)*1j 
    RaIa_n=Ra*Ia_n
    Ea_n=Vφ+jXsIa_n+RaIa_n
### Calculando os parametros do gerador COM DADOS NOMIINAIS###    


### Calculando os parametros da carga###

    Ia=S_carga/(np.sqrt(3)*Vl)
    theta=np.arccos(fp)
    Ia_real=Ia*np.cos(theta)
    Ia_imag=Ia*np.sin(theta)
    if re == 'a':
        Ia=Ia_real+Ia_imag*(-1j)
    else:
        Ia=Ia_real+Ia_imag*(1j)
     
    wm=(120*f)/p

    RaIa=Ra*Ia 

    jXsIa=(Xs*Ia)*1j 

    Vetor_1=[Vφ,RaIa+Vφ] 

    Vetor_2=[Vφ+RaIa,RaIa+Vφ+jXsIa] 

    Ea=RaIa+Vφ+jXsIa

    Vetor_3=[0,Ea]  
    ### Calculando os parametros ###
       
    return Vetor_1,Vetor_2,Vetor_3,Vφ,Xs,S_nominal,fp,P_nucleo,P_mec,S_carga,Ea,Ea_n,RaIa,jXsIa,Ia,wm,lim_pot

def Plotagem(i): 
    ###Chamando funções que retornam os dados da plotagem(parametros da maquina)###
    Vetor_1,Vetor_2,Vetor_3,Vφ,Xs,S_nominal,fp,P_nucleo,P_mec,S_carga,Ea,Ea_n,RaIa,jXsIa,Ia,wm,lim_pot = Recepcao_dos_dados()

    Vetor_torque,δ,Torque_de_op,Amax,Tmax=Torque_de_Operação(Vφ,Ea,Ea_n,wm,Xs)

    i_f_x,v_t_y,op_if,op_Vt=CAV(Ea)

    x_rotor,y_rotor,x_estator,y_estator,Pmax,P_carga,Q_carga,Q=Curva_de_Capacidade(Vφ,Xs,S_nominal,P_nucleo,P_mec,S_carga,fp,Ea_n,lim_pot)
    ###Chamando funções que retornam os dados da plotagem(parametros da maquina)###

    Grafico.clear()
    ### Plotagem e anotações das somas vetorias de Ea,Vφ,Ea,RaIa,jXsIa####
    plt.subplot(3,2,1)
    plt.title('Diagrama Fasorial')
    plt.xlabel('Tensão(V)') 
    plt.ylabel('Tensão(V)')
    plt.axhline(0, color='black',linewidth=2) 
    plt.axvline(0, color='black',linewidth=2) 
    plt.plot([0, Vφ.real],[0, Vφ.imag], color='r') 
    plt.plot([0, Ia.real],[0, Ia.imag], color='g') 
    plt.plot([Vetor_1[0].real, Vetor_1[1].real],[Vetor_1[0].imag, Vetor_1[1].imag], color='y') 
    plt.plot([Vetor_2[0].real, Vetor_2[1].real],[Vetor_2[0].imag, Vetor_2[1].imag], color='purple')
    plt.plot([Vetor_3[0].real, Vetor_3[1].real],[Vetor_3[0].imag, Vetor_3[1].imag], color='brown')  
    plt.annotate("", xy=(Vφ.real, Vφ.imag), xytext=(0,0),arrowprops=dict(arrowstyle="->", color='r'))     
    plt.annotate("", xy=(Ia.real, Ia.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color='g')) 
    plt.annotate("", xy=(Vetor_1[1].real, Vetor_1[1].imag), xytext=(Vetor_1[0].real, Vetor_1[0].imag), arrowprops=dict(arrowstyle="->", color='y')) 
    plt.annotate("", xy=(Vetor_2[1].real, Vetor_2[1].imag), xytext=(Vetor_2[0].real, Vetor_2[0].imag), arrowprops=dict(arrowstyle="->", color='purple')) 
    plt.annotate("", xy=(Vetor_3[1].real, Vetor_3[1].imag), xytext=(Vetor_3[0].real, Vetor_3[0].imag), arrowprops=dict(arrowstyle="->", color='gray'))
    plt.annotate(f"Vφ={Vφ:.2f} V", xy=(Vφ.real-(0.15*Vφ.real),Vφ.imag+(0.01*Vφ.imag)))      
    plt.annotate(f"Ia={Ia:.2f} A", xy=(Ia.real+(0.15*Ia.real),Ia.imag))     
    plt.annotate(f"RaIa={RaIa:.2f} W", xy=(Vetor_1[1].real+(0.01*Vetor_1[1].real),Vetor_1[1].imag))    
    plt.annotate(f"jXsIa={jXsIa:.2f} Var", xy=(Vetor_2[1].real,Vetor_2[1].imag-(0.1*Vetor_2[1].imag)))   
    plt.annotate(f"Ea={Ea:.2f} V", xy=(Vetor_3[1].real-(0.1*Vetor_3[1].real),Vetor_3[1].imag)) 
    plt.grid()
    plt.tight_layout()
    ### Plotagem e anotações das somas vetorias de Ea,Vφ,Ea,RaIa,jXsIa####

    ###Plotagem da curva de torque em função do angulo entre EA e Vφ e do ponto de operação####
    plt.subplot(3,2,3)
    plt.title('Curva de Torque')
    plt.xlabel('Angulo δ(°)') 
    plt.ylabel('Torque τ(N.m)')
    plt.axhline(0, color='black',linewidth=2) 
    plt.axvline(0, color='black',linewidth=2) 
    plt.plot(Vetor_torque, color='black')
    plt.plot(δ,Torque_de_op,'ro')
    plt.plot(Amax,Tmax,'bo')
    plt.annotate(f"δ={δ:.2f}°\nτ={Torque_de_op:.2f}N.m ", xy=(δ+(0.015*δ), Torque_de_op-(0.26*Torque_de_op))) 
    plt.annotate(f"δ={Amax:.2f}°\nτ={Tmax:.2f}N.m ", xy=(Amax+(0.01*Amax), Tmax-(0.2*Tmax))) 
    plt.grid()
    plt.tight_layout()
    ###Plotagem da curva de torque em função do angulo entre EA e Vφ e do ponto de operação####

    ###Plotagem CAV E PONTO DE CORRENTE E TENSÃO NA CAV####
    plt.subplot(3,2,5)
    plt.title('CAV')
    plt.xlabel('Corrente do estator(A)') 
    plt.ylabel('Tensão Terminal(V)')
    plt.axhline(0, color='black',linewidth=2) 
    plt.axvline(0, color='black',linewidth=2) 
    plt.plot(i_f_x,v_t_y, color='black')
    plt.plot(op_if,op_Vt,'ro')
    plt.annotate(f"If={op_if:.2f}A\nVt={op_Vt:.2f}V", xy=(op_if+(0.01*op_if), op_Vt-(0.25*op_Vt))) 
    plt.grid()
    plt.tight_layout()
    ###Plotagem CAV E PONTO DE CORRENTE E TENSÃO NA CAV####

    ###curva de capacidade####
    plt.subplot(1,2,2)
    plt.title('Curva de Capacidade')
    plt.xlabel('Q (Var)') 
    plt.ylabel('P (w)')
    plt.axhline(0, color='black',linewidth=2) 
    plt.axvline(0, color='black',linewidth=2)
    plt.axvline(Pmax, color='red',linewidth=1,label='Limite de potência da máquina motriz')
    plt.plot(x_rotor,y_rotor, color='r', ls='--',label='Limite de Corrente do Rotor')
    plt.plot(x_estator,y_estator, color='black',label='Limite de Corrente do Estator ')
    plt.plot(P_carga,Q_carga,'ro')
    plt.plot(0,Q,'bo')
    plt.annotate(f"P={P_carga:.2f}W\nQ={Q_carga:.2f}Var", xy=(P_carga+(0.01*P_carga), Q_carga-(0.25*Q_carga)))
    plt.annotate(f"Q={Q:.2f}Var", xy=((0),(Q)))
    plt.grid()
    plt.legend()
    plt.tight_layout()
    ###curva de capacidade####


def Torque_de_Operação(Vφ,Ea,Ea_n,wm,Xs):
    ####Criando vetor com os angulos em graus e Vetor que irá receber os valores de torque para determinado angulo###
    Angs=np.arange(0,181,1)
    Vetor_torque=[]
    ####Criando vetor com os angulos em graus e Vetor que irá receber os valores de torque para determinado angulo###

    ### Calculando angulo entre EA e Vφ e definindo torque de operação da maquina###
    δ=(np.arctan(Ea.imag/Ea.real)*180)/np.pi-np.arctan(Vφ.imag/Vφ.real)
    Torque_de_op=(3*abs(Vφ)*abs(Ea)*np.sin((δ*np.pi)/180))/(wm*Xs)
    ### Calculando angulo entre EA e Vφ e definindo torque de operação da maquina###

    ### Calculando curva de torque para os angulos definidos###

    for i in Angs:
        Vetor_torque.append((3*abs(Vφ)*abs(Ea_n)*np.sin((i*np.pi)/180))/(wm*Xs))
    v0=0
    for i,v in enumerate(Vetor_torque):
        if v>v0:
            Tmax=v
            Amax=i
    ### Calculando curva de torque para os angulos definidos###
        v0=v
    return Vetor_torque,δ,Torque_de_op,Amax,Tmax

def CAV(Vl):
    ###PONTOS DA CAV FIGURA P4-1 Chapman5ED####
    i_F=[829.318,922.9465,1093.1095,1193.213,1289.302,1401.19,1541.05,1704.22,1886.815]
    v_t_LINHA=[127305.50,139999.68,161350.63,172153.41,181301.22,190230.79,200051.50,209326.62,218419.87]
    ###PONTOS DA CAV FIGURA P4-1 Chapman5ED####
    ###DEFININDO COEFICIENTES DA FUNÇÃO DE INTERPOLAÇÃO####
    coef_interpolação=np.polyfit(i_F,v_t_LINHA,4)
    ###DEFININDO COEFICIENTES DA FUNÇÃO DE INTERPOLAÇÃO####
    ###DEFININDO A FUNÇÃO DE INTERPOLAÇÃO####
    função_gerada=np.poly1d(coef_interpolação)
    ###DEFININDO A FUNÇÃO DE INTERPOLAÇÃO####
    ###VETOR COM OS VALORES DO EIXO X####
    i_F_final=np.linspace(0,max(i_F),100)
    ###VETOR COM OS VALORES DO EIXO Y####
    v_t_LINHA_final=função_gerada(i_F_final)
    ###VETOR COM OS VALORES DO EIXO Y####
    ###DEFININDO PONTO DE OPERAÇÃO NA CAV####
    v0=abs(Vl)
    for i,v in enumerate(v_t_LINHA_final):
          if v>=v0:
            Op_iF=i_F_final[i]
            Op_Vt=v0
            break  
    ###DEFININDO PONTO DE OPERAÇÃO NA CAV####
    return i_F_final,v_t_LINHA_final,Op_iF,Op_Vt

def Curva_de_Capacidade(Vφ,Xs,S_nominal,p_nucleo,p_mec,S_carga,fp,Ea_n,lim_pot):
    theta=np.arccos(fp)

    P_carga=S_carga*fp
    Q_carga=S_carga*np.sin(theta)

    Pmax = lim_pot-p_nucleo-p_mec

    De=(3*abs(Ea_n)*abs(Vφ))/Xs
    Q=(-3*abs(Vφ)**2)/Xs

    Limite_Rotor = np.linspace(2.1,1, 100)
    Limite_estator = np.linspace(3,-1, 100)

    x_rotor= De * np.cos(Limite_Rotor)
    y_rotor= Q+(De * np.sin(Limite_Rotor))
    x_estator= S_nominal* np.cos(Limite_estator)
    y_estator= S_nominal * np.sin(Limite_estator)

    return x_rotor,y_rotor,x_estator,y_estator,Pmax,P_carga,Q_carga,Q

a=animation.FuncAnimation(Grafico,Plotagem,interval=100,cache_frame_data=False) ### animando a figura  ou grafico definido no inicio do codigo de 1 em 1 s 
plt.show() ### mostrando o grafico


