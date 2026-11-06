export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname === "www.danodonnell.net") {
      url.protocol = "https:";
      url.hostname = "danodonnell.net";
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname === "/index.html") {
      url.pathname = "/";
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname.endsWith("/index.html")) {
      url.pathname = url.pathname.slice(0, -"index.html".length);
      return Response.redirect(url.toString(), 301);
    }

    return env.ASSETS.fetch(request);
  }
};
