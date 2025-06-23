import pandas as pd
import matplotlib.pyplot as plt

# Arquivo csv
file_path = 'results.csv'

try:
    # Ler o CSV
    df = pd.read_csv(file_path)

    # Verificar se está lendo certo
    print("Columns in the DataFrame:")
    print(df.columns)
    print("\nFirst 5 rows of the DataFrame:")
    print(df.head())

    # Criar o tempo com a coluna date
    df['time'] = pd.to_datetime(df['date'])

    #Pegar as colunas que serão utilizadas no gráfico
    tensao = df['Grid-0.0-Bus R17-vm_pu']
    pot_ativa = df['PV-0.PV_0-P_gen']
    controle = df['PV-0.PV_0-mod']

    #Plotar sobre todas juntas
    plt.figure(figsize=(12, 10))

    # Tensão
    plt.subplot(3, 1, 1)
    plt.plot(df['time'], tensao, label='Tensão (pu)', color='blue')
    plt.ylabel('Tensão (pu)')
    plt.title('Controller Performance Analysis')
    plt.grid(True)
    plt.legend()

    # Potência ativa
    plt.subplot(3, 1, 2)
    plt.plot(df['time'], pot_ativa, label='P_out (pu)', color='green')
    plt.ylabel('P_out (pu)')
    plt.grid(True)
    plt.legend()

    # Atuação do controlador
    plt.subplot(3, 1, 3)
    plt.plot(df['time'], controle, label='Controle (mod)', color='red')
    plt.ylabel('Controle (mod)')
    plt.xlabel('Tempo')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

    
   # plt.figure(figsize=(8, 6))
   # plt.scatter(tensao, pot_ativa, color='purple', alpha=0.6)
   # plt.xlabel('Tensão (pu)')
   # plt.ylabel('Potência ativa (pu)')
   # plt.title('Curva Volt-Watt observada')
   # plt.grid(True)
   # plt.show()

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure it is in the same directory as the script.")
except KeyError as e:
    print(f"Error: A required column was not found. Please check column names. Missing: {e}")
    print("Available columns are:", df.columns.tolist())
except Exception as e:
    print(f"An unexpected error occurred: {e}")