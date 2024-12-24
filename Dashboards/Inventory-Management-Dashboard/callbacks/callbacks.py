from dash.dependencies import Input, Output, State
from dash import callback
import plotly.express as px
import pandas as pd

def register_callbacks(app):
    @callback(
        [Output("stock-graph", "figure"),
         Output("summary-cards", "children"),
         Output("stock-alerts", "children")],
        [Input("inventory-table", "data"),
         Input("inventory-table", "selected_rows")]
    )
    def update_dashboard(data, selected_rows):
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Filter for selected rows if any
        if selected_rows:
            dff = df.iloc[selected_rows]
        else:
            dff = df
            
        # Update graph
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
            title_font_size=16,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                showgrid=False,
                showline=True,
                linecolor='rgba(0,0,0,0.1)'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.05)',
                showline=True,
                linecolor='rgba(0,0,0,0.1)'
            )
        )
        
        # Update summary cards
        from components.summary import create_summary_cards, create_stock_alerts
        summary_cards = create_summary_cards(df)
        stock_alerts = create_stock_alerts(df)
        
        return fig, summary_cards, stock_alerts
