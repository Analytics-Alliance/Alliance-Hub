import dash_bootstrap_components as dbc
from dash import html

def create_summary_cards(df):
    return dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody([
                            html.H4("Total Products", className="card-title text-muted h6"),
                            html.H2(f"{len(df)}", className="text-primary mb-0")
                        ])
                    ],
                    className="text-center h-100"
                ),
                width=12,
                lg=4,
                className="mb-4"
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody([
                            html.H4("Total Stock", className="card-title text-muted h6"),
                            html.H2(f"{df['stock'].sum():.0f}", className="text-primary mb-0")
                        ])
                    ],
                    className="text-center h-100"
                ),
                width=12,
                lg=4,
                className="mb-4"
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardBody([
                            html.H4("Avg Price", className="card-title text-muted h6"),
                            html.H2(f"${df['price'].mean():.2f}", className="text-primary mb-0")
                        ])
                    ],
                    className="text-center h-100"
                ),
                width=12,
                lg=4,
                className="mb-4"
            )
        ],
        className="g-4",
        id="summary-cards"
    )

def create_stock_alerts(df, threshold=20):
    low_stock = df[df['stock'] <= threshold]
    if len(low_stock) > 0:
        return dbc.Alert(
            [
                html.H4("Low Stock Alert!", className="alert-heading h5"),
                html.P(f"The following items are running low: {', '.join(low_stock['name'])}", className="mb-0")
            ],
            color="warning",
            className="mb-4",
            id="stock-alerts"
        )
    return html.Div(id="stock-alerts")
