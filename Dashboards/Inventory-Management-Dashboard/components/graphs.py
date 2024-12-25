import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

def create_stock_bar_chart(inventory_status):
    fig = go.Figure([
        go.Bar(
            name='Current Stock',
            x=inventory_status['ProductName'],
            y=inventory_status['OnHandQty'],
            marker_color='#36A2EB'
        ),
        go.Bar(
            name='Reorder Point',
            x=inventory_status['ProductName'],
            y=inventory_status['ReorderPoint'],
            marker_color='#FF6384'
        )
    ])
    
    fig.update_layout(
        title='Current Stock vs Reorder Points',
        barmode='group',
        height=400,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    return dbc.Card([
        dbc.CardHeader([
            html.H4("Stock Levels", className="mb-0")
        ]),
        dbc.CardBody([
            dcc.Graph(figure=fig, config={'displayModeBar': False})
        ])
    ])

def create_sales_trend(sales_metrics):
    # Create a bar chart for total revenue by product
    fig = px.bar(
        sales_metrics,
        x='SKU',
        y='TotalRevenue',
        title='Revenue by Product',
        labels={'TotalRevenue': 'Total Revenue ($)', 'SKU': 'Product SKU'},
        color='TotalQuantitySold',
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        height=400,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    return dbc.Card([
        dbc.CardHeader([
            html.H4("Sales Analysis", className="mb-0")
        ]),
        dbc.CardBody([
            dcc.Graph(figure=fig, config={'displayModeBar': False})
        ])
    ])