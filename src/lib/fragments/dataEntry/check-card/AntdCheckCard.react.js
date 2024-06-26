import React, { useEffect, useContext } from 'react';
import { CheckCard } from '@ant-design/pro-components';
import { isUndefined, isString } from 'lodash';
import { pickBy } from 'ramda';
import useCss from '../../../hooks/useCss';
import PropsContext from '../../../contexts/PropsContext';
import FormContext from '../../../contexts/FormContext';
import useFormStore from '../../../store/formStore';
import { propTypes, defaultProps } from '../../../components/dataEntry/check-card/AntdCheckCard.react';

// 定义选择卡片组件AntdCheckCard，api参数参考https://procomponents.ant.design/components/check-card
const AntdCheckCard = (props) => {
    // 取得必要属性或参数
    let {
        id,
        children,
        className,
        style,
        key,
        name,
        checked,
        bordered,
        value,
        defaultChecked,
        disabled,
        size,
        readOnly,
        setProps,
        loading_state,
        persistence,
        persisted_props,
        persistence_type
    } = props;

    const context = useContext(PropsContext)
    const formId = useContext(FormContext)

    const updateItemValue = useFormStore((state) => state.updateItemValue)
    const deleteItemValue = useFormStore((state) => state.deleteItemValue)

    // 处理AntdForm表单值搜集功能
    useEffect(() => {
        // 若上文中存在有效表单id
        if (formId && (name || id)) {
            // 表单值更新
            updateItemValue(formId, name || id, checked)
        }
    }, [checked, name, id])

    // 处理组件卸载后，对应表单项值的清除
    useEffect(() => {
        return () => {
            // 若上文中存在有效表单id
            if (formId && (name || id)) {
                // 表单值更新
                deleteItemValue(formId, name || id)
            }
        }
    }, [name, id])

    useEffect(() => {
        if (!isUndefined(defaultChecked) && isUndefined(checked)) {
            setProps({ checked: defaultChecked })
        }
    }, [])

    return (
        <CheckCard
            // 提取具有data-*或aria-*通配格式的属性
            {...pickBy((_, k) => k.startsWith('data-') || k.startsWith('aria-'), props)}
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            description={children}
            checked={checked}
            bordered={bordered}
            value={value}
            defaultChecked={defaultChecked}
            disabled={
                context && !isUndefined(context.componentDisabled) ?
                    context.componentDisabled :
                    disabled
            }
            size={size}
            onChange={e => {
                if (!readOnly) {
                    setProps({ checked: e })
                }
            }}
            persistence={persistence}
            persisted_props={persisted_props}
            persistence_type={persistence_type}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default AntdCheckCard;

AntdCheckCard.defaultProps = defaultProps;
AntdCheckCard.propTypes = propTypes;