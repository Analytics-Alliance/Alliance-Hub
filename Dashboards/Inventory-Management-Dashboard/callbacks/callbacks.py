from dash.dependencies import Input, Output, State
from dash import callback
import plotly.express as px

def register_callbacks(app):
    @callback(
        Output("stock-graph", "figure"),
        [Input("inventory-table", "selected_rows"),
         Input("inventory-table", "data")]
    )
    def update_graph(selected_rows, data):
        if not selected_rows:
            # If no rows selected, show all data
            dff = data
        else:
            # Filter for selected rows
            dff = [data[i] for i in selected_rows]
            
        fig = px.bar(
            dff, 
            x='name', 
            y='stock',
            title='Stock per Product',
            color="name",
            template="plotly_white"
        )
        
        fig.update_layout(
            showlegend=False,
            margin=dict(l=20, r=20, t=40, b=20),
            title_x=0.5,
            title_font_size=16
        )
        
        return fig
