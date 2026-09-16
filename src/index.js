import { onRequestPost as handleHostApplication } from '../functions/api/host-application.js';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === '/api/host-application') {
      if (request.method !== 'POST') {
        return new Response('Method Not Allowed', {
          status: 405,
          headers: { Allow: 'POST' }
        });
      }

      return handleHostApplication({ request });
    }

    return env.ASSETS.fetch(request);
  }
};
