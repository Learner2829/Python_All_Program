import plotly.graph_objs as go
import pandas as pd
from django.shortcuts import render

def candlestick_chart(request):
    # Dummy OHLC Data
    data = [
        {'date': '2025-02-18 09:00:00', 'open': 1500, 'high': 1520, 'low': 1490, 'close': 1510},
        {'date': '2025-02-18 10:00:00', 'open': 1510, 'high': 1530, 'low': 1505, 'close': 1525},
        {'date': '2025-02-18 11:00:00', 'open': 1525, 'high': 1540, 'low': 1520, 'close': 1535},
        {'date': '2025-02-18 12:00:00', 'open': 1535, 'high': 1555, 'low': 1530, 'close': 1545},
        {'date': '2025-02-18 13:00:00', 'open': 1545, 'high': 1560, 'low': 1540, 'close': 1555},
        {'date': '2025-02-18 14:00:00', 'open': 1555, 'high': 1570, 'low': 1545, 'close': 1565},
        {'date': '2025-02-18 14:00:00', 'open': 1400, 'high':1410, 'low': 1545, 'close': 1565},
    ]

    # Convert the data to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    # Create the candlestick chart using Plotly
    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        increasing_line_color='green',
        decreasing_line_color='red'
    )])

    # Update the layout for the candlestick chart
    fig.update_layout(
        title="Sample Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False  # Disable range slider for a cleaner chart
    )

    # Convert the Plotly figure to HTML
    chart_html = fig.to_html(full_html=False)

    # Render the template with the chart
    return render(request, 'live_trading/candlestick_chart.html', {'chart_html': chart_html})
