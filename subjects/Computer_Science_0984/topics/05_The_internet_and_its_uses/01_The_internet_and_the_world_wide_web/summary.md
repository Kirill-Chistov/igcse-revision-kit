# 5.1 The internet and the world wide web — summary

Cambridge IGCSE (9–1) Computer Science 0984 · points 5.1.1–5.1.6 · Paper 1

- **Internet** = the infrastructure (interconnected networks and devices). **WWW** = the websites and
  web pages accessed using the internet. Email and chat use the internet but are not the web.
- **URL** = text-based address of a web page: **protocol** (`https://`) + **domain name**
  (`www.example.org`) + **web page / file name** (`/revision/topic5.html`).
- **HTTP** = rules for transferring web pages between browser and web server: browser sends a
  **request**, server sends a **response** with the file. **HTTPS** = HTTP + **SSL encryption**;
  server proves identity with an SSL certificate; `https://` + padlock.
- **Browser**: main purpose is to **render HTML** and display web pages. Functions: address bar,
  navigation tools, multiple tabs, bookmarks/favourites, user history, storing cookies.
- **Finding a page**: URL typed → browser sends domain name to **DNS** → DNS looks up the IP address
  (asks another DNS if not found) → **IP address** returned → browser sends HTTP request to the
  **web server** → server sends **HTML** → browser renders and displays it.
- **Cookie** = small file sent by a web server, stored by the browser on the user's device, sent
  back on later visits.
  - **Session**: in RAM; deleted when the browser closes; e.g. shopping cart.
  - **Persistent**: on storage until expiry date or deleted; e.g. login details, personal details,
    user preferences.
