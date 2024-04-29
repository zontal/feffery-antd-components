# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdInputNumber(Component):
    """An AntdInputNumber component.


Keyword arguments:

- id (string; optional)

- addonAfter (a list of or a singular dash component, string or number; optional)

- addonBefore (a list of or a singular dash component, string or number; optional)

- aria-* (string; optional):
    `aria-*`格式属性通配.

- autoFocus (boolean; default False)

- batchPropsNames (list of strings; optional)

- batchPropsValues (dict; optional)

- bordered (boolean; default True):
    设置是否渲染边框，设置为True时等价于variant='outlined' 默认：True.

- className (string | dict; optional)

- controls (boolean; default True)

- data-* (string; optional):
    `data-*`格式属性通配.

- debounceValue (number | string; optional)

- debounceWait (number; default 0)

- defaultValue (number | string; optional)

- disabled (boolean; default False)

- key (string; optional)

- keyboard (boolean; default True)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- max (number | string; optional)

- min (number | string; optional)

- nSubmit (number; default 0)

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

- precision (number; optional)

- prefix (a list of or a singular dash component, string or number; optional)

- readOnly (boolean; optional)

- size (a value equal to: 'small', 'middle', 'large'; default 'middle')

- status (a value equal to: 'error', 'warning'; optional)

- step (number | string; optional)

- stringMode (boolean; default False)

- style (dict; optional)

- value (number | string; optional)

- variant (a value equal to: 'outlined', 'borderless', 'filled'; optional):
    设置形态变体类型，可选的有'outlined'、'borderless'、'filled'
    其中'outlined'等价于bordered=True，优先级高于bordered."""
    _children_props = ['addonBefore', 'addonAfter', 'prefix']
    _base_nodes = ['addonBefore', 'addonAfter', 'prefix', 'children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdInputNumber'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, name=Component.UNDEFINED, addonBefore=Component.UNDEFINED, addonAfter=Component.UNDEFINED, autoFocus=Component.UNDEFINED, prefix=Component.UNDEFINED, controls=Component.UNDEFINED, keyboard=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, step=Component.UNDEFINED, precision=Component.UNDEFINED, stringMode=Component.UNDEFINED, disabled=Component.UNDEFINED, size=Component.UNDEFINED, bordered=Component.UNDEFINED, variant=Component.UNDEFINED, placeholder=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, debounceValue=Component.UNDEFINED, debounceWait=Component.UNDEFINED, nSubmit=Component.UNDEFINED, status=Component.UNDEFINED, readOnly=Component.UNDEFINED, batchPropsNames=Component.UNDEFINED, batchPropsValues=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'addonAfter', 'addonBefore', 'aria-*', 'autoFocus', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'controls', 'data-*', 'debounceValue', 'debounceWait', 'defaultValue', 'disabled', 'key', 'keyboard', 'loading_state', 'max', 'min', 'nSubmit', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'precision', 'prefix', 'readOnly', 'size', 'status', 'step', 'stringMode', 'style', 'value', 'variant']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'addonAfter', 'addonBefore', 'aria-*', 'autoFocus', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'controls', 'data-*', 'debounceValue', 'debounceWait', 'defaultValue', 'disabled', 'key', 'keyboard', 'loading_state', 'max', 'min', 'nSubmit', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'precision', 'prefix', 'readOnly', 'size', 'status', 'step', 'stringMode', 'style', 'value', 'variant']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdInputNumber, self).__init__(**args)
