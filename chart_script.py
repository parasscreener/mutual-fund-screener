import plotly.graph_objects as go
import plotly.express as px
import json

# Data using exact names from instructions and provided data
data = {
    "components": [
        {
            "layer": "Data Sources",
            "items": [
                {"name": "Market Data APIs", "type": "market_data", "color": "#4A90E2"},
                {"name": "Mutual Fund Data", "type": "fund_data", "color": "#4A90E2"},
                {"name": "News Sources", "type": "news_data", "color": "#4A90E2"}
            ]
        },
        {
            "layer": "Core Processing Engine",
            "items": [
                {"name": "Screen Algorithm", "type": "core_logic", "color": "#50C878"},
                {"name": "Momentum Indicators", "type": "technical_analysis", "color": "#50C878"},
                {"name": "Technical Analysis", "type": "analytics", "color": "#50C878"}
            ]
        },
        {
            "layer": "Analysis Components",
            "items": [
                {"name": "Beaten-down Fund Detection", "type": "screening", "color": "#32CD32"},
                {"name": "Recovery Potential Scoring", "type": "analytics", "color": "#32CD32"},
                {"name": "Market Context Integration", "type": "context_analysis", "color": "#32CD32"}
            ]
        },
        {
            "layer": "Output Generation",
            "items": [
                {"name": "HTML Dashboard", "type": "web_output", "color": "#FF8C42"},
                {"name": "CSV Reports", "type": "data_export", "color": "#FF8C42"},
                {"name": "JSON Data", "type": "api_output", "color": "#FF8C42"}
            ]
        },
        {
            "layer": "Automation & Deployment",
            "items": [
                {"name": "GitHub Actions", "type": "automation", "color": "#9B59B6"},
                {"name": "Scheduled Execution", "type": "scheduler", "color": "#9B59B6"},
                {"name": "Web Deployment", "type": "hosting", "color": "#9B59B6"}
            ]
        },
        {
            "layer": "User Interface",
            "items": [
                {"name": "Live Web Dashboard", "type": "ui", "color": "#E74C3C"},
                {"name": "Mobile Responsive", "type": "responsive", "color": "#E74C3C"},
                {"name": "Real-time Updates", "type": "updates", "color": "#E74C3C"}
            ]
        }
    ],
    "metrics": [
        {"name": "Schedule", "value": "9:30 AM IST Daily"},
        {"name": "Momentum Score", "value": "0-100"},
        {"name": "Recommendations", "value": "Strong Buy/Buy/Hold/Avoid"}
    ]
}

# Create figure
fig = go.Figure()

# Define positions for each layer (y-coordinates) with more vertical spacing
layer_y_positions = [6, 5, 4, 3, 2, 1]
layer_names = ["Data Sources", "Core Processing Engine", "Analysis Components", "Output Generation", "Automation & Deployment", "User Interface"]

# Create rectangles and text for each component
shapes = []
annotations = []

for layer_idx, layer in enumerate(data["components"]):
    layer_y = layer_y_positions[layer_idx]
    items = layer["items"]
    
    # Calculate x positions for items in this layer with better spacing
    n_items = len(items)
    if n_items == 3:
        x_positions = [3, 6, 9]
    elif n_items == 4:
        x_positions = [2, 4.5, 7, 9.5]
    else:
        x_positions = [i * 3 + 3 for i in range(n_items)]
    
    for item_idx, item in enumerate(items):
        x_pos = x_positions[item_idx]
        y_pos = layer_y
        
        # Add rectangle shape - larger boxes for better text fit
        shapes.append(
            dict(
                type="rect",
                x0=x_pos - 1.3,
                y0=y_pos - 0.4,
                x1=x_pos + 1.3,
                y1=y_pos + 0.4,
                fillcolor=item["color"],
                line=dict(color="white", width=2),
                opacity=0.9
            )
        )
        
        # Abbreviate long names to fit in boxes while keeping meaning
        display_name = item["name"]
        if len(display_name) > 15:
            if "Beaten-down" in display_name:
                display_name = "Beaten-down ID"
            elif "Recovery Potential" in display_name:
                display_name = "Recovery Score"
            elif "Market Context" in display_name:
                display_name = "Market Context"
            elif "Scheduled" in display_name:
                display_name = "Daily Schedule"
            elif "Live Web" in display_name:
                display_name = "Live Dashboard"
        
        # Add text annotation with larger font
        annotations.append(
            dict(
                x=x_pos,
                y=y_pos,
                text=display_name,
                showarrow=False,
                font=dict(color="white", size=13, family="Arial Black"),
                xanchor="center",
                yanchor="middle"
            )
        )

# Add layer labels - larger and positioned better
for layer_idx, layer_name in enumerate(layer_names):
    layer_y = layer_y_positions[layer_idx]
    # Abbreviate layer names if too long
    display_layer_name = layer_name
    if len(display_layer_name) > 15:
        if "Core Processing" in display_layer_name:
            display_layer_name = "Processing"
        elif "Analysis Components" in display_layer_name:
            display_layer_name = "Analysis"
        elif "Output Generation" in display_layer_name:
            display_layer_name = "Output"
        elif "Automation &" in display_layer_name:
            display_layer_name = "Automation"
    
    annotations.append(
        dict(
            x=0.5,
            y=layer_y,
            text=f"<b>{display_layer_name}</b>",
            showarrow=False,
            font=dict(color="#2C3E50", size=14, family="Arial Black"),
            xanchor="right",
            yanchor="middle"
        )
    )

# Add flow arrows between layers - thicker and more visible
for i in range(len(layer_y_positions) - 1):
    current_y = layer_y_positions[i]
    next_y = layer_y_positions[i + 1]
    
    # Add main flow arrows
    for x in [4.5, 7.5]:
        shapes.append(
            dict(
                type="line",
                x0=x,
                y0=current_y - 0.45,
                x1=x,
                y1=next_y + 0.45,
                line=dict(color="#2C3E50", width=4),
            )
        )
        
        # Add arrowhead - larger and more visible
        shapes.append(
            dict(
                type="line",
                x0=x - 0.2,
                y0=next_y + 0.65,
                x1=x,
                y1=next_y + 0.45,
                line=dict(color="#2C3E50", width=4),
            )
        )
        shapes.append(
            dict(
                type="line",
                x0=x + 0.2,
                y0=next_y + 0.65,
                x1=x,
                y1=next_y + 0.45,
                line=dict(color="#2C3E50", width=4),
            )
        )

# Add metrics box in a better position - top right without overlap
shapes.append(
    dict(
        type="rect",
        x0=11,
        y0=5.5,
        x1=14.5,
        y1=6.8,
        fillcolor="#F8F9FA",
        line=dict(color="#2C3E50", width=2),
        opacity=0.95
    )
)

annotations.append(
    dict(
        x=12.75,
        y=6.6,
        text="<b>Key Metrics</b>",
        showarrow=False,
        font=dict(color="#2C3E50", size=14, family="Arial Black"),
        xanchor="center",
        yanchor="middle"
    )
)

# Add individual metric lines with better spacing
metric_y_positions = [6.3, 6.1, 5.9]
for idx, metric in enumerate(data["metrics"]):
    annotations.append(
        dict(
            x=12.75,
            y=metric_y_positions[idx],
            text=f"<b>{metric['name']}:</b> {metric['value']}",
            showarrow=False,
            font=dict(color="#2C3E50", size=11),
            xanchor="center",
            yanchor="middle"
        )
    )

# Create a dummy scatter plot to establish the coordinate system
fig.add_trace(go.Scatter(
    x=[0, 15],
    y=[0, 7.5],
    mode='markers',
    marker=dict(size=0, opacity=0),
    showlegend=False,
    hoverinfo='skip'
))

# Update layout with better spacing
fig.update_layout(
    title="Mutual Fund Recovery Screener Flow",
    shapes=shapes,
    annotations=annotations,
    showlegend=False,
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-1, 15]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[0.3, 7.2]
    ),
    plot_bgcolor='rgba(248,249,250,0.2)',
    paper_bgcolor='white'
)

# Save the chart with optimal dimensions
fig.write_image("mutual_fund_recovery_screener_flow.png", width=1500, height=1000)