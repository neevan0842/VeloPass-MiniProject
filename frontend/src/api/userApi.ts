import { apiAuthenticated, apiUnauthenticated } from "./api.js";

const loginUser = async (credentials: {
  username: string;
  password: string;
}) => {
  console.log(credentials);
  try {
    const params = new URLSearchParams();
    for (const key in credentials) {
      params.append(key, credentials[key as keyof typeof credentials]);
    }

    const response = await apiUnauthenticated.post(`/auth/token`, params, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Login error:", error);
    throw error;
  }
};

const registerUser = async (userData: {
  username: string;
  email: string;
  password: string;
}) => {
  console.log(userData);
  try {
    await apiUnauthenticated.post(`/auth/register`, userData);
  } catch (error) {
    console.error("Registration error:", error);
    throw error;
  }
};

const fetchUserProfile = async () => {
  try {
    const response = await apiAuthenticated.get(`/user/me`);
    return response.data;
  } catch (error) {
    console.error("Fetch user profile error:", error);
    throw error;
  }
};

export { loginUser, registerUser, fetchUserProfile };
