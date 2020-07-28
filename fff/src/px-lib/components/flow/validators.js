export function StringValidator(value, fieldName) {
    return {valid: value ? /^[a-zA-Z]+$/.test(value) : true, msg: `${fieldName} should contain string only`};
}

export function LengthValidator(value, fieldName , {minLength, maxLength}) {
    let validLength = true;
    if (minLength && value) {
        validLength &= `${value}`.length >= minLength;
    }
    if (maxLength && value) {
        validLength &= `${value}`.length <= maxLength
    }
    return {valid: validLength, msg: `${fieldName} should be between ${minLength ? minLength: '0'} - ${maxLength ? maxLength: '999'}`};
}