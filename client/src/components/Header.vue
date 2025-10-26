<template>
  <n-card class="header-card" :bordered="false">
    <div class="header-container">
      <div class="header-left">
        <n-text class="app-title">ArticleAtlas</n-text>
      </div>

      <div class="header-right">
        <n-text class="username">{{ username }}</n-text>
        <LoginModal />
      </div>
    </div>
  </n-card>
</template>

<script setup>
import { defineProps } from 'vue'
import LoginModal from './LoginModal.vue';

defineProps({
  username: {
    type: String,
    default: 'Guest User'
  },
})

</script>

<style scoped>
.header-card {
  padding: 12px 24px;
  background-color: var(--n-color);
  box-shadow: var(--n-box-shadow);
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left .app-title {
  font-size: 1.2rem;
  font-weight: 600;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.username {
  font-weight: 500;
}
</style>
