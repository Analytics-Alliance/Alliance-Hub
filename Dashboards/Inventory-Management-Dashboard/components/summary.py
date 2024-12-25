import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

def create_summary_cards(dashboard_data):
    inventory_status = dashboard_data['inventory_status']
    sales_metrics = dashboard_data['sales_metrics']
    pending_orders = dashboard_data['pending_orders']

    # Calculate summary metrics
    total_inventory_value = inventory_status['TotalValue'].sum()
    low_stock_items = len(inventory_status[inventory_status['OnHandQty'] <= inventory_status['ReorderPoint']])
    total_sales = sales_metrics['TotalRevenue'].sum()
    pending_deliveries = len(pending_orders)

    return dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Inventory Value"),
                    html.H2(f"${total_inventory_value:,.2f}")
                ])
            ], className="text-center")
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Low Stock Items"),
                    html.H2(f"{low_stock_items}")
                ])
            ], className="text-center bg-warning text-white")
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Sales"),
                    html.H2(f"${total_sales:,.2f}")
                ])
            ], className="text-center bg-success text-white")
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Pending Deliveries"),
                    html.H2(f"{pending_deliveries}")
                ])
            ], className="text-center bg-info text-white")
        ], width=3),
    ], className="mb-4")

def create_stock_alerts(inventory_status):
    # Filter for items that need reordering
    alerts = inventory_status[inventory_status['OnHandQty'] <= inventory_status['ReorderPoint']]
    
    if len(alerts) == 0:
        return html.Div()  # Return empty div if no alerts
        
    alert_items = [
        f"{row['ProductName']} (SKU: {row['SKU']}) - Current Stock: {row['OnHandQty']}, Reorder Point: {row['ReorderPoint']}"
        for _, row in alerts.iterrows()
    ]

    return dbc.Alert(
        [
            html.H4("Stock Alerts", className="alert-heading"),
            html.Hr(),
            html.P("The following items need attention:"),
            html.Ul([html.Li(item) for item in alert_items])
        ],
        color="warning",
        className="mb-4"
    )