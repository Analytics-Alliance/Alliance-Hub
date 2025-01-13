import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# Generate the attractor points
dt = 0.01
num_steps = 10000
xs = np.empty(num_steps)
ys = np.empty(num_steps)
zs = np.empty(num_steps)

# Set initial values (modify these values to see the butterfly effect)
initial_conditions = (0., 1., 1.05)  # Change these values as needed
xs[0], ys[0], zs[0] = initial_conditions

# Calculate points
for i in range(num_steps - 1):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Create figure
fig = go.Figure(
    data=[go.Scatter3d(
        x=xs[0:1],
        y=ys[0:1],
        z=zs[0:1],
        mode='lines',
        line=dict(width=2, color='blue'),
    )],
    layout=go.Layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        title='Lorenz Attractor Formation',
        updatemenus=[dict(
            type='buttons',
            showactive=False,
            buttons=[dict(
                label='Play',
                method='animate',
                args=[None, dict(
                    frame=dict(duration=0, redraw=True),
                    fromcurrent=True,
                    mode='immediate',
                    transition=dict(duration=0)
                )]
            )]
        )]
    ),
    frames=[
        go.Frame(
            data=[go.Scatter3d(
                x=xs[:k],
                y=ys[:k],
                z=zs[:k],
                mode='lines',
                line=dict(width=2, color='blue')
            )],
            name=f'frame{k}'
        )
        # Create a frame every 50 steps to make the animation smoother
        for k in range(0, num_steps, 50)
    ]
)

# Update axis ranges to keep them fixed during animation
axis_range = dict(
    xaxis=dict(range=[min(xs), max(xs)]),
    yaxis=dict(range=[min(ys), max(ys)]),
    zaxis=dict(range=[min(zs), max(zs)])
)
fig.update_layout(scene=axis_range)

fig.show()