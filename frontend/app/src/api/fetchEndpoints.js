// api/fetchEndpoints.js
import api from "./api";

export async function fetchCustomers({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/customers", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchArtists({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/artists", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchAlbums({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/albums", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchGenres({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/genres", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchMediaTypes({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/media-types", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchPlaylists({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/playlists", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchTracks({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/tracks", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchInvoices({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/invoices", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchInvoiceLines({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/invoice-lines", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchEmployees({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/employees", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}

export async function fetchPlaylistTracks({ page = 1, itemsPerPage = 10 }) {
  const skip = (page - 1) * itemsPerPage;
  const response = await api.get("/playlist-tracks", {
    params: { skip, limit: itemsPerPage },
  });
  return response.data;
}
