import {BaseServiceClass} from "./base.service";
import Cookies from "js-cookie";

class TokenServiceClass extends BaseServiceClass {

    base = 'user';

    getToken = () => {
        return Cookies.get("token");
    };

    saveToken = (token) => {
        Cookies.set('token', token);
    };

    clearToken = () => {
        Cookies.remove('token');
    };

    isValidToken = async () => {
        if (!this.getToken()) {
            return false;
        }
        try {
            const response = await this.createRequest().post(`${this.base}/is-valid-key`, {token: this.getToken()});
            if (response.data.valid) {
                return true
            }
        } catch (e) {

        }
        return false;
    };

}

const TokenService = new TokenServiceClass();
export default TokenService;