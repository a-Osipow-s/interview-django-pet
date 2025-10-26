<template>
  <n-card class="footer-card" :bordered="false">
    <div class="footer-container">
      <n-text depth="3" class="footer-text">
        © {{ new Date().getFullYear() }} ArticleAtlas
      </n-text>

      <n-button type="primary" size="small" @click="scrollToTop">
        Scroll to Top
      </n-button>
    </div>
  </n-card>
</template>

<script setup>
const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}
</script>

<style scoped>
.footer-card {
  padding: 12px 24px;
  background-color: var(--n-color);
  box-shadow: var(--n-box-shadow);
  position: sticky;
  bottom: 0;
  z-index: 10;
}

.footer-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-text {
  font-size: 0.9rem;
}
</style>
