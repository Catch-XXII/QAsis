import axios from "axios";

// ENV'den veya sabit olarak API adresi
const BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:4141/v1";

// Token varsa storage’dan al
const getAuthToken = () => localStorage.getItem("access_token");

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use(
  (config) => {
    const token = getAuthToken();
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

export default api;
