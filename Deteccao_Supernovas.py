import plotly.graph_objects as go
import numpy as np

def curva_de_luz():
    # Gera uma curva de luz aleatória com base em uma distribuição normal
    tempo = np.linspace(0, 10, 100)
    luminosidade_base = np.random.normal(loc=1.0, scale=0.2, size=len(tempo))

    # Adiciona uma supernova em um ponto aleatório
    supernova_index = np.random.randint(20, 80)
    luminosidade_supernova = np.random.normal(loc=2.0, scale=0.5, size=len(tempo) - supernova_index)
    luminosidade = np.concatenate((luminosidade_base[:supernova_index], luminosidade_base[supernova_index:] + luminosidade_supernova))

    return tempo, luminosidade

def detectar_supernova(tempo, luminosidade):
    threshold = 1.5
    for i in range(len(tempo)):
        if luminosidade[i] > threshold:
            return True, tempo[i]

    return False, None

def main():
    # Gera a curva de luz
    tempo, luminosidade = curva_de_luz()

    # Detecta a supernova na curva de luz
    supernova_detectada, tempo_supernova = detectar_supernova(tempo, luminosidade)

    # Criando a curva de luz
    trace_curva_luz = go.Scatter(x=tempo, y=luminosidade, mode='lines', name='Curva de luz', line=dict(color='blue', width=2))

    # Adicionando a supernova detectada
    trace_supernova = go.Scatter(x=[tempo_supernova], y=[2.5], mode='markers', name='Supernova detectada',
                                marker=dict(color='red', size=10, symbol='star'))

    # Configurações do layout
    layout = go.Layout(title='Detecção de Supernova', xaxis=dict(title='Tempo'), yaxis=dict(title='Luminosidade'))

    # Criando a figura
    fig = go.Figure(data=[trace_curva_luz, trace_supernova], layout=layout)

    if supernova_detectada:
        # Adicionando anotação se a supernova for detectada
        fig.add_annotation(
            x=tempo_supernova,
            y=2.5,
            text="Supernova detectada!",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="red",
            font=dict(size=12, color="black"),
            bgcolor="white",
            opacity=0.7
        )

    # Atualizando o layout para mostrar a legenda
    fig.update_layout(showlegend=True)

    # Exibindo a figura
    fig.show()

if __name__ == "__main__":
    main()
