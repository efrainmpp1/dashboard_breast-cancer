import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Breast cancer diagnosis",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a Bug': 'https://www.example.com/bug',
        'About': '# This is a demo app designed to showcase a dashboard presenting an analysis of breast cancer diagnosis data. The app provides visualizations and insights derived from the dataset, allowing users to gain a better understanding of the patterns and relationships within the data. It offers various visual representations, including correlation heatmaps, density heatmaps, scatter matrices, density contours, histograms, and boxplots. By exploring these visualizations, users can obtain valuable insights into the features and characteristics associated with breast cancer diagnosis.'
    }
)
st.write('# Breast cancer diagnosis - Dashboard')
st.markdown('This is an interactive dashboard that features visualizations of breast cancer diagnostic data.')

df = pd.read_csv('./dataset/breast-cancer.csv')
st.write(df.head())

df.drop('id', axis=1, inplace=True)
data_nulls = df.isnull().sum().sum()

# Matriz de correlação
correlation_matrix = df.corr()

# Criação do heatmap
fig = px.imshow(correlation_matrix,
                labels=dict(x="Features", y="Features", color="Correlation"),
                x=correlation_matrix.columns,
                y=correlation_matrix.columns,
                color_continuous_scale='Viridis')

# Exibição do heatmap
st.write('### Correlation Heatmap')
st.plotly_chart(fig)

# Criação do heatmap de densidade
fig = px.density_heatmap(df, x="radius_mean", y="texture_mean", marginal_x="rug", marginal_y="histogram")

# Exibição do heatmap
st.write('### Density Heatmap')
st.plotly_chart(fig)

# Criação da matriz de dispersão
fig = px.scatter_matrix(df, dimensions=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'symmetry_mean', 'fractal_dimension_mean'], color="diagnosis", color_discrete_sequence=["red", "blue"])

# Exibição da matriz de dispersão
st.write('### Dispersion Matrix')
st.plotly_chart(fig)

# Criação do gráfico de contorno de densidade
fig = px.density_contour(df, x='radius_mean', y='texture_mean', color="diagnosis", marginal_x="rug", marginal_y="histogram", color_discrete_sequence=["red", "blue"])

# Exibição do gráfico de contorno de densidade
st.write('### Density Contour')
st.plotly_chart(fig)

# Criação do histograma
fig = px.histogram(df, x='radius_mean', y='texture_mean', color="diagnosis", marginal="rug", hover_data=df.columns, color_discrete_sequence=["red", "blue"])

# Exibição do histograma
st.write('### Histogram')
st.plotly_chart(fig)

# Criação do gráfico de boxplot
fig = px.box(df, x="diagnosis", y='radius_mean', color="diagnosis", notched=True, color_discrete_sequence=["red", "blue"])

# Exibição do gráfico de boxplot
st.write('### Boxplot')
st.plotly_chart(fig)

st.markdown('---')
st.write('Created by:')
st.write('Jaysa Barbosa and Efrain Pantaleon')