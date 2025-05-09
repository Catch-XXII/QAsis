// File: src/components/DataTableComponent.vue
<template>
  <v-fade-transition>
    <v-data-table-server
      v-show="headers.length && !loading"
      :headers="headers"
      :items="serverItems"
      :items-per-page="itemsPerPage"
      :items-length="totalItems"
      :loading="loading"
      show-select
      hover
      item-value="id"
      @update:options="$emit('update:options', $event)"
      @update:items-per-page="$emit('update:items-per-page', $event)"
    >
      <template #loader="{ isActive }">
        <v-progress-linear
          :active="isActive"
          indeterminate
          color="primary"
          height="4"
        />
      </template>

      <template #loading>
        <v-skeleton-loader :type="`table-row@${itemsPerPage || 5}`" />
      </template>
    </v-data-table-server>
  </v-fade-transition>
</template>

<script setup>
defineProps({
  headers: Array,
  serverItems: Array,
  totalItems: Number,
  loading: Boolean,
  itemsPerPage: Number,
});
</script>
