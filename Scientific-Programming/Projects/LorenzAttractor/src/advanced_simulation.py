import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def generate_trajectory(initial_conditions, num_steps=10000, dt=0.01):
    xs = np.empty(num_steps)
    ys = np.empty(num_steps)
    zs = np.empty(num_steps)
    
    xs[0], ys[0], zs[0] = initial_conditions
    
    for i in range(num_steps - 1):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)
    
    return xs, ys, zs

app.layout = html.Div([
    html.H1("Lorenz Attractor - Butterfly Effect Visualization", 
            style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.H3("Initial Conditions - Trajectory 1 (Blue)"),
            html.Div([
                html.Label("X1: "),
                dcc.Input(id='x1', type='number', value=0.0, step=0.01),
                html.Label("Y1: "),
                dcc.Input(id='y1', type='number', value=1.0, step=0.01),
                html.Label("Z1: "),
                dcc.Input(id='z1', type='number', value=1.05, step=0.01),
            ], style={'padding': '10px'}),
        ], style={'flex': 1}),
        
        html.Div([
            html.H3("Initial Conditions - Trajectory 2 (Red)"),
            html.Div([
                html.Label("X2: "),
                dcc.Input(id='x2', type='number', value=0.001, step=0.01),
                html.Label("Y2: "),
                dcc.Input(id='y2', type='number', value=1.0, step=0.01),
                html.Label("Z2: "),
                dcc.Input(id='z2', type='number', value=1.05, step=0.01),
            ], style={'padding': '10px'}),
        ], style={'flex': 1}),
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),
    
    html.Button('Update Trajectories', id='update-button', n_clicks=0,
                style={'margin': '20px'}),
    
    dcc.Graph(id='lorenz-plot'),
    
    dcc.Slider(
        id='animation-slider',
        min=0,
        max=100,
        value=100,
        marks={i: f'{i}%' for i in range(0, 101, 10)},
        step=1,
    ),
])

@app.callback(
    Output('lorenz-plot', 'figure'),
    [Input('update-button', 'n_clicks'),
     Input('animation-slider', 'value')],
    [State('x1', 'value'),
     State('y1', 'value'),
     State('z1', 'value'),
     State('x2', 'value'),
     State('y2', 'value'),
     State('z2', 'value'),
     State('lorenz-plot', 'figure')]
)
def update_figure(n_clicks, slider_value, x1, y1, z1, x2, y2, z2, current_fig):
    # Generate both trajectories
    xs1, ys1, zs1 = generate_trajectory((x1, y1, z1))
    xs2, ys2, zs2 = generate_trajectory((x2, y2, z2))
    
    # Calculate points to show based on slider
    points = int((slider_value/100) * len(xs1))
    
    # Create figure with both trajectories
    fig = go.Figure()
    
    # Add first trajectory (blue)
    fig.add_trace(go.Scatter3d(
        x=xs1[:points],
        y=ys1[:points],
        z=zs1[:points],
        mode='lines',
        line=dict(width=2, color='blue'),
        name='Trajectory 1'
    ))
    
    # Add second trajectory (red)
    fig.add_trace(go.Scatter3d(
        x=xs2[:points],
        y=ys2[:points],
        z=zs2[:points],
        mode='lines',
        line=dict(width=2, color='red'),
        name='Trajectory 2'
    ))
    
    # Get the current camera position from the existing figure, or use default if none exists
    camera_settings = current_fig.get('layout', {}).get('scene', {}).get('camera', {}) if current_fig else dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.5, y=1.5, z=1.5)
    )
    
    # Update layout while preserving camera position
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            camera=camera_settings,  # Use preserved camera settings
            xaxis=dict(range=[min(min(xs1), min(xs2)), max(max(xs1), max(xs2))]),
            yaxis=dict(range=[min(min(ys1), min(ys2)), max(max(ys1), max(ys2))]),
            zaxis=dict(range=[min(min(zs1), min(zs2)), max(max(zs1), max(zs2))])
        ),
        title=f'Lorenz Attractor - Initial Condition Difference: ({x2-x1:.3f}, {y2-y1:.3f}, {z2-z1:.3f})',
        showlegend=True,
        uirevision='camera'  # Add this to preserve zoom level and camera position
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)