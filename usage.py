import json
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdTable(
            id='input',
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'width': 'calc(100% / 3)'
                }
                for i in range(1, 4)
            ],
            data=[
                {
                    'key': f'row-{i}',
                    '字段1': '第一层',
                    '字段2': '第一层',
                    '字段3': '第一层',
                    'children': [
                        {
                            'key': f'row-{i}{j}',
                            '字段1': '第二层',
                            '字段2': '第二层',
                            '字段3': '第二层'
                        }
                        for j in range(3)
                    ]
                }
                for i in range(3)
            ],
            bordered=True,
            rowSelectionType='checkbox',
            rowSelectionCheckStrictly=False,
            showHeader=False,
            footer=fac.AntdSpace(
                [
                    fac.AntdTag(
                        content=f'标签{i}',
                        color='green'
                    )
                    for i in range(1, 6)
                ]
            )
        ),
        html.Pre(
            id='output'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('output', 'children'),
    Input('input', 'selectedRowKeys'),
    prevent_initial_call=True
)
def demo(selectedRowKeys):

    return json.dumps(
        dict(selectedRowKeys=selectedRowKeys),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
