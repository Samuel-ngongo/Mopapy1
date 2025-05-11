import numpy as np

def estimar_proxima_rodada(dados):
    if len(dados) < 10:
        return 1.00, 1.50  # valores seguros para poucos dados
    ultimos = np.array(dados[-10:])
    media = np.mean(ultimos)
    minimo = max(1.00, np.percentile(ultimos, 10))
    return minimo, media

def avaliar_tendencia(dados):
    if len(dados) < 5:
        return "Tendência: Insuficiente para análise."
    subidas = sum(1 for i in range(-5, 0) if dados[i] > 2)
    quedas = sum(1 for i in range(-5, 0) if dados[i] <= 2)
    if subidas >= 3:
        return "Tendência de alta detectada. Prepare-se para possível queda em breve."
    elif quedas >= 3:
        return "Tendência de queda detectada. Pode haver subida em breve."
    else:
        return "Tendência estável nas últimas rodadas."

def analisar_dados(dados):
    alertas = []
    ultimos = dados[-10:] if len(dados) >= 10 else dados

    # Alerta para sequência de altos
    altos = [v for v in ultimos if v >= 2.60]
    if len(altos) >= 3:
        alertas.append("Muitos valores altos recentes. Possível queda em breve.")

    # Alerta para sequência de baixos críticos
    baixos = [v for v in ultimos if v <= 1.20]
    if len(baixos) >= 3:
        alertas.append("Sequência de baixos críticos detectada. Possível subida em breve.")

    # Alerta se últimos 3 forem todos acima de 3.00
    if all(v > 3.0 for v in ultimos[-3:]):
        alertas.append("Três rodadas muito altas seguidas. Alta probabilidade de queda!")

    # Alerta se padrão instável
    if np.std(ultimos) > 1.5:
        alertas.append("Alta instabilidade detectada nas últimas rodadas. Cautela!")

    return alertas