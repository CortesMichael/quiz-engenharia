perguntas = [
    {
        "pergunta": "Na definição clássica de Tom Mitchell para Aprendizado de Máquina, o processo de aprendizado de um algoritmo é estruturado a partir de quais elementos?",
        "alternativas": [
            "Dados, Filtros e Algoritmos.",
            "Tarefa (T), Experiência (E) e Medida de Desempenho (P).",
            "Entrada (X), Camada Oculta (H) e Saída (Y).",
            "Programação, Execução e Validação."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Se eu preciso treinar um modelo para prever um valor numérico exato e contínuo, como o preço de venda de uma máquina ou a temperatura de um sistema, qual tipo de problema estou resolvendo?",
        "alternativas": [
            "Classificação.",
            "Agrupamento (Clustering).",
            "Regressão.",
            "Redução de Dimensionalidade."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "Qual tipo de aprendizado de máquina é caracterizado por utilizar bases de dados que não possuem rótulos, etiquetas ou respostas históricas conhecidas?",
        "alternativas": [
            "Aprendizado Supervisionado.",
            "Aprendizado Não Supervisionado.",
            "Aprendizado por Reforço.",
            "Programação Baseada em Regras."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Como é chamado o problema que ocorre quando um modelo de Inteligência Artificial decora os dados de treinamento tão perfeitamente que perde a capacidade de acertar em dados novos do mundo real?",
        "alternativas": [
            "Underfitting.",
            "Overfitting.",
            "Oversampling.",
            "Oclusão."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Em uma Rede Neural Artificial, qual é a função principal das chamadas Camadas Ocultas (Hidden Layers)?",
        "alternativas": [
            "Receber os dados brutos de entrada do sistema sem fazer nenhuma alteração.",
            "Mostrar diretamente o resultado final da predição para o usuário.",
            "Extrair características, bordas, formas e padrões complexos dos dados em níveis de abstração progressivos.",
            "Guardar uma cópia de segurança dos dados de treino."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "Qual métrica de avaliação é a mais indicada para medir o sucesso de um modelo de Classificação binária, como identificar se uma peça é aprovada ou reprovada?",
        "alternativas": [
            "Erro Quadrático Médio (MSE).",
            "Coeficiente de Determinação (R2).",
            "Acurácia.",
            "Variância Residual."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "Em projetos práticos de desenvolvimento de sistemas inteligentes, estima-se que o engenheiro gaste cerca de 80% do tempo total do projeto em qual dessas etapas?",
        "alternativas": [
            "Escolha do modelo de Deep Learning mais moderno do mercado.",
            "Coleta, organização, limpeza e tratamento dos dados brutos.",
            "Criação de apresentações e gráficos de desempenho.",
            "Upgrade de hardware e compra de processadores mais rápidos."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Qual é a principal finalidade de separarmos a nossa base de dados original em conjuntos distintos de Treino e de Teste?",
        "alternativas": [
            "Forçar o modelo a usar todos os dados possíveis para memorizar as respostas.",
            "Avaliar como o modelo se comporta diante de dados inéditos para medir sua capacidade real de generalização.",
            "Reduzir o tempo que o computador leva para processar os cálculos matemáticos.",
            "Separar as colunas que possuem textos daquelas que possuem números."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "O que representa o conceito de Peso nas conexões sinápticas entre os neurônios artificiais de uma rede?",
        "alternativas": [
            "O espaço em disco que o arquivo final do modelo ocupa no computador.",
            "A força ou intensidade daquela conexão, ditando o quanto o sinal de um neurônio vai influenciar o próximo.",
            "O número total de rodadas ou épocas que o algoritmo precisa para terminar o treino.",
            "O número exato de neurônios que foram alocados na camada de entrada do sistema."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Sistemas que envolvem reconhecimento de voz, tradução de idiomas em tempo real e assistentes virtuais baseados em texto pertencem a qual grande área de aplicação da IA?",
        "alternativas": [
            "Visão Computacional.",
            "Processamento de Linguagem Natural (PLN).",
            "Otimização por Algoritmos Genéticos.",
            "Redes Autônomas de Infraestrutura."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Imagine que estou trabalhando com um banco de dados onde existem 10.000 amostras de funcionamento normal de um equipamento e apenas 20 amostras de falhas graves. Se eu decidir duplicar de forma aleatória as amostras de falhas para equilibrar os dados, qual técnica apliquei?",
        "alternativas": [
            "Undersampling.",
            "Regularização de Pesos.",
            "Oversampling.",
            "Validação Cruzada."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "Apesar de carregar a palavra Regressão em seu nome técnico por questões matemáticas, o algoritmo de Regressão Logística é amplamente utilizado no mercado para resolver problemas de:",
        "alternativas": [
            "Regressão Linear Múltipla.",
            "Classificação (saídas discretas ou categorias).",
            "Agrupamento Não Supervisionado.",
            "Previsão de Séries Temporais Contínuas."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Na Visão Computacional aplicada à robótica, quando uma câmera tenta identificar um objeto na linha de produção, mas outro elemento da cena passa na frente e bloqueia parte da visão desse objeto, a IA enfrenta o desafio clássico de:",
        "alternativas": [
            "Iluminação Variável.",
            "Mudança de Escala.",
            "Oclusão.",
            "Distorção de Perspectiva."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "O algoritmo KNN realiza suas predições baseando-se na proximidade geométrica dos dados vizinhos. Se eu configurar esse modelo com um parâmetro K muito pequeno, igual a 1 (K=1), o que acontecerá com o comportamento do sistema?",
        "alternativas": [
            "O modelo se tornará extremamente robusto contra ruídos e outliers.",
            "O modelo sofrerá de Underfitting devido à suavização excessiva das fronteiras de decisão.",
            "O modelo ficará excessivamente sensível a ruídos nos dados de treino, aumentando muito a chance de Overfitting.",
            "O algoritmo não conseguirá calcular as distâncias devido à falta de dados comparativos."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "O classificador probabilístico Naive-Bayes recebe o adjetivo de Ingênuo por fazer qual suposição simplificadora sobre a estrutura dos dados?",
        "alternativas": [
            "Ele assume que o modelo nunca vai errar independentemente dos dados de entrada.",
            "Ele assume que todas as variáveis de entrada são completamente independentes entre si para prever o resultado.",
            "Ele assume que dados textuais não possuem semântica e os trata apenas como números binários simples.",
            "Ele assume que a ordem das palavras em uma frase nunca altera o sentido do texto."
        ],
        "resposta": 1  # b
    },
    {
        "pergunta": "Após rodar um modelo de regressão para prever o consumo de combustível de uma frota, o resultado apontou um Coeficiente de Determinação R2 = 0.92. Como interpretar esse indicador?",
        "alternativas": [
            "O modelo apresenta um erro médio de 92 unidades da variável medida.",
            "O modelo é considerado ruim porque foi capaz de explicar apenas 8% dos dados.",
            "O modelo obteve um bom ajuste, conseguindo explicar 92% da variabilidade da variável de saída com base nas variáveis de entrada.",
            "O modelo está sofrendo de Underfitting crítico por ter ficado muito próximo do valor unitário."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "No processo de construção de uma Árvore de Decisão, o algoritmo precisa quebrar os nós repetidamente buscando criar grupos cada vez mais homogêneos. Quais são as duas métricas matemáticas mais utilizadas para calcular o nível de impureza ou desordem desses nós?",
        "alternativas": [
            "Erro Quadrático Médio (MSE) e R-Quadrado (R2).",
            "Distância Euclidiana e Distância de Manhattan.",
            "Impureza de Gini e Entropia.",
            "Funções de Ativação Sigmoide e ReLu."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "Uma rede neural profunda apresentou um Erro Quadrático Médio (MSE) igual a zero durante a fase de treinamento, mas quando foi testada com dados novos, o erro foi muito alto. Qual técnica matemática adiciona uma penalidade diretamente na função de perda para encolher o valor dos pesos e forçar a rede a ficar mais simples?",
        "alternativas": [
            "Regularização (como as técnicas L1 ou L2).",
            "Gradiente Descendente Estocástico.",
            "Amostragem por Bootstrap.",
            "Funções de Ativação Linear por Partes."
        ],
        "resposta": 0  # a
    },
    {
        "pergunta": "No campo de Processamento de Linguagem Natural (PLN), qual é o principal fator de complexidade que diferencia as Linguagens Naturais (como o português) das Linguagens Formais (como o Python)?",
        "alternativas": [
            "As linguagens formais alteram sua sintaxe dependendo da região geográfica de quem está programando.",
            "As linguagens naturais seguem regras matemáticas perfeitas que eliminam qualquer margem para duplo sentido.",
            "As linguagens naturais são inerentemente ambíguas, dependendo fortemente do contexto, entonação, gírias e ironia, enquanto as formais são estritas e unívocas.",
            "As linguagens formais não utilizam o concept de tokens durante seu processamento lógico no computador."
        ],
        "resposta": 2  # c
    },
    {
        "pergunta": "Se um algoritmo de machine learning apresenta um comportamento com alto viés (High Bias) and baixa variância (Low Variance) tanto no conjunto de treinamento quanto no de testes, conclui-se que o modelo se encontra em estado de:",
        "alternativas": [
            "Overfitting (Sobreajuste aos dados).",
            "Underfitting (Subajuste) por não ter capacidade de capturar a complexidade real do problema.",
            "Ajuste Ideal (Modelo Balanceado).",
            "Vazamento de Dados (Data Leakage)."
        ],
        "resposta": 1  # b
    }
]