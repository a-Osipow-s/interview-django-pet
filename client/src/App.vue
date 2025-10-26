<script setup>
import { NConfigProvider, NMessageProvider, NDialogProvider } from 'naive-ui'
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Main from './components/Main.vue';
</script>

<template>
  <n-config-provider>
    <n-message-provider>
      <n-dialog-provider>
        <Header />
        <Main />
        <Footer />
      </n-dialog-provider>
    </n-message-provider>
  </n-config-provider>
</template>

