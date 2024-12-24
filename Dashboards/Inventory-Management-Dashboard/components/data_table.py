from dash import dash_table
import dash_bootstrap_components as dbc

def create_data_table(df):
    # Calculate value column
    data = [{
        **row,
        'value': round(row['stock'] * row['price'], 2)
    } for row in df.to_dict('records')]
    
    return dbc.Card(
        [
            dbc.CardHeader("Inventory Data"),
            dbc.CardBody(
                dash_table.DataTable(
                    id='inventory-table',
                    columns=[
                        {"name": "Product", "id": "name"},
                        {"name": "Stock", "id": "stock", "type": "numeric"},
                        {"name": "Price ($)", "id": "price", "type": "numeric"},
                        {"name": "Value ($)", "id": "value", "type": "numeric"}
                    ],
                    data=data,
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
                    style_data_conditional=[
                        {
                            'if': {'filter_query': '{stock} <= 20'},
                            'backgroundColor': '#FFF3CD',
                            'color': '#856404'
                        }
                    ],
                    tooltip_data=[
                        {
                            column: {'value': f'Click to edit {column}', 'type': 'markdown'}
                            for column in ['stock', 'price']
                        } for row in data
                    ],
                    editable=True,
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