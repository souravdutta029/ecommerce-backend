import { useState } from "react";
import axios from "axios";
import config from "../utils/config";

function useApi() {
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const callApi = async ({url, method="GET", body={}, headers={}, params={}}) => {
        let gUrl = config.API_URL+url;
        setLoading(true);
        let response = null;
        headers['Authorization'] = localStorage.getItem('token')?`Bearer ${localStorage.getItem('token')}`:"";
        try {
            response = await axios.request({
                url:gUrl,
                method:method,
                data:body,
                headers:headers,
                params:params
            });
        } catch (err) {
            setError(err);
        }
        setLoading(false);
        return response;
    };

    return {callApi, error, loading}
}

export default useApi