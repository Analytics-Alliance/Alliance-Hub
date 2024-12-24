from dash import dash_table
import dash_bootstrap_components as dbc

def create_data_table(df):
    return dbc.Card(
        [
            dbc.CardHeader("Inventory Data"),
            dbc.CardBody(
                dash_table.DataTable(
                    id='inventory-table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    style_table={
                        'overflowX': 'auto',
                        'height': '500px',
                        'overflowY': 'auto'
                    },
                    style_cell={
                        'textAlign': 'left',
                        'padding': '1rem',
                        'fontFamily': 'Inter, sans-serif',
                        'fontSize': '0.9rem'
                    },
                    style_header={
                        'backgroundColor': 'rgba(0, 0, 0, 0.02)',
                        'fontWeight': '600',
                        'border': 'none',
                        'borderBottom': '1px solid rgba(0, 0, 0, 0.05)'
                    },
                    style_data={
                        'border': 'none',
                        'borderBottom': '1px solid rgba(0, 0, 0, 0.05)'
                    },
                    page_size=10,
                    row_selectable="multi",
                    selected_rows=[],
                    sort_action="native",
                    filter_action="native"
                )
            )
        ],
        className="h-100"
    )