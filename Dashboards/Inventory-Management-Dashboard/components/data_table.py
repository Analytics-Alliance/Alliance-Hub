import dash_bootstrap_components as dbc
from dash import dash_table, html
import pandas as pd

def create_inventory_table(inventory_status):
    # Merge with products to get product names and other details
    table_data = inventory_status[[
        'SKU',
        'ProductName',
        'Category',
        'OnHandQty',
        'SafetyStock',
        'ReorderPoint',
        'RetailPrice',
        'TotalValue'
    ]].to_dict('records')

    return dbc.Card([
        dbc.CardHeader([
            html.H4("Inventory Status", className="mb-0")
        ]),
        dbc.CardBody([
            dash_table.DataTable(
                id='inventory-table',
                data=table_data,
                columns=[
                    {'name': 'SKU', 'id': 'SKU'},
                    {'name': 'Product', 'id': 'ProductName'},
                    {'name': 'Category', 'id': 'Category'},
                    {'name': 'On Hand', 'id': 'OnHandQty'},
                    {'name': 'Safety Stock', 'id': 'SafetyStock'},
                    {'name': 'Reorder Point', 'id': 'ReorderPoint'},
                    {'name': 'Price', 'id': 'RetailPrice', 'type': 'numeric', 'format': {'specifier': '$.2f'}},
                    {'name': 'Total Value', 'id': 'TotalValue', 'type': 'numeric', 'format': {'specifier': '$.2f'}}
                ],
                style_table={'overflowX': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'padding': '10px',
                    'minWidth': '100px'
                },
                style_header={
                    'backgroundColor': '#f8f9fa',
                    'fontWeight': 'bold'
                },
                style_data_conditional=[
                    {
                        'if': {
                            'filter_query': '{OnHandQty} <= {ReorderPoint}'
                        },
                        'backgroundColor': '#fff3cd',
                        'color': '#856404'
                    }
                ],
                sort_action='native',
                filter_action='native',
                page_size=10
            )
        ])
    ])