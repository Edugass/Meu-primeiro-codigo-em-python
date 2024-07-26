import json


try:
    with open("frutas.json", "r") as comida:
       frutas=json.load(comida)
except FileNotFoundError:
    frutas= []

while True:
   resposta=input("Qual é o nome da fruta?")
   quantidade=input("Quantas frutas são?")

   dados = {
      "Nome" : resposta,
      "quantidade" : quantidade
   }
    
   frutas.append(dados)

   continuar = input("Deseja adicionar uma fruta nova? (s/n)")
   if continuar.lower () != "s":
      break
   
   print("Obrigado por cadastrar essas frutas")

with open ("frutas.json", "w") as comida:
      json.dump(frutas, comida, indent=4)


