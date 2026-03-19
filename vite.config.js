import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        privacy: resolve(__dirname, 'privacy.html'),
        terms: resolve(__dirname, 'terms.html'),
        support: resolve(__dirname, 'support.html'),
        upgrade: resolve(__dirname, 'upgrade.html'),
        'checkout-success': resolve(__dirname, 'checkout/success.html'),
        'checkout-cancel': resolve(__dirname, 'checkout/cancel.html'),
      },
    },
  },
});
