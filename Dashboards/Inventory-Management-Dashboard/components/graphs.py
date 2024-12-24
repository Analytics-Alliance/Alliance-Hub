import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc

def create_stock_bar_chart(df):
    fig = px.bar(
        df, 
        x='name', 
        y='stock', 
        title='Stock per Product',
        color="name",
        template="plotly_white",
        height=500  # Fixed height for better consistency
    )
    
    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20),
        title_x=0.5,
        title_font_size=16,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='rgba(0,0,0,0.1)'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.05)',
            showline=True,
            linecolor='rgba(0,0,0,0.1)'
        )
    )
    
    return dbc.Card(
        [
            dbc.CardHeader("Stock Levels"),
            dbc.CardBody(
                dcc.Graph(
                    id='stock-graph',
                    figure=fig,
                    config={
                        'displayModeBar': False,
                        'scrollZoom': False
                    }
                )
            )
        ],
        className="h-100"
    )