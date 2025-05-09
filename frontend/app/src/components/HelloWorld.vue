// File: src/views/HelloWorld.vue
<template>
  <v-container fluid class="fill-height px-4">
    <v-row>
      <v-col cols="12">
        <TableView
          :fetch-function="fetchArtists"
          tableName="Artist"
          count="1"
          prependIcon="mdi-account-music"
        />
        <TableView
          :fetch-function="fetchAlbums"
          tableName="Albums"
          count="2"
          prependIcon="mdi-album"
        />
        <TableView
          :fetch-function="fetchCustomers"
          tableName="Customers"
          count="3"
          prependIcon="mdi-account"
        />
        <TableView
          :fetch-function="fetchEmployees"
          tableName="Employees"
          count="4"
          prependIcon="mdi-account-tie"
        />
        <TableView
          :fetch-function="fetchGenres"
          tableName="Genres"
          count="5"
          prependIcon="mdi-music-note"
        />
        <TableView
          :fetch-function="fetchInvoices"
          tableName="Invoices"
          count="6"
          prependIcon="mdi-file-document-outline"
        />
        <TableView
          :fetch-function="fetchInvoiceLines"
          tableName="Invoice Lines"
          count="7"
          prependIcon="mdi-playlist-music"
        />
        <TableView
          :fetch-function="fetchMediaTypes"
          tableName="Media Types"
          count="8"
          prependIcon="mdi-disc"
        />
        <TableView
          :fetch-function="fetchPlaylists"
          tableName="Playlists"
          count="9"
          prependIcon="mdi-playlist-play"
        />
        <TableView
          :fetch-function="fetchPlaylistTracks"
          tableName="Playlist Tracks"
          count="10"
          prependIcon="mdi-music-box-multiple"
        />
        <TableView
          :fetch-function="fetchTracks"
          tableName="Tracks"
          count="11"
          prependIcon="mdi-music"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import TableView from "@/views/TableView.vue";
import {
  fetchCustomers,
  fetchArtists,
  fetchAlbums,
  fetchEmployees,
  fetchGenres,
  fetchInvoices,
  fetchInvoiceLines,
  fetchMediaTypes,
  fetchPlaylists,
  fetchPlaylistTracks,
  fetchTracks,
} from "@/api/fetchEndpoints.js";
</script>
