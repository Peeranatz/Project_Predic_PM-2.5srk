import dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks

# กำหนดชื่อแอป Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# กำหนดเลย์เอาต์
app.layout = create_layout()

register_callbacks(app)

# รันแอป
if __name__ == "__main__":
    app.run_server(debug=True)
