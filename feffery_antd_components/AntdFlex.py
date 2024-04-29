# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdFlex(Component):
    """An AntdFlex component.
弹性布局组件AntdFlex

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    组件型，内嵌元素.

- id (string; optional):
    组件唯一id.

- align (string; default 'normal'):
    子元素在交叉轴方向上的对齐方式，同css中的align-items 默认值：`'normal'`.

- aria-* (string; optional):
    `aria-*`格式属性通配.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- data-* (string; optional):
    `data-*`格式属性通配.

- flex (string; default 'normal'):
    同css中的flex 默认值：`'normal'`.

- gap (string | number | a value equal to: 'small', 'middle', 'large'; optional):
    子元素之间的间隙，可选项有`'small'`、`'middle'`、`'large'`，也可传入字符型css宽度，或数值型像素宽度.

- justify (string; default 'normal'):
    子元素在主轴方向上的对齐方式，同css中的justify-content 默认值：`'normal'`.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    当前组件css样式.

- vertical (boolean; default False):
    是否使用垂直主轴 默认值：`False`.

- wrap (string; default 'nowrap'):
    子元素换行显示行为，同css中的flex-wrap 默认值：`'nowrap'`."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdFlex'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, vertical=Component.UNDEFINED, wrap=Component.UNDEFINED, justify=Component.UNDEFINED, align=Component.UNDEFINED, flex=Component.UNDEFINED, gap=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'align', 'aria-*', 'className', 'data-*', 'flex', 'gap', 'justify', 'key', 'loading_state', 'style', 'vertical', 'wrap']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'align', 'aria-*', 'className', 'data-*', 'flex', 'gap', 'justify', 'key', 'loading_state', 'style', 'vertical', 'wrap']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(AntdFlex, self).__init__(children=children, **args)
