import dash
from dash import Dash
from layouts.main_layout import create_layout
from utils.data_processing import load_and_process_data  # Updated import
from callbacks.callbacks import register_callbacks
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = Dash(
    __name__,
    external_stylesheets=[
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap',
        dbc.themes.BOOTSTRAP
    ],
    suppress_callback_exceptions=True
)

# Load and process data
dashboard_data = load_and_process_data()

# Create the app layout
app.layout = create_layout(dashboard_data)

# Register callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)