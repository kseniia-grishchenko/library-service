import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const getRequest = (uri, params = {}) => {
  return axios
    .get(uri, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access')}` },
      params
    })
    .then((response) => response);
};

const getRequestUnautorized = (uri, params = {}) => {
  axios
    .get(uri, {
      params
    })
    .then((response) => {
      return response;
    });
};

const postRequestUnauthorized = async (uri, payload = {}) => {
  await axios.post(uri, payload, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
};

const postRequest = async (uri, payload = {}) => {
  return axios
    .post(uri, payload, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`,
        'Content-Type': 'application/json'
      }
    })
    .then((response) => response);
};

const putRequest = async (uri, payload = {}) => {
  return axios
    .put(uri, payload, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`,
        'Content-Type': 'application/json'
      }
    })
    .then((response) => response);
};

const patchRequest = async (uri, payload = {}) => {
  return axios
    .patch(uri, payload, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`,
        'Content-Type': 'application/json'
      }
    })
    .then((response) => response);
};

const patchRequestWithFormData = async (uri, formData) => {
  return axios
    .patch(uri, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }
    })
    .then((response) => response);
};

const deleteRequest = async (uri) => {
  return axios
    .delete(uri, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`,
        'Content-Type': 'application/json'
      }
    })
    .then((response) => response);
};

export {
  getRequest,
  getRequestUnautorized,
  postRequest,
  postRequestUnauthorized,
  putRequest,
  patchRequest,
  patchRequestWithFormData,
  deleteRequest
};
