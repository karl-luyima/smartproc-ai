import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getEvaluation = (requestId) =>
  API.get(`/ai/evaluate/${requestId}`);

export default API;