# 5.3 Cyber security — practice

Cambridge IGCSE (9–1) Computer Science 0984 · points 5.3.1–5.3.2 · Paper 1

No past papers are stored in `me/papers/Computer_Science_0984/` yet. The marking guidance below
is written for this repository and is **not an official Cambridge mark scheme**.

## Questions

1. Describe the process and the aim of a brute-force attack. **[3]**
2. Describe how a DDoS attack is carried out and what it aims to do. **[4]**
3. Explain the difference between phishing and pharming. **[4]**
4. Describe **two** differences between a virus and a worm. **[4]**
5. Identify the type of malware described: (a) encrypts the user's files and demands payment;
   (b) records key presses and sends them to a third party; (c) is disguised as a useful program;
   (d) floods the user with pop-up adverts. **[4]**
6. Describe what is meant by social engineering, giving **one** example. **[3]**
7. Explain how a firewall helps keep data safe. **[3]**
8. Explain how a proxy server can help protect a company's web server. **[3]**
9. A bank uses two-step verification for online banking. Explain how two-step verification helps
   keep customers' accounts safe. **[3]**
10. Describe the process of SSL when a browser connects to a secure website. **[5]**
11. A student receives an email that appears to be from their bank asking them to log in. Explain
    **two** checks the student could make before clicking the link. **[4]**
12. A company is worried about data interception and hacking. Explain **three** solutions it could
    use, and how each one keeps its data safe. **[6]**

## Marking guidance

1. Tries every possible combination of characters (1); often starts with common passwords / a word
   list (1); aim: find the password to gain unauthorised access (1).
2. Attacker uses many (infected) computers (1) to send huge numbers of requests (1) to a web server
   at the same time, overloading it (1); aim: server cannot respond to genuine users / website made
   unavailable (1).
3. Phishing: legitimate-looking email/message (1) with link to fake site or request for details —
   user must click/reply (1). Pharming: malicious code on computer / DNS server (1) redirects the
   browser to a fake site even when the correct URL is typed — no user action needed (1).
4. Any two pairs (2 each): virus needs a host program, worm is stand-alone; virus must be run by the
   user, worm spreads by itself; virus aims to corrupt/delete files, worm aims to spread through a
   network / use bandwidth.
5. (a) ransomware (b) spyware (c) Trojan horse (d) adware — 1 each.
6. Manipulating people (1) into breaking normal security procedures / revealing information by
   exploiting fear, curiosity or trust (1); example e.g. fake IT-support phone call, infected USB
   stick left to be found, fake virus pop-up (1).
7. Sits between the computer/network and the internet (1); checks all incoming and outgoing traffic
   against set rules (1); blocks traffic that fails, e.g. from blocked IP addresses, keeping hackers
   and malware out (1). Also credit: logs traffic / warns user.
8. Acts as an intermediary between users and the web server (1); filters requests, blocking invalid
   ones (1); attacks such as DDoS hit the proxy rather than the web server (1); hides IP addresses (1).
9. Two different methods of authentication are needed (1), e.g. password then one-time code sent to
   the registered phone (1); a criminal who knows / has stolen the password still cannot log in
   without the phone (1).
10. One mark per step, max 5: browser requests connection to the secure website; browser asks the
    server to identify itself; server sends a copy of its SSL certificate; browser checks the
    certificate is authentic; browser sends message to begin communication; server acknowledges and
    encrypted data transfer begins.
11. Two checks, 2 marks each (check + reason): check spelling / grammar / tone — mistakes, generic
    greeting or urgent tone suggest phishing; check the URL behind the link (hover) — misspelt or
    different domain / no https suggests a fake site; check the sender's email address matches the
    bank's domain.
12. Three solutions, 2 marks each (solution + how it keeps data safe), e.g. SSL / HTTPS — encrypts
    data so intercepted data is unreadable; firewall — blocks unauthorised incoming traffic;
    strong passwords with attempt limit / two-step verification — prevents unauthorised access;
    access levels — limits what each user can reach; automatic updates — patches security
    weaknesses; proxy server — hides IP addresses / filters traffic.
