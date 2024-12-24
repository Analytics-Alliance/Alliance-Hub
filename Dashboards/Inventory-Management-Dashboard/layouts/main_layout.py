import dash_bootstrap_components as dbc
from dash import html
from components.data_table import create_data_table
from components.graphs import create_stock_bar_chart

def create_layout(df):
    return html.Div(
        className="dashboard-container",
        children=[
            html.H1(
                "Inventory Management Dashboard",
                className="text-center mb-4"
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                create_data_table(df),
                                className="h-100"
                            )
                        ],
                        lg=6,
                        className="mb-4"
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                create_stock_bar_chart(df),
                                className="h-100"
                            )
                        ],
                        lg=6,
                        className="mb-4"
                    ),
                ],
                className="g-4"
            )
        ]
    )