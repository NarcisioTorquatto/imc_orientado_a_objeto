
class Pessoa:
    def __init__(self,nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura


    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def faixa_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau I"
        elif 35 <= imc < 39.9:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"

def main():

    nome = input("Qual o seu nome?: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    

    pessoa = Pessoa(nome, peso, altura)
    

    imc = pessoa.calcular_imc()
    print(f"Seu IMC é: {imc:.2f}")
    

    print(f"Faixa de peso: {pessoa.faixa_imc()}")


if __name__ == "__main__":
    main()
