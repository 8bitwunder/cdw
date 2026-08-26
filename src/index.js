export default {
  async fetch(request, env) {
    const response = await env.ASSETS.fetch(request);
    const contentType = response.headers.get("content-type") || "";

    if (!contentType.includes("text/html")) {
      return response;
    }

    let html = await response.text();

    html = html
      .replace(
        "Canberra, ACT &middot; 2026",
        "Canberra, ACT &middot; 28 SEP - 2 OCT 2026"
      )
      .replace(
        '<div class="stat-card"><div class="stat-card__num">1</div><div class="stat-card__label">Week-long festival</div></div>',
        '<div class="stat-card"><div class="stat-card__num">5</div><div class="stat-card__label">Days &middot; Citywide data festival</div></div>'
      )
      .replace(
        "A diverse program of free events across a full week. Browse the types of events you can attend, or apply to run your own as a partner host.",
        "28 September - 2 October 2026. A diverse program of free events across five days. Browse the types of events you can attend, or apply to run your own as a partner host."
      );

    const headers = new Headers(response.headers);
    headers.delete("content-length");

    return new Response(html, {
      status: response.status,
      statusText: response.statusText,
      headers
    });
  }
};
