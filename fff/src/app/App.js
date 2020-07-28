import React from 'react';
import {BrowserRouter, Route} from "react-router-dom";
import {urlList} from '../settings/router';
import TokenService from "../services/token.service";

async function applicationLoaded() {
    if (!await TokenService.isValidToken()) {
        TokenService.clearToken();
    }
}


function App() {
    TokenService.saveToken('fdsfdsfdsfdsfdsfsd');
    applicationLoaded();
    return (
        <div className="page-wrapper">
            <BrowserRouter>
                {
                    urlList.map((route, index) => {
                        return <Route key={index} {...route}/>
                    })
                }
            </BrowserRouter>
        </div>
    );
}

export default App;
