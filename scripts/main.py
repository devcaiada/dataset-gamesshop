import pandas as pd
import streamlit as st

st.set_page_config(page_title="Análise de Vendas Meganium", layout="wide")
st.title("📊 Análise de Vendas - Meganium")

# Upload do arquivo
file = st.file_uploader("📂 Envie o arquivo Excel com os dados consolidados", type=["xlsx"])

if file:
    xls = pd.ExcelFile(file)
    st.success(f"Abas carregadas: {xls.sheet_names}")

    df_list = []
    for sheet in xls.sheet_names:
        df_temp = xls.parse(sheet)
        df_temp["Origem"] = sheet
        df_list.append(df_temp)

    dados = pd.concat(df_list, ignore_index=True)

    dados.columns = dados.columns.str.strip()
    dados.columns = dados.columns.str.replace(" ", "_")
    dados.columns = dados.columns.str.title()

    st.subheader("🔍 Visualização Inicial dos Dados")
    st.dataframe(dados.head())

    st.markdown("### 📌 Colunas disponíveis no DataFrame:")
    st.write(dados.columns.tolist())

    colunas_esperadas = [
        "Total_Price", "Quantity", "Product_Sold",
        "Delivery_Country", "Date_Sold"
    ]

    if all(col in dados.columns for col in colunas_esperadas):

        dados["Date_Sold"] = pd.to_datetime(dados["Date_Sold"], errors="coerce")

        st.markdown("## 📈 Indicadores Gerais")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Vendas", f"R$ {dados['Total_Price'].sum():,.2f}")
        col2.metric("Total de Itens Vendidos", f"{dados['Quantity'].sum():,.0f}")
        col3.metric("Ticket Médio", f"R$ {dados['Total_Price'].sum() / dados['Quantity'].sum():.2f}")

        st.markdown("## 🌍 Produtos Mais Vendidos por País")
        top_produtos = (
            dados.groupby(['Delivery_Country', 'Product_Sold'])['Quantity']
            .sum()
            .reset_index()
            .sort_values(['Delivery_Country', 'Quantity'], ascending=[True, False])
        )

        for pais in top_produtos['Delivery_Country'].unique():
            st.write(f"**{pais}**")
            top = top_produtos[top_produtos['Delivery_Country'] == pais].head(5)
            st.dataframe(top, use_container_width=True)

        st.markdown("## 🚛 Logística e Transporte")
        st.info("⚠️ Coluna com data de entrega não encontrada. Caso exista, envie a versão da base com essa informação para análise de logística.")
    else:
        st.error("❌ As colunas necessárias não foram encontradas. Verifique se os nomes estão corretos.")
