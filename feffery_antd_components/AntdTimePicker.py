# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTimePicker(Component):
    """An AntdTimePicker component.


Keyword arguments:

- id (string; optional)

- allowClear (boolean; default True)

- aria-* (string; optional):
    `aria-*`格式属性通配.

- autoFocus (boolean; default False)

- batchPropsNames (list of strings; optional)

- batchPropsValues (dict; optional)

- bordered (boolean; default True):
    设置是否渲染边框，设置为True时等价于variant='outlined' 默认：True.

- className (string | dict; optional)

- data-* (string; optional):
    `data-*`格式属性通配.

- defaultValue (string; optional)

- disabled (boolean; default False)

- extraFooter (a list of or a singular dash component, string or number; optional)

- format (string; default 'HH:mm:ss')

- hourStep (number; default 1)

- key (string; optional)

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn')

- minuteStep (number; default 1)

- name (string; optional):
    用于在基于AntdForm的表单值自动搜集功能中，充当当前表单项的字段名 缺省时会以id作为字段名.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- placeholder (string; optional)

- placement (a value equal to: 'bottomLeft', 'bottomRight', 'topLeft', 'topRight'; default 'bottomLeft')

- popupClassName (string; optional):
    设置弹框菜单css类名.

- popupContainer (a value equal to: 'parent', 'body'; default 'body')

- readOnly (boolean; optional)

- secondStep (number; default 1)

- showNow (boolean; default True)

- size (a value equal to: 'small', 'middle', 'large'; default 'middle')

- status (a value equal to: 'error', 'warning'; optional)

- style (dict; optional)

- use12Hours (boolean; default False)

- value (string; optional)

- variant (a value equal to: 'outlined', 'borderless', 'filled'; optional):
    设置形态变体类型，可选的有'outlined'、'borderless'、'filled'
    其中'outlined'等价于bordered=True，优先级高于bordered."""
    _children_props = ['extraFooter']
    _base_nodes = ['extraFooter', 'children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdTimePicker'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, popupClassName=Component.UNDEFINED, key=Component.UNDEFINED, name=Component.UNDEFINED, locale=Component.UNDEFINED, format=Component.UNDEFINED, disabled=Component.UNDEFINED, hourStep=Component.UNDEFINED, minuteStep=Component.UNDEFINED, secondStep=Component.UNDEFINED, use12Hours=Component.UNDEFINED, size=Component.UNDEFINED, bordered=Component.UNDEFINED, variant=Component.UNDEFINED, placeholder=Component.UNDEFINED, placement=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, status=Component.UNDEFINED, allowClear=Component.UNDEFINED, autoFocus=Component.UNDEFINED, readOnly=Component.UNDEFINED, extraFooter=Component.UNDEFINED, showNow=Component.UNDEFINED, popupContainer=Component.UNDEFINED, batchPropsNames=Component.UNDEFINED, batchPropsValues=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowClear', 'aria-*', 'autoFocus', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'data-*', 'defaultValue', 'disabled', 'extraFooter', 'format', 'hourStep', 'key', 'loading_state', 'locale', 'minuteStep', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'placement', 'popupClassName', 'popupContainer', 'readOnly', 'secondStep', 'showNow', 'size', 'status', 'style', 'use12Hours', 'value', 'variant']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowClear', 'aria-*', 'autoFocus', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'data-*', 'defaultValue', 'disabled', 'extraFooter', 'format', 'hourStep', 'key', 'loading_state', 'locale', 'minuteStep', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'placement', 'popupClassName', 'popupContainer', 'readOnly', 'secondStep', 'showNow', 'size', 'status', 'style', 'use12Hours', 'value', 'variant']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdTimePicker, self).__init__(**args)
