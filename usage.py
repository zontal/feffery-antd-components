import dash
from dash import html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    fac.AntdSpace(
        [
            fac.AntdNotification(
                message='通知提示框示例',
                duration=0,
                type='info',
                placement='topLeft',
                closeButton={
                    'content': '我知道了'
                },
                closable=False
            )
        ],
        direction='vertical',
        style={
            'width': '100%'
        }
    ),
    style={
        'padding': '50px 100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
