"""Wrap the page bodies in src/ with the shared head, header and footer.

Run `python3 build.py` after editing anything in src/; it rewrites the four
index.html files. The pages are plain static HTML served by GitHub Pages.
"""
from pathlib import Path

ROOT = Path(__file__).parent
UPDATED = "21 September 2026"
UPDATED_TR = "21 Eylül 2026"
EMAIL = "info.live2a100@gmail.com"

PAGES = [
    # (source, output dir, depth, title, description, nav key)
    ("home.html", "", 0, "livetoahundred",
     "livetoahundred: research-based health and longevity posts. Privacy policy, data deletion and terms.", "home"),
    ("privacy.html", "privacy", 1, "Privacy Policy · livetoahundred",
     "How livetoahundred and its publishing app handle data.", "privacy"),
    ("data-deletion.html", "data-deletion", 1, "Data Deletion · livetoahundred",
     "How to ask livetoahundred to delete data, and how to remove the app's access.", "data-deletion"),
    ("terms.html", "terms", 1, "Terms of Service · livetoahundred",
     "Terms for livetoahundred's content, website and publishing app.", "terms"),
]

NAV = [("privacy", "Privacy"), ("data-deletion", "Data deletion"), ("terms", "Terms")]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="color-scheme" content="light dark">
<link rel="icon" type="image/png" sizes="32x32" href="{up}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<header class="site">
  <div class="inner">
    <a class="brand" href="{home}"><img src="{up}assets/logo-192.png" alt="" width="44" height="44"><span>livetoahundred</span></a>
    <nav aria-label="Site">{nav}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="inner">
    <p>livetoahundred · <a href="mailto:{email}">{email}</a> · <a href="https://www.instagram.com/livetoahundred/">Instagram</a></p>
    <p>Last updated {updated} · Son güncelleme {updated_tr}</p>
  </div>
</footer>
</body>
</html>
"""


def main() -> None:
    for src, out, depth, title, description, key in PAGES:
        up = "../" * depth
        current = ' aria-current="page"'
        nav = " ".join(
            f'<a href="{up}{slug}/"{current if slug == key else ""}>{label}</a>'
            for slug, label in NAV)
        body = (ROOT / "src" / src).read_text(encoding="utf-8").strip()
        body = body.replace("{email}", EMAIL).replace("{updated}", UPDATED).replace("{updated_tr}", UPDATED_TR)
        html = TEMPLATE.format(title=title, description=description, up=up, home=up or "./",
                               nav=nav, body=body, email=EMAIL, updated=UPDATED, updated_tr=UPDATED_TR)
        target = ROOT / out / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print("wrote", target.relative_to(ROOT))


if __name__ == "__main__":
    main()
