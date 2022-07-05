import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter(),
		vite: {
			server: {
				hmr: {
					port: 24678,
					clientPort: 443,
					path: "/ws"
				},
				watch: {
					usePolling: true
				}
			}
		}
	}
};

export default config;
