import {API_URL} from "../settings/app.config";
import axios from 'axios';
import TokenService from "./token.service";

export class BaseServiceClass {

    endPoint = '';

    createRequest = () => {
        return axios.create({
            baseURL: API_URL
        });
    };

    createAuthRequest = () => {
        return axios.create({
            baseURL: API_URL,
            headers: {
                Authorization: `Token ${TokenService.getToken()}`
            }
        });
    };

    get = () => {
        return this.createAuthRequest().get(this.endPoint);
    };

    post = (data) => {
        return this.createAuthRequest().post(this.endPoint, data);
    };

    put = (data) => {
        return this.createAuthRequest().put(this.endPoint, data);
    };

    delete() {
        return this.createAuthRequest().delete(this.endPoint);
    }
}