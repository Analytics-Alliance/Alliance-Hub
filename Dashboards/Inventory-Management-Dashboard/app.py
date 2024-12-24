import dash
from dash import Dash
import pandas as pd
from layouts.main_layout import create_layout
from utils.data_processing import process_data
from callbacks.callbacks import register_callbacks
import dash_bootstrap_components as dbc

# Initialize the Dash app with external stylesheets
app = Dash(
    __name__,
    external_stylesheets=[
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap',
        dbc.themes.BOOTSTRAP
    ],
    suppress_callback_exceptions=True
)

# Load and process data
df = pd.read_csv("data/inventory_data.csv")
processed_df = process_data(df)

# Create the app layout
app.layout = create_layout(processed_df)

# Register callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)