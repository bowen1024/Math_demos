import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

BACKGROUND_COLOR = '#1E1E1E'
GRID_COLOR = '#2E2E2E'
AXIS_COLOR = '#555555'
TEXT_COLOR = '#CCCCCC'

LINE_COLOR_BLUE = '#4B9EFF'
LINE_COLOR_RED = '#FF4136'
LINE_COLOR_GREEN = '#4CAF50'
LINE_COLOR_CYAN = '#00E5E5'


def quadratic_demo():
    st.markdown("<h2>Explore the Quadratic Function: f(x) = ax² + bx + c</h2>", unsafe_allow_html=True)
    
    # Initialize session state variables if they don't exist
    if 'quadratic_params' not in st.session_state:
        st.session_state.quadratic_params = {'a': 1.0, 'b': 0.0, 'c': 0}

    if st.button('Reset to Default Values'):
        st.session_state.quadratic_params = {'a': 1.0, 'b': 0.0, 'c': 0}
        st.rerun()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<p class="big-title-slider">a</p>', unsafe_allow_html=True)
        a = st.slider('-', min_value=-5.0, max_value=5.0, value=st.session_state.quadratic_params['a'], step=0.1, key='slider_a')
    with col2:
        st.markdown('<p class="big-title-slider">b</p>', unsafe_allow_html=True)
        b = st.slider('-', min_value=-20.0, max_value=20.0, value=st.session_state.quadratic_params['b'], step=1., key='slider_b')
    with col3:
        st.markdown('<p class="big-title-slider">c</p>', unsafe_allow_html=True)
        c = st.slider('-', min_value=-100, max_value=100, value=st.session_state.quadratic_params['c'], step=1, key='slider_c')

    # Update session state
    st.session_state.quadratic_params = {'a': a, 'b': b, 'c': c}


    x = np.linspace(-50, 50, 500)
    y = a * x**2 + b * x + c

    fig = go.Figure()
        
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'{a}x² + {b}x + {c}', line=dict(color=LINE_COLOR_BLUE)))

    # Add custom legend
    fig.add_annotation(
        x=1.02,
        y=1.05,
        xref="paper",
        yref="paper",
        text=f"<b>f(x) = {a:.2f}x² + {b:.2f}x + {c:.2f}</b>",
        showarrow=False,
        font=dict(family="Courier New, monospace", size=16, color=TEXT_COLOR),
        bgcolor="rgba(0,0,0,0.5)",
        bordercolor=TEXT_COLOR,
        borderwidth=2,
        borderpad=4,
        align="left",
    )

    fig.update_layout(
        xaxis_title='x',
        yaxis_title='y',
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=BACKGROUND_COLOR,
        font=dict(color='white'),
        height=600,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False,
        autosize=False
    )

    # Configure axes with a refined grid
    fig.update_xaxes(
        range=[-25, 25],
        showline=False,
        linewidth=2,
        linecolor=AXIS_COLOR,
        mirror=True,
        tickmode='linear',
        tick0=0,
        dtick=5,
        minor=dict(
            tickmode='linear',
            tick0=0,
            dtick=2.5,
            showgrid=True,
            gridcolor=GRID_COLOR,
            gridwidth=1
        ),
        showgrid=True,
        gridcolor=GRID_COLOR,
        gridwidth=1,
        zeroline=True,
        zerolinecolor=AXIS_COLOR,
        zerolinewidth=2.5
    )
    fig.update_yaxes(
        range=[-250, 250],
        showline=False,
        linewidth=2,
        linecolor=AXIS_COLOR,
        mirror=True,
        tickmode='linear',
        tick0=0,
        dtick=50,
        minor=dict(
            tickmode='linear',
            tick0=0,
            dtick=25,
            showgrid=True,
            gridcolor=GRID_COLOR,
            gridwidth=1
        ),
        showgrid=True,
        gridcolor=GRID_COLOR,
        gridwidth=1,
        zeroline=True,
        zerolinecolor=AXIS_COLOR,
        zerolinewidth=2.5
    )

    st.plotly_chart(fig, use_container_width=True)


def transformation_demo():

    # Base function parameters
    st.markdown("<h2>Base Function Parameters</h2>", unsafe_allow_html=True)

    # Function selection
    function_type = st.selectbox(
        "Select base function",
        ["Linear", "Quadratic", "Cubic"],
        key="function_type"
    )
    
    if function_type == "Linear":
        col1, col2 = st.columns(2)
        with col1:
            M = st.number_input("Slope (M)", value=1.0, step=0.1, min_value=-5.0, max_value=5.0, format="%.1f")
        with col2:
            B = st.number_input("y-intercept (B)", value=0.0, step=0.1, min_value=-10.0, max_value=10.0, format="%.1f")
        base_func = lambda x: M * x + B
        base_func_str = f"{M:.1f}x + {B:.1f}"
    elif function_type == "Quadratic":
        col1, col2, col3 = st.columns(3)
        with col1:
            A = st.number_input("A", value=1.0, step=0.1, min_value=-2.0, max_value=2.0, format="%.1f")
        with col2:
            B = st.number_input("B", value=0.0, step=0.5, min_value=-10.0, max_value=10.0, format="%.1f")
        with col3:
            C = st.number_input("C", value=0.0, step=0.5, min_value=-10.0, max_value=10.0, format="%.1f")
        base_func = lambda x: A * x**2 + B * x + C
        base_func_str = f"{A:.1f}x² + {B:.1f}x + {C:.1f}"
    else:  # Cubic
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            A = st.number_input("A", value=1.0, step=0.1, min_value=-2.0, max_value=2.0, format="%.1f")
        with col2:
            B = st.number_input("B", value=0.0, step=0.15, min_value=-10.0, max_value=10.0, format="%.1f")
        with col3:
            C = st.number_input("C", value=0.0, step=0.5, min_value=-10.0, max_value=10.0, format="%.1f")
        with col4:
            D = st.number_input("D", value=0.0, step=0.5, min_value=-10.0, max_value=10.0, format="%.1f")
        base_func = lambda x: A * x**3 + B * x**2 + C * x + D
        base_func_str = f"{A:.1f}x³ + {B:.1f}x² + {C:.1f}x + {D:.1f}"

    st.markdown(f"<div class='big-math-label'>f(x) = {base_func_str}</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Transformation parameters
    st.markdown("<h2>Transformation Parameters</h2>", unsafe_allow_html=True)

    # Initialize session state for transform parameters if not exists
    if 'transform_params' not in st.session_state:
        st.session_state.transform_params = {'a_trans': 1.0, 'b_trans': 1.0, 'c_trans': 0.0, 'd_trans': 0.0}

    # Add reset button
    if st.button('Reset Transformation Parameters'):
        st.session_state.transform_params = {'a_trans': 1.0, 'b_trans': 1.0, 'c_trans': 0.0, 'd_trans': 0.0}
        st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        a_trans = st.slider("Vertical Stretch (a)", -5.0, 5.0, st.session_state.transform_params['a_trans'], 0.1, key="vert_stretch")
        c_trans = st.slider("Horizontal Shift (c)", -10.0, 10.0, st.session_state.transform_params['c_trans'], 0.5, key="horiz_shift")
    with col2:
        b_trans = st.slider("Horizontal Stretch (b)", 0.1, 5.0, st.session_state.transform_params['b_trans'], 0.1, key="horiz_stretch")
        d_trans = st.slider("Vertical Shift (d)", -10.0, 10.0, st.session_state.transform_params['d_trans'], 0.5, key="vert_shift")

    # Update session state
    st.session_state.transform_params = {'a_trans': a_trans, 'b_trans': b_trans, 'c_trans': c_trans, 'd_trans': d_trans}

    # Generate x and y values
    x = np.linspace(-10, 10, 400)
    y_base = base_func(x)
    y_transformed = a_trans * base_func(b_trans * (x + c_trans)) + d_trans

    # Prepare the transformation string
    transform_parts = []
    if a_trans != 1:
        transform_parts.append(f"{a_trans:.1f} · ")
    transform_parts.append("f(")
    if b_trans != 1:
        transform_parts.append(f"{b_trans:.1f}")
    transform_parts.append("x")
    if c_trans != 0:
        transform_parts.append(f" {'+' if c_trans > 0 else '-'} {abs(c_trans):.1f}")
    transform_parts.append(")")
    if d_trans != 0:
        transform_parts.append(f" {'+' if d_trans > 0 else '-'} {abs(d_trans):.1f}")

    transform_str = "".join(transform_parts)

    st.markdown(
        f"""
        <div class='big-math-label'>
            g(x) = {transform_str}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()

    
    # Create plot
    fig = go.Figure()

    # Add base function
    fig.add_trace(go.Scatter(x=x, y=y_base, mode='lines', name=f'f(x) = {base_func_str}', line=dict(color=LINE_COLOR_BLUE)))

    # Add transformed function
    # transformed_func_str = f"{a_trans}f({b_trans}(x{'+' if c_trans >= 0 else '-'}{abs(c_trans)})) + {d_trans}"
    fig.add_trace(go.Scatter(x=x, y=y_transformed, mode='lines', name=f'g(x) = {transform_str}', line=dict(color=LINE_COLOR_RED)))

    # Add custom legend
    fig.add_annotation(
        x=1.02,
        y=1.05,
        xref="paper",
        yref="paper",
        text=f"<b>f(x) = {base_func_str}</b><br><b>g(x) = {transform_str}</b>",
        showarrow=False,
        font=dict(family="Courier New, monospace", size=14, color=TEXT_COLOR),
        bgcolor="rgba(0,0,0,0.5)",
        bordercolor=TEXT_COLOR,
        borderwidth=2,
        borderpad=4,
        align="left",
    )

    fig.update_layout(
        title='Function Transformation Visualization',
        xaxis_title='x',
        yaxis_title='y',
        plot_bgcolor=BACKGROUND_COLOR,
        paper_bgcolor=BACKGROUND_COLOR,
        font=dict(color='white'),
        height=600,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False,
        autosize=False
    )

    # Configure axes with a refined grid
    fig.update_xaxes(
        range=[-10, 10],
        showline=False,
        linewidth=2,
        linecolor=AXIS_COLOR,
        mirror=True,
        tickmode='linear',
        tick0=0,
        dtick=2,
        minor=dict(
            tickmode='linear',
            tick0=0,
            dtick=1,
            showgrid=True,
            gridcolor=GRID_COLOR,
            gridwidth=1
        ),
        showgrid=True,
        gridcolor=GRID_COLOR,
        gridwidth=1,
        zeroline=True,
        zerolinecolor=AXIS_COLOR,
        zerolinewidth=2.5
    )
    fig.update_yaxes(
        range=[-10, 10],
        showline=False,
        linewidth=2,
        linecolor=AXIS_COLOR,
        mirror=True,
        tickmode='linear',
        tick0=0,
        dtick=2,
        minor=dict(
            tickmode='linear',
            tick0=0,
            dtick=1,
            showgrid=True,
            gridcolor=GRID_COLOR,
            gridwidth=1
        ),
        showgrid=True,
        gridcolor=GRID_COLOR,
        gridwidth=1,
        zeroline=True,
        zerolinecolor=AXIS_COLOR,
        zerolinewidth=2.5
    )

    st.plotly_chart(fig, use_container_width=True)

    # Explanation
    st.markdown("""
    ### Transformation Explanations:
    - **Vertical Stretch/Compression (a)**: This parameter scales the output of the function. If |a| > 1, the graph stretches vertically, making it narrower. If 0 < |a| < 1, the graph compresses vertically, making it wider. If a is negative, it also reflects the graph across the x-axis.
    - **Horizontal Stretch/Compression (b)**: This parameter scales the input of the function. If |b| > 1, the graph compresses horizontally, making it narrower. If 0 < |b| < 1, the graph stretches horizontally, making it wider. If b is negative, it also reflects the graph across the y-axis.
    - **Horizontal Shift (c)**: This parameter shifts the graph horizontally. If c is positive, the graph shifts to the left by c units. If c is negative, the graph shifts to the right by |c| units.
    - **Vertical Shift (d)**: This parameter shifts the graph vertically. If d is positive, the graph shifts up by d units. If d is negative, the graph shifts down by |d| units.

    The combined transformation is: g(x) = a * f(b(x + c)) + d
    """)