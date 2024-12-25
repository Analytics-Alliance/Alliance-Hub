import pandas as pd
from datetime import datetime

def load_and_process_data():
    """
    Load and process all data files, creating relationships between them.
    """
    # Load all CSV files
    inventory_levels = pd.read_csv("data/inventory_levels.csv")
    products = pd.read_csv("data/products.csv")
    purchase_orders = pd.read_csv("data/purchase_orders.csv")
    sales_orders = pd.read_csv("data/sales_orders.csv")
    suppliers = pd.read_csv("data/suppliers.csv")
    warehouses = pd.read_csv("data/warehouses.csv")

    # Calculate total inventory by SKU (combining warehouses)
    total_inventory = inventory_levels.groupby('SKU')['OnHandQty'].sum().reset_index()
    
    # Merge product information with inventory levels
    inventory_status = pd.merge(
        total_inventory,
        products,
        on='SKU',
        how='left'
    )

    # Calculate key metrics
    inventory_status['TotalValue'] = inventory_status['OnHandQty'] * inventory_status['RetailPrice']
    inventory_status['NeedsReorder'] = inventory_status['OnHandQty'] <= inventory_status['ReorderPoint']

    # Process sales data
    sales_orders['OrderDate'] = pd.to_datetime(sales_orders['OrderDate'])
    sales_by_product = sales_orders.groupby('SKU').agg({
        'Quantity': 'sum',
        'Price': lambda x: (x * sales_orders.loc[x.index, 'Quantity']).sum()
    }).reset_index()
    sales_by_product.columns = ['SKU', 'TotalQuantitySold', 'TotalRevenue']

    # Process purchase orders
    purchase_orders['PODate'] = pd.to_datetime(purchase_orders['PODate'])
    pending_orders = purchase_orders[purchase_orders['ActualDeliveryDate'].isna()]
    
    # Create final dashboard data
    dashboard_data = {
        'inventory_status': inventory_status,
        'sales_metrics': sales_by_product,
        'pending_orders': pending_orders,
        'suppliers': suppliers,
        'warehouses': warehouses
    }

    return dashboard_data