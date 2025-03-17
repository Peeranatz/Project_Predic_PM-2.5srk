from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# สร้างแอป Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "style.css"])


# สร้างแผนที่
def create_map():
    # ข้อมูลของแต่ละพื้นที่
    df = pd.DataFrame(
        {
            "lat": [
                9.135369739503975,
                7.020309167422308,
                6.978699681363061,
                7.005287444298349,
            ],  # ละติจูดของแต่ละพื้นที่
            "lon": [
                99.33177228415428,
                100.47099961070477,
                100.48087891070438,
                100.46776709950608,
            ],  # ลองจิจูดของแต่ละพื้นที่
            "id": ["JSPS001", "JSPS014", "JSPS016", "JSPS018"],  # ID ของแต่ละพื้นที่
        }
    )

    # สีสำหรับแต่ละหมุด
    colors = ["red", "blue", "green", "purple"]

    # สร้างแผนที่ด้วย go.Scattermapbox
    fig = go.Figure()

    # เพิ่มหมุดสำหรับแต่ละพื้นที่
    for i, row in df.iterrows():
        fig.add_trace(
            go.Scattermapbox(
                lat=[row["lat"]],
                lon=[row["lon"]],
                mode="markers+text",
                marker=dict(
                    size=15,  # ขนาดของหมุด
                    color=colors[i],  # สีของหมุด
                    symbol="circle",  # รูปทรงของหมุด
                ),
                text=[row["id"]],  # ข้อความแสดง ID ของพื้นที่
                textposition="top right",  # ตำแหน่งของข้อความ
                hoverinfo="text",  # ข้อมูลที่แสดงเมื่อ hover
                name=row["id"],  # ชื่อของพื้นที่
            )
        )

    # ปรับแต่ง layout ของแผนที่
    fig.update_layout(
        mapbox=dict(
            style="open-street-map",  # สไตล์แผนที่
            center=dict(
                lat=7.005287444298349, lon=100.46776709950608
            ),  # จุดศูนย์กลางของแผนที่
            zoom=8,  # ระดับการซูม
        ),
        margin=dict(l=0, r=0, t=0, b=0),  # ระยะขอบ
        showlegend=False,  # ไม่แสดง legend
    )

    return dcc.Graph(
        id="sensor_map",
        figure=fig,
        style={"height": "600px", "width": "100%"},  # ปรับขนาดของแผนที่
    )


# สร้างกราฟเริ่มต้น (สีดำ)
def create_initial_graph():
    fig = go.Figure()
    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="PM2.5 (µg/m³)",
        title="PM2.5 Forecast",
        title_font_size=20,
        title_x=0.5,
        plot_bgcolor="var(--secondary-color)",
        paper_bgcolor="var(--secondary-color)",
        font_color="var(--text-color)",
    )
    return fig


# สร้างส่วนควบคุม (เพิ่ม Dropdown สำหรับเลือกพื้นที่)
def create_controls():
    return [
        html.Label(
            "Select number of days to forecast:",
            className="mb-2 font-weight-bold important-text",
            style={"fontSize": "1.2rem"},
        ),
        html.Button(
            "Predict",
            id="predict_button",
            n_clicks=0,
            className="btn btn-primary btn-lg w-100 custom-button",
        ),
    ]


# สร้างการ์ดแสดงผลการทำนาย (ไม่มีส่วนที่เกี่ยวข้องกับเซ็นเซอร์)
def create_prediction_cards(predicted_values):
    cards = []
    for i, value in enumerate(predicted_values):
        card = dbc.Card(
            dbc.CardBody(
                [
                    html.H4(
                        f"Day {i+1}",
                        className="card-title",
                        style={"color": "var(--primary-color)"},
                    ),
                    html.P(
                        f"PM2.5: {value:.2f} µg/m³",
                        className="card-text",
                        style={"color": "var(--primary-color)"},
                    ),
                ]
            ),
            className="m-2 prediction-card",
            style={"width": "18%", "display": "inline-block"},
        )
        cards.append(card)
    return cards


def create_layout():
    return dbc.Container(
        [
            # พื้นหลังเคลื่อนไหว
            html.Div(className="background-effect"),
            # Header
            dbc.Row(
                dbc.Col(
                    html.Div(
                        html.H1(
                            "🌍 PM2.5 WATCHER",
                            className="text-center font-weight-bold important-text custom-header",
                            style={"color": "var(--background-color)"},
                        ),
                    ),
                    width=12,
                    className="mb-4",
                )
            ),
            # แถวหลัก (แผนที่และกราฟ)
            dbc.Row(
                [
                    # ด้านซ้าย: แผนที่ (ลดความกว้าง)
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                create_map(),
                                style={
                                    "height": "400px",
                                    "overflow": "hidden",
                                },  # ความยาวเท่าเดิม
                            ),
                            className="mb-4 custom-card",
                        ),
                        width=4,  # ลดความกว้างของแผนที่จาก 6 เป็น 4
                    ),
                    # ด้านขวา: ส่วนควบคุมและกราฟ (เพิ่มความกว้าง)
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    # ส่วนควบคุม
                                    html.Div(
                                        [
                                            html.Label(
                                                "Select number of days to forecast:",
                                                className="mb-2 font-weight-bold important-text",
                                                style={
                                                    "fontSize": "1.2rem",
                                                    "color": "var(--text-color)",
                                                },
                                            ),
                                            dcc.RadioItems(
                                                id="days_radio",
                                                options=[
                                                    {"label": "7 Days", "value": 7},
                                                    {"label": "14 Days", "value": 14},
                                                ],
                                                value=7,  # ค่าเริ่มต้น
                                                inline=True,
                                                className="mb-4 dcc_radio_items",
                                                style={"color": "var(--text-color)"},
                                            ),
                                            html.Button(
                                                "Predict",
                                                id="predict_button",
                                                n_clicks=0,
                                                className="btn btn-primary btn-lg w-100 custom-button",
                                            ),
                                        ],
                                        style={"marginBottom": "30px"},
                                    ),
                                    # กราฟ (เพิ่มความกว้าง)
                                    dcc.Graph(
                                        id="pm25_graph",
                                        figure=create_initial_graph(),
                                        style={
                                            "height": "400px",
                                            "width": "100%",
                                        },  # ความยาวเท่าเดิม
                                    ),
                                ]
                            ),
                            className="custom-card",
                        ),
                        width=8,  # เพิ่มความกว้างของกราฟจาก 6 เป็น 8
                    ),
                ],
                justify="center",
                style={"marginBottom": "30px"},
            ),
            # แถวแสดงผลการทำนาย (ไม่เปลี่ยนแปลงความกว้าง)
            dbc.Row(
                dbc.Col(
                    html.Div(
                        id="prediction_output",
                        style={"fontSize": "1.2rem", "textAlign": "center"},
                    ),
                    width=12,
                    className="mb-4",
                )
            ),
        ],
        fluid=True,
        style={"maxWidth": "1400px", "padding": "30px"},
    )
