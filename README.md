# aviator-project

> 🇧🇷 [Português](#português) · 🇺🇸 [English](#english)

## Português

### O que você encontrará neste repositório?

Um estudo de dados sobre o **Aviator**, o "crash game" da Spribe em que um multiplicador sobe até "explodir" aleatoriamente.
Feito em **janeiro de 2023**, o projeto tem três partes:

1. **Coleta:** um robô com Selenium abre o jogo no modo demonstração (sem login) e registra cada multiplicador (payout)
   em `data/payouts.txt`. No meio do caminho, uma descoberta curiosa: sites diferentes exibiam as mesmas odds.
2. **Tratamento e geração:** um notebook ajusta uma distribuição de Pareto aos ~5 mil resultados reais e gera dados
   sintéticos, exportando tudo em CSV e Excel.
3. **Simulação:** funções que testam uma estratégia de aposta fixa com saída em uma odd alvo sobre o histórico.

> ⚠️ Projeto de estudo, com fins educacionais. Não é recomendação de aposta: jogos de azar envolvem risco real de perda.

### Ferramentas

- Python 3.11
- Selenium + webdriver-manager (automação do navegador, no padrão *Page Object*)
- pytest (usado para executar o coletor)
- pandas, SciPy e openpyxl (tratamento, distribuição de Pareto e exportação)
- Jupyter Notebook

### Estrutura

```
├── main.py              # leitura/tratamento dos dados e simulação de apostas
├── main.ipynb           # ajuste de Pareto, geração de dados e exportação
├── pages/               # Page Objects (base e páginas de cada cassino)
├── resources/           # seletores (locators) dos elementos do jogo
├── tests/test_web.py    # coletor de payouts com Selenium
└── data/                # payouts coletados (.txt) e exportações (.csv/.xlsx)
```

Sobre `data/`: `payouts.*` são os 5.040 resultados reais; `payouts10k.*` e `payouts50k.*` incluem dados sintéticos.

### Como usar

**1. Clone e instale as dependências**

```bash
git clone https://github.com/tofolo17/aviator-project.git
cd aviator-project
python -m venv .venv
# Windows: .venv\Scripts\activate | Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

**2. Simule uma estratégia** (não depende de internet, usa os dados já coletados)

```python
from main import read_data, treat_data, bet_MC

odds = treat_data(read_data('data/payouts.txt'))
resultado = bet_MC(odds, ini_amount=100, stop_odd=2, cash_in=1)
print(resultado['Valor final'], resultado['Vitórias'], resultado['Derrotas'])
```

**3. Gere e exporte os dados** abrindo o notebook:

```bash
jupyter notebook main.ipynb
```

**4. Colete novos payouts** (requer o Google Chrome instalado):

```bash
pytest tests/test_web.py::test_lv
```

O coletor roda em loop até ser interrompido com `Ctrl+C`, adicionando cada novo resultado a `data/payouts.txt`.

> Os sites e seletores são de janeiro de 2023 e podem ter mudado. Se a coleta falhar, atualize a URL em
> `pages/game_pages.py` e os seletores em `resources/locators.py`.

### Licença

[MIT](LICENSE)

---

## English

### What will you find in this repository?

A data study on **Aviator**, Spribe's crash game, where a multiplier climbs until it randomly "crashes".
Built in **January 2023**, the project has three parts:

1. **Collection:** a Selenium bot opens the game in demo mode (no login) and records every multiplier (payout) in
   `data/payouts.txt`. Along the way, a curious finding: different sites showed the same odds.
2. **Processing and generation:** a notebook fits a Pareto distribution to the ~5k real results and generates
   synthetic data, exporting everything to CSV and Excel.
3. **Simulation:** functions that backtest a fixed-stake strategy with a target cash-out odd over the history.

> ⚠️ Study project, for educational purposes. Not betting advice: gambling carries a real risk of loss.

### Tools

- Python 3.11
- Selenium + webdriver-manager (browser automation, *Page Object* pattern)
- pytest (used to run the collector)
- pandas, SciPy and openpyxl (processing, Pareto distribution and export)
- Jupyter Notebook

### Structure

```
├── main.py              # data reading/processing and bet simulation
├── main.ipynb           # Pareto fit, data generation and export
├── pages/               # Page Objects (base and per-casino pages)
├── resources/           # selectors (locators) for the game's elements
├── tests/test_web.py    # Selenium payout collector
└── data/                # collected payouts (.txt) and exports (.csv/.xlsx)
```

About `data/`: `payouts.*` hold the 5,040 real results; `payouts10k.*` and `payouts50k.*` include synthetic data.

### How to use

**1. Clone and install the dependencies**

```bash
git clone https://github.com/tofolo17/aviator-project.git
cd aviator-project
python -m venv .venv
# Windows: .venv\Scripts\activate | Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

**2. Simulate a strategy** (works offline, using the data already collected)

```python
from main import read_data, treat_data, bet_MC

odds = treat_data(read_data('data/payouts.txt'))
result = bet_MC(odds, ini_amount=100, stop_odd=2, cash_in=1)
print(result['Valor final'], result['Vitórias'], result['Derrotas'])
```

**3. Generate and export the data** by opening the notebook:

```bash
jupyter notebook main.ipynb
```

**4. Collect new payouts** (requires Google Chrome):

```bash
pytest tests/test_web.py::test_lv
```

The collector loops until stopped with `Ctrl+C`, appending each new result to `data/payouts.txt`.

> Sites and selectors date from January 2023 and may have changed. If collection fails, update the URL in
> `pages/game_pages.py` and the selectors in `resources/locators.py`.

### License

[MIT](LICENSE)
