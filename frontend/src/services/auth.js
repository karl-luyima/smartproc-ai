export const login = (email, password) => {
  if (email && password) {
    localStorage.setItem("token", "demo-token");
    return true;
  }
  return false;
};

export const logout = () => {
  localStorage.removeItem("token");
};

export const isAuthenticated = () => {
  return !!localStorage.getItem("token");
};