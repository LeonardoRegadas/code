class Funcionario: 
      
     def _init_(self, id, nome, senha): 
         self.id = id 
         self.nome = nome 
         self.senha = senha 
  
     def _str_(self): 
         return f'{self.id}{self.senha}' 
  
 class Gerente(Funcionario): 
      
     def _init_(self, id, nome, senha): 
         super()._init_(id, nome, senha) 
  
 class Vendedor(Funcionario): 
  
     def _init_(self, id, nome, senha): 
         super()._init_(id, nome, senha) 
  
 class Autenticacao: 
  
     def _init_(self,dados): 
         self.dados = dados 
         self.autentica = False 
      
     @property 
     def realizar_login(self): 
         user = int(input("Digite seu Id: ")) 
         senha = input("Digite sua senha: ") 
  
         log = str(f'{user}{senha}') 
         for logn in self.dados: 
             if log == str(logn): 
                 print("Voce Entrou") 
                 self.autentica = True 
                 break 
         if self.autentica == False: 
             print("Senha Incorreta") 
          
  
 gerent1 = Gerente(1, "Claudio", "10") 
 vende1 = Vendedor(2, "Claudio", "20") 
  
 dados = [gerent1, vende1] 
  
 entrar = Autenticacao(dados) 
  
 entrar.realizar_login