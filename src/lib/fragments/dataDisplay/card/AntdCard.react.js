import React from 'react';
import { Card } from 'antd';
import { isString } from 'lodash';
import { pickBy } from 'ramda';
import useCss from '../../../hooks/useCss';
import { parseChildrenToArray } from '../../../components/utils';
import { propTypes, defaultProps } from '../../../components/dataDisplay/card/AntdCard.react';

// 定义卡片组件AntdCard，api参数参考https://ant.design/components/card-cn/
const AntdCard = (props) => {
    // 取得必要属性或参数
    let {
        id,
        children,
        className,
        style,
        key,
        actions,
        extraLink,
        extra,
        coverImg,
        bodyStyle,
        headStyle,
        bordered,
        hoverable,
        size,
        title,
        nClicks,
        setProps,
        loading_state
    } = props;

    children = parseChildrenToArray(children)

    return (
        <Card
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
            bodyStyle={{
                // 确保网格卡片排布正常
                display: 'flex',
                flexWrap: 'wrap',
                ...bodyStyle
            }}
            headStyle={headStyle}
            actions={actions}
            extra={
                extra || (
                    <a className={extraLink && extraLink.className}
                        style={extraLink && extraLink.style}
                        href={extraLink && extraLink.href}
                        target={extraLink && extraLink.target || '_blank'}>
                        {extraLink && extraLink.content}
                    </a>
                )
            }
            cover={
                <img alt={coverImg && coverImg.alt}
                    src={coverImg && coverImg.src}
                    style={coverImg && coverImg.style}
                    className={coverImg && coverImg.className} />
            }
            bordered={bordered}
            hoverable={hoverable}
            size={size}
            title={title}
            onClick={(e) => setProps({ nClicks: nClicks + 1 })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }>
            {children}
        </Card>
    );
}

export default AntdCard;

AntdCard.defaultProps = defaultProps;
AntdCard.propTypes = propTypes;