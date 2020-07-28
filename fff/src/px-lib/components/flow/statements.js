export function If(props) {
    return props.flag && props.children? props.children : null;
}

