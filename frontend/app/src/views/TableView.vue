<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  fetchFunction: Function,
  tableName: String,
  prependIcon: String,
  count: [String, Number],
});

const headers = ref([]);
const serverItems = ref([]);
const totalItems = ref(0);
const loading = ref(false);
const itemsPerPage = ref(5);
const selected = ref([]);
const options = ref({
  page: 1,
  itemsPerPage: itemsPerPage.value,
  sortBy: [],
});

watch(
  options,
  async (newOptions) => {
    if (typeof props.fetchFunction !== "function") {
      console.warn("Invalid fetch function");
      return;
    }

    try {
      loading.value = true;
      const res = await props.fetchFunction(newOptions);
      headers.value = res.headers;
      serverItems.value = res.rows;
      totalItems.value = res.total;
    } catch (e) {
      console.error("Fetch error:", e);
    } finally {
      loading.value = false;
    }
  },
  { immediate: true, deep: true },
);
</script>

<template>
  <v-sheet
    class="pa-1 mb-15"
    elevation="15"
    style="overflow-x: auto"
    color="primary"
  >
    <v-card class="py-4" :prepend-icon="prependIcon" rounded="lg">
      <template #title>
        <h2 class="text-h5 font-weight-bold">
          #{{ count }} {{ tableName }} Table
        </h2>
      </template>

      <v-data-table-server
        v-if="headers.length"
        v-model:options="options"
        v-model="selected"
        :items="serverItems"
        :headers="headers"
        :items-length="totalItems"
        :items-per-page="itemsPerPage"
        :loading="loading"
        hover
        show-select
        height="400"
        class="data-table-fixed"
        density="compact"
      >
        <template #loader="{ isActive }">
          <v-progress-linear
            :active="isActive"
            color="deep-purple"
            height="4"
            indeterminate
          />
        </template>
      </v-data-table-server>
    </v-card>
  </v-sheet>
</template>

<style>
.data-table-fixed table {
  table-layout: fixed;
  width: 100%;
}
</style>
