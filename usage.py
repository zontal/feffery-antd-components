import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdButton(
            '测试',
            **{
                'aria-label': 'aria',
                'data-test': 'data',
            },
        )
    ],
    style={'padding': '50px 100px'},
)

if __name__ == '__main__':
    app.run(debug=True)
