import axios, { AxiosInstance } from "axios";

const API_URL: string = import.meta.env.VITE_API_URL;

const token: string | null = localStorage.getItem("token");

const apiAuthenticated: AxiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    Authorization: `Bearer ${token}`,
  },
});

const apiUnauthenticated: AxiosInstance = axios.create({
  baseURL: API_URL,
});

export { apiAuthenticated, apiUnauthenticated };
