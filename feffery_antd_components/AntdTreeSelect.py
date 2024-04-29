# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTreeSelect(Component):
    """An AntdTreeSelect component.


Keyword arguments:

- id (string; optional)

- allowClear (boolean; default True)

- aria-* (string; optional):
    `aria-*`格式属性通配.

- autoClearSearchValue (boolean; default True)

- batchPropsNames (list of strings; optional)

- batchPropsValues (dict; optional)

- bordered (boolean; default True):
    设置是否渲染边框，设置为True时等价于variant='outlined' 默认：True.

- className (string | dict; optional)

- data-* (string; optional):
    `data-*`格式属性通配.

- defaultValue (string | number | list of string | numbers; optional)

- disabled (boolean; default False)

- dropdownAfter (a list of or a singular dash component, string or number; optional)

- dropdownBefore (a list of or a singular dash component, string or number; optional)

- key (string; optional)

- listHeight (number; default 256)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn')

- maxTagCount (number | a value equal to: 'responsive'; optional)

- multiple (boolean; default False)

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

- showCheckedStrategy (a value equal to: 'show-all', 'show-parent', 'show-child'; default 'show-all')

- size (a value equal to: 'small', 'middle', 'large'; default 'middle')

- status (a value equal to: 'error', 'warning'; optional)

- style (dict; optional)

- treeCheckStrictly (boolean; default False)

- treeCheckable (boolean; default False)

- treeData (list; required)

- treeDataMode (a value equal to: 'tree', 'flat'; default 'tree')

- treeDefaultExpandAll (boolean; default False)

- treeDefaultExpandedKeys (list of strings; optional)

- treeExpandedKeys (list of strings; optional)

- treeLine (boolean; default False)

- treeNodeFilterMode (a value equal to: 'case-insensitive', 'case-sensitive', 'regex'; default 'case-insensitive')

- treeNodeFilterProp (a value equal to: 'title', 'value'; default 'value')

- treeNodeKeyToTitle (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional)

- value (string | number | list of string | numbers; optional)

- variant (a value equal to: 'outlined', 'borderless', 'filled'; optional):
    设置形态变体类型，可选的有'outlined'、'borderless'、'filled'
    其中'outlined'等价于bordered=True，优先级高于bordered.

- virtual (boolean; default True)"""
    _children_props = ['treeNodeKeyToTitle{}', 'dropdownBefore', 'dropdownAfter']
    _base_nodes = ['dropdownBefore', 'dropdownAfter', 'children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdTreeSelect'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, popupClassName=Component.UNDEFINED, key=Component.UNDEFINED, name=Component.UNDEFINED, locale=Component.UNDEFINED, treeDataMode=Component.UNDEFINED, treeData=Component.REQUIRED, treeNodeKeyToTitle=Component.UNDEFINED, disabled=Component.UNDEFINED, size=Component.UNDEFINED, bordered=Component.UNDEFINED, variant=Component.UNDEFINED, placeholder=Component.UNDEFINED, placement=Component.UNDEFINED, treeLine=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, maxTagCount=Component.UNDEFINED, listHeight=Component.UNDEFINED, multiple=Component.UNDEFINED, treeCheckable=Component.UNDEFINED, treeCheckStrictly=Component.UNDEFINED, treeDefaultExpandAll=Component.UNDEFINED, treeDefaultExpandedKeys=Component.UNDEFINED, treeExpandedKeys=Component.UNDEFINED, virtual=Component.UNDEFINED, status=Component.UNDEFINED, allowClear=Component.UNDEFINED, treeNodeFilterProp=Component.UNDEFINED, treeNodeFilterMode=Component.UNDEFINED, autoClearSearchValue=Component.UNDEFINED, showCheckedStrategy=Component.UNDEFINED, dropdownBefore=Component.UNDEFINED, dropdownAfter=Component.UNDEFINED, readOnly=Component.UNDEFINED, popupContainer=Component.UNDEFINED, batchPropsNames=Component.UNDEFINED, batchPropsValues=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowClear', 'aria-*', 'autoClearSearchValue', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'data-*', 'defaultValue', 'disabled', 'dropdownAfter', 'dropdownBefore', 'key', 'listHeight', 'loading_state', 'locale', 'maxTagCount', 'multiple', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'placement', 'popupClassName', 'popupContainer', 'readOnly', 'showCheckedStrategy', 'size', 'status', 'style', 'treeCheckStrictly', 'treeCheckable', 'treeData', 'treeDataMode', 'treeDefaultExpandAll', 'treeDefaultExpandedKeys', 'treeExpandedKeys', 'treeLine', 'treeNodeFilterMode', 'treeNodeFilterProp', 'treeNodeKeyToTitle', 'value', 'variant', 'virtual']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'allowClear', 'aria-*', 'autoClearSearchValue', 'batchPropsNames', 'batchPropsValues', 'bordered', 'className', 'data-*', 'defaultValue', 'disabled', 'dropdownAfter', 'dropdownBefore', 'key', 'listHeight', 'loading_state', 'locale', 'maxTagCount', 'multiple', 'name', 'persisted_props', 'persistence', 'persistence_type', 'placeholder', 'placement', 'popupClassName', 'popupContainer', 'readOnly', 'showCheckedStrategy', 'size', 'status', 'style', 'treeCheckStrictly', 'treeCheckable', 'treeData', 'treeDataMode', 'treeDefaultExpandAll', 'treeDefaultExpandedKeys', 'treeExpandedKeys', 'treeLine', 'treeNodeFilterMode', 'treeNodeFilterProp', 'treeNodeKeyToTitle', 'value', 'variant', 'virtual']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['treeData']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdTreeSelect, self).__init__(**args)
