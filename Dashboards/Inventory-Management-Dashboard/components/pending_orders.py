import dash_bootstrap_components as dbc
from dash import html, dash_table
import pandas as pd

def create_pending_orders_card(pending_orders):
    # Merge with suppliers to get supplier names
    pending_orders = pd.merge(
        pending_orders,
        pd.read_csv("data/suppliers.csv"),
        on='SupplierID',
        how='left'
    )
    
    # Format the table data
    table_data = pending_orders[[
        'PONumber', 
        'SKU', 
        'Quantity', 
        'ExpectedDeliveryDate',
        'SupplierName'
    ]].to_dict('records')

    return dbc.Card([
        dbc.CardHeader([
            html.H4("Pending Orders", className="mb-0")
        ]),
        dbc.CardBody([
            dash_table.DataTable(
                data=table_data,
                columns=[
                    {'name': 'PO Number', 'id': 'PONumber'},
                    {'name': 'SKU', 'id': 'SKU'},
                    {'name': 'Qty', 'id': 'Quantity'},
                    {'name': 'Expected Delivery', 'id': 'ExpectedDeliveryDate'},
                    {'name': 'Supplier', 'id': 'SupplierName'}
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
                }
            )
        ])
    ])
