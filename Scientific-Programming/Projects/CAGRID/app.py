import numpy as np
from dash import Dash, dcc, html, Input, Output, callback_context
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Constants
GRID_WIDTH = 80
GRID_HEIGHT = 60

# Initialize the grid with random states
grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.8, 0.2])  # 80% dead, 20% alive

def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            live_neighbors = np.sum(grid[max(0, x-1):min(x+2, grid.shape[0]), max(0, y-1):min(y+2, grid.shape[1])]) - grid[x, y]
            if grid[x, y] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0  # Dies
                else:
                    new_grid[x, y] = 1  # Lives
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[x, y] = 1  # Becomes alive
    return new_grid

def create_grid_figure(grid):
    """Create a grid figure for Dash."""
    return {
        'data': [{
            'z': grid,
            'type': 'heatmap',
            'colorscale': [[0, 'black'], [1, 'white']],
            'showscale': False
        }],
        'layout': {
            'xaxis': {'showgrid': False, 'zeroline': False, 'showticklabels': False},
            'yaxis': {'showgrid': False, 'zeroline': False, 'showticklabels': False},
            'height': 600,
            'width': 800,
            'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0},
            'paper_bgcolor': 'black'
        }
    }

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1("Cellular Automata Dashboard"), width={"size": 6, "offset": 3}),
    ]),
    dcc.Graph(id='grid', figure=create_grid_figure(grid)),
    dbc.Row([
        dbc.Col(dbc.Button("Next Generation", id='next-gen', color='primary'), width={"size": 2, "offset": 5}),
        dbc.Col(dbc.Button("Reset", id='reset', color='secondary'), width={"size": 2}),
    ]),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0, disabled=True),  # For animation
])

@app.callback(
    Output('grid', 'figure'),
    Input('next-gen', 'n_clicks'),
    Input('reset', 'n_clicks'),
    Input('interval-component', 'n_intervals')
)
def update_output(next_clicks, reset_clicks, n_intervals):
    global grid
    ctx = dash.callback_context

    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_id == 'next-gen':
        grid = update_grid(grid)
    elif triggered_id == 'reset':
        grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.8, 0.2])  # Reset grid

    return create_grid_figure(grid)

if __name__ == "__main__":
    app.run_server(debug=True)