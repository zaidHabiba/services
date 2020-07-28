/**
 * @return {boolean}
 */
export function FlowNumber(value) {
    return !isNaN(value);
}

/**
 * @return {boolean}
 */
export function FlowSpacePrevent(value) {
    return value ? !(value.split(" ").length > 1) : true;
}

/**
 * Tack: maxLength in flowProps
 * @return {boolean}
 */
export function FlowLength(value, { maxLength }) {
    return value ? `${value}`.length <= maxLength : true;
}