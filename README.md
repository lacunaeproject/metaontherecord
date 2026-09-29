# Meta on the Record

A sourced, evidence-labeled record of court rulings, regulatory findings and reported events involving Meta. Researched, written, organized and built with AI (Anthropic’s Claude); the site says so on the home page, on every entry page, in the footer and in the data downloads. Keep those disclosures when you edit.

## How the folders work

You edit `src/`. The build writes the finished site to `docs/`. GitHub Pages publishes `docs/`.

| Path | What it is |
|---|---|
| `src/data.json` | Every entry, credit and note. Edit this to change content. |
| `src/home.html` | The home page’s visible content. The build adds the page head, the rendered record, the footer and scripts. |
| `src/styles.css` | All styles. |
| `src/app.js` | Filters, search, navigation and the hero animation. |
| `src/img/` | Photos used on the home page. Use only public-domain or openly licensed images, and credit each one in its caption. |
| `build.py` | Builds `docs/` from `src/`. The domain is set at the top (`BASE`). |
| `og.py` | Renders the share image for every page into `docs/og/`. |
| `docs/` | The finished site. Don’t edit it by hand; the build replaces it. |

## Update the record

```
python3 build.py
pip install playwright && python3 -m playwright install chromium   # first time only
python3 og.py
```

Run `og.py` after every build, since the build clears `docs/`. Then commit and push both `src/` and `docs/`. Update `UPDATED` in `build.py` when content changes.

## Publish on GitHub Pages

1. Create a repository and push this folder to it.
2. In the repository, go to Settings → Pages. Under “Build and deployment,” choose “Deploy from a branch,” then your main branch and the `/docs` folder.
3. In the same screen, enter `metaontherecord.org` as the custom domain. The build already writes the `CNAME` file that keeps it set.
4. At your domain registrar, point the domain to GitHub. For the bare domain, GitHub’s documentation lists four A records (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153); add a CNAME record for `www` pointing to `<your-username>.github.io`. Confirm the current values in GitHub’s “Managing a custom domain” guide before saving.
5. After DNS updates, turn on “Enforce HTTPS” in Settings → Pages.

The site needs the custom domain to work. Its links start from the root (`/assets/…`), which only resolves correctly at metaontherecord.org, not at `<username>.github.io/<repo>/`.

## Before launch

1. **Source checks are complete** as of September 28, 2026. Flag any new entry without sources with `"check": true`; it shows a “source being added” note until you link one.
2. **Recheck pending cases before each update:** appeals, the Flo damages, the second New Mexico penalty and EU decisions.
3. **Add a corrections address.** Search `Contact address coming soon` in `src/home.html` and `build.py` and replace it.
4. **Choose the data license.** The build declares the downloads as CC BY 4.0. Change it in `build.py` if you prefer something else.
5. **Get a media lawyer’s read** before sharing widely, including the use of “Meta” in the name and domain.

## Getting found

**Week one**
- **Google Search Console:** add metaontherecord.org as a Domain property, verify through DNS, submit `https://metaontherecord.org/sitemap.xml`, and request indexing for the home page and your strongest entries.
- **Bing Webmaster Tools:** import from Search Console. Bing's index also powers DuckDuckGo and several AI search tools.
- **Check the metadata:** run a few entry URLs through Google's Rich Results Test, and paste links into a social post preview to confirm the share cards appear.

**What earns visibility**
- **Links from people who cover this beat.** Send specific entries to the reporters who broke those stories, digital-rights groups (EFF, Fight for the Future, Amnesty Tech, GLAAD) and researchers. Offer the CSV. A sourced, reusable dataset is what gets linked.
- **Share single entries, not just the home page.** Every entry has its own URL, title and share image, so a post about the Flo verdict can link straight to it and rank for searches about it.
- **Post when the news moves.** Update and reshare the relevant entries when an appeal, verdict or settlement lands. Freshly updated pages on a live topic rank and spread best.
- **Keep it clean.** No paid links, link swaps or adding your own site to Wikipedia. They violate search guidelines and hand critics an easy line of attack.
