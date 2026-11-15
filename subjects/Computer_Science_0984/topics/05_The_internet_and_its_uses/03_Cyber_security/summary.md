# 5.3 Cyber security — summary

Cambridge IGCSE (9–1) Computer Science 0984 · points 5.3.1–5.3.2 · Paper 1

## Threats — process → aim

- **Brute-force** — try every combination (common passwords first) → find password, get access.
- **Data interception** — packet sniffer / wireless signals copy data in transit → steal data.
- **DDoS** — many infected computers flood a web server with requests → site unavailable.
- **Hacking** — unauthorised access via security weaknesses → steal, change, delete data.
- **Phishing** — fake email/message; user clicks link or replies → personal data.
- **Pharming** — code on PC or DNS server redirects correct URL to fake site; no click → personal data.
- **Social engineering** — exploit fear, curiosity, trust (fake call, pop-up, USB stick) → information/access.
- **Malware**: **virus** (needs host + user to run; corrupts files) · **worm** (stand-alone, spreads
  through network itself) · **Trojan horse** (disguised as real software; gives access) · **spyware**
  (monitors, e.g. key logger; steals data) · **adware** (unwanted adverts) · **ransomware** (encrypts
  data; demands payment).

## Solutions

- **Access levels** — permissions per account; users see only what they need.
- **Anti-malware** — scans, compares with database of known malware, heuristic checks, quarantines;
  keep updated. Anti-spyware removes spyware/key loggers.
- **Authentication** — strong password + attempt limit; biometrics (unique, can't be guessed);
  two-step verification (password + one-time code to phone).
- **Automatic updates** — security patches installed at once.
- **Spelling/tone** — mistakes, "Dear customer", urgency → don't click or reply.
- **Check the URL** — hover; misspelt/different domain/no https → fake site.
- **Firewall** — checks all traffic in and out against rules; blocks what fails; logs, warns.
- **Proxy server** — intermediary; hides user's IP; filters requests; attacks hit the proxy.
- **Privacy settings** — limit who sees personal data.
- **SSL** — encrypts browser ↔ server data; certificate authenticates the site; request → identify →
  certificate sent → browser checks → begin → encrypted transfer.
