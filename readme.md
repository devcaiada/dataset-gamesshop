## 📊 Projeto de Análise de Vendas - Meganium

Este projeto foi desenvolvido para consolidar dados de vendas de múltiplas fontes (abas diferentes do Excel) e transformar essas informações em **insights relevantes para a fabricante**, como:

- Total de vendas por país
- Produtos mais vendidos
- Métricas gerais como ticket médio, total de itens e faturamento
- Apoio à logística e transporte

![upload]()

---

## 🧰 Tecnologias e Bibliotecas Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Excel (pandas.ExcelFile)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelFile.html)

---

## 📁 Estrutura da Base de Dados

O arquivo `Meganium_Sales_data.xlsx` contém múltiplas abas com o mesmo esquema de dados. As colunas esperadas são:

| Coluna             | Descrição                                         |
|--------------------|---------------------------------------------------|
| `Sku`              | Identificador do produto                          |
| `Product_Sold`     | Nome do produto vendido                           |
| `Date_Sold`        | Data da venda                                     |
| `Quantity`         | Quantidade de itens vendidos                      |
| `Unit_Price`       | Preço unitário do produto                         |
| `Total_Price`      | Preço total da venda (quantidade * unit price)    |
| `Currency`         | Moeda da transação                                |
| `Site`             | Canal ou site da venda                            |
| `Discount_Coupon`  | Código do cupom utilizado                         |
| `Discount_Value`   | Valor do desconto                                 |
| `Buyer_Birth_Date` | Data de nascimento do comprador                   |
| `Buyer_Name`       | Nome do comprador                                 |
| `Delivery_Country` | País de entrega                                   |
| `Invoice_Id`       | Número da nota fiscal                             |
| `Origem`           | Identificador da origem (nome da aba)             |

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/meganium-vendas.git
cd meganium-vendas
```

### 2. Crie um ambiente virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

**Arquivo `requirements.txt`**:
```txt
pandas
streamlit
openpyxl
```

### 4. Execute o Streamlit
```bash
streamlit run C:\Users\yourname\folder\dataset-gamesshop\scripts\main.py
```

![view]()

![kpis]()

---

## 📌 Funcionalidades do App

- **Upload do Arquivo Excel** com múltiplas abas.
- **Tratamento automático** de nomes de colunas.
- **Indicadores principais**:
  - Total de vendas
  - Total de itens vendidos
  - Ticket médio
- **Produtos mais vendidos por país**
- **Visualização por país e por produto**
- Informações de apoio para **logística** e **planejamento estratégico**.

## 📦 Melhorias Futuras
- Adicionar visualização de gráficos interativos

- Criar filtros por data e país

- Implementar sugestões de otimização logística

- Integração com Dashboards BI (Power BI ou Google Looker Studio)

## 🧑‍💻 Autor
Desenvolvido por [Caio Arruda](https://github.com/devcaiada)
📬 dev.caiada@gmail.com
