import dash_bootstrap_components as dbc
from dash import html
from components.data_table import create_inventory_table
from components.graphs import create_stock_bar_chart, create_sales_trend
from components.summary import create_summary_cards, create_stock_alerts
from components.pending_orders import create_pending_orders_card

def create_layout(dashboard_data):
    return html.Div(
        className="dashboard-container",
        children=[
            html.H1("Inventory Management Dashboard", className="text-center mb-4"),
            
            # Summary Cards
            create_summary_cards(dashboard_data),
            
            # Alerts Section
            create_stock_alerts(dashboard_data['inventory_status']),
            
            # Main Content
            dbc.Row([
                # Inventory Table
                dbc.Col([
                    create_inventory_table(dashboard_data['inventory_status'])
                ], lg=8, className="mb-4"),
                
                # Pending Orders
                dbc.Col([
                    create_pending_orders_card(dashboard_data['pending_orders'])
                ], lg=4, className="mb-4"),
            ], className="g-4"),
            
            # Charts Row
            dbc.Row([
                # Stock Levels
                dbc.Col([
                    create_stock_bar_chart(dashboard_data['inventory_status'])
                ], lg=6, className="mb-4"),
                
                # Sales Trend
                dbc.Col([
                    create_sales_trend(dashboard_data['sales_metrics'])
                ], lg=6, className="mb-4"),
            ], className="g-4"),
        ]
    )