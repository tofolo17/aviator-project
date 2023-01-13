"""Funções de leitura de dados e simulação de apostas no Aviator."""


# Funções de dados
def read_data(path):
    """Lê o arquivo de payouts e devolve uma lista de linhas (ex.: '2.54x')."""
    with open(path, 'r') as f:
        data = [line.rstrip() for line in f]

    return data


def treat_data(data):
    """Remove o sufixo 'x' de cada payout e converte para float."""
    return [float(d[:-1]) for d in data]


def clean_data(data, limit):
    """Descarta odds iguais ou acima de `limit` (outliers); 0 desativa."""
    if limit > 0:
        return [d for d in data if d < limit]
    return data


# Funções de aposta
def bet(odd, stop_od):
    """Indica se a odd da rodada atingiu a odd de parada."""
    if odd < stop_od:
        return False
    return True


def bet_MC(data, ini_amount, stop_odd, cash_in):
    """Simula apostas sequenciais de valor fixo sobre o histórico de odds.

    Retorna um dicionário com o saldo final, extremos, histórico do saldo
    e estatísticas das odds.
    """
    amounts = []  # saldo após cada rodada
    v, der = 0, 0  # contadores de vitórias e derrotas
    amount = ini_amount

    for d in data:
        # Vitória se o avião alcança a odd de parada (lucro de
        # cash_in * (stop_odd - 1)); caso contrário, perde a aposta.
        if bet(d, stop_odd):
            amount += cash_in * (stop_odd - 1)
            v += 1
        else:
            amount -= cash_in
            der += 1
        amounts += [amount]

    simulation_data = {
        "Valor inicial": ini_amount,
        "Valor final": amount,
        "Valor mais alto": max(amounts),
        "Valor mais baixo": min(amounts),
        "Registros": amounts,
        "Vitórias": v,
        "Derrotas": der,
        "Maior odd": max(data),
        "Menor odd": min(data),
        "Média odd": sum(data) / len(data)
    }
    return simulation_data
