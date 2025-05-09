// fetchHandlers.js
import {
  fetchAlbums,
  fetchArtists,
  fetchCustomers,
  fetchEmployees,
  fetchGenres,
  fetchInvoiceLines,
  fetchInvoices,
  fetchMediaTypes,
  fetchPlaylists,
  fetchTracks,
} from "@/api/fetchEndpoints";

export async function fetchCustomerData(options, state) {
  await fetchWrapper(fetchCustomers, options, state);
}

export async function fetchArtistData(options, state) {
  await fetchWrapper(fetchArtists, options, state);
}

export async function fetchAlbumData(options, state) {
  await fetchWrapper(fetchAlbums, options, state);
}

export async function fetchEmployeeData(options, state) {
  await fetchWrapper(fetchEmployees, options, state);
}

export async function fetchGenreData(options, state) {
  await fetchWrapper(fetchGenres, options, state);
}

export async function fetchInvoiceLineData(options, state) {
  await fetchWrapper(fetchInvoiceLines, options, state);
}

export async function fetchInvoiceData(options, state) {
  await fetchWrapper(fetchInvoices, options, state);
}

export async function fetchMediaTypeData(options, state) {
  await fetchWrapper(fetchMediaTypes, options, state);
}

export async function fetchPlaylistData(options, state) {
  await fetchWrapper(fetchPlaylists, options, state);
}

export async function fetchTrackData(options, state) {
  await fetchWrapper(fetchTracks, options, state);
}

// Genel wrapper fonksiyon
async function fetchWrapper(fn, options, state) {
  state.loading.value = true;
  try {
    const res = await fn(options);
    state.headers.value = res.headers;
    state.serverItems.value = res.rows;
    state.totalItems.value = res.total;
  } catch (e) {
    console.error(`Fetch failed for ${fn.name}`, e);
  } finally {
    state.loading.value = false;
  }
}
