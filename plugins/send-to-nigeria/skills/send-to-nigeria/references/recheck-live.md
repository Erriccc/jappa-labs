# How to re-check live before quoting

The figures in this skill come from research on **28 Nov 2026**. Before you quote a price to a user, re-check the providers you are recommending.

## Procedure

1. **Shortlist two or three providers** for the user's item and city. Use [options-ladder.md](options-ladder.md) and the matching file in [scenarios/](scenarios/README.md).
2. **Fetch each provider's live page** with `WebFetch`, using the URLs below. Ask for the specific figure, for example:
   - `WebFetch(url="https://sgkglobal.com/shipping-from-texas-to-nigeria/", prompt="Per-lb air rate to Lagos, minimum charge, beyond-Lagos rate, and any date on the page")`
3. **If the fetch fails** (timeout, 403, 404, or a JavaScript-only page), use `WebSearch`:
   - `WebSearch(query="<provider> US to Nigeria rate per lb 2026")`
   - Label anything you get this way **[snippet]**.
4. **If neither works**, quote the baseline figure from [price-baseline.md](price-baseline.md). Label it **"[baseline, as of 28 Nov 2026], not re-checked today"**.
5. **Compare.** If a live figure differs from the baseline, use the live one and mention the change.

## Labelling rules for every figure you give

- **[fetched today]**: you read the page in this session. Include the URL and today's date.
- **[snippet]**: the figure comes from a search result summary only. Say it is unverified.
- **[baseline, as of 28 Nov 2026]**: the figure comes from this skill's files. Carry over the original label too: [fetched], [snippet], [decoded], [stale] or [unverified].
- **Always state the as-of date**, plus the page's own date if it shows one.
- **If a page is undated, say so.**
- If sources disagree (for example, Hont's live FAQ and its April PDF), give the newer one and mention the conflict.

## Pages to re-check

For each shortlisted provider, fetch the Source URL given next to its figure in [price-baseline.md](price-baseline.md) (or in the file that quotes it). The table below adds the pages that need a particular tool, have a known problem, or are not cited elsewhere.

| Provider / topic | URL | Tool | Known issues |
|---|---|---|---|
| SGK Chicago | https://sgkglobal.com/shipping-from-chicago-to-nigeria | WebFetch | Pickup fee not stated |
| SGK Baltimore | (page returned 404) | WebSearch | No Baltimore sailing found |
| Hont live FAQ | https://www.hontglobal.com/faq/ | WebFetch | Newer than the PDF |
| Hont rate PDF | https://www.hontglobal.com/wp-content/uploads/2026/04/Hont-Global-Services-Shipping-Details-_April-2026.pdf | WebFetch | Binary PDF; may not decode. Also look for a newer PDF |
| Topship Shop & Ship | https://topship.africa/shop-&-ship | WebFetch, then WebSearch | JS-rendered; needs a headless browser |
| Cargo Naija | https://cargonaija.com/air-freight-from-usa-to-nigeria/ | WebFetch | Ignore any older $3.50 sea figure; it is not on the live page |
| FCEL / Dechaser (Atlanta) | https://dechaser.com/fcel-rate-card-atlanta-georgia-to-nigeria-2026/ | WebFetch | Last updated 20 Jan 2026 |
| Cargo2Lagos | https://www.cargo2lagos.com/ | WebFetch | Undated |
| Hezelinks Atlanta | https://hezelinks.com/air-freight-cargo-shipping-from-atlanta-usa-to-nigeria/ | WebFetch | Units inconsistent |
| Hezelinks Maryland | https://hezelinks.com/air-freight-shipping-to-nigeria-from-maryland/ | WebFetch | Units inconsistent |
| County Cargo | https://countycargo.com/shipping-barrels-from-the-usa-to-nigeria | WebFetch | Snippet only so far |
| Icon Logistics (MD) | https://iconshipping.com/barrel-shipping ; https://iconshipping.com/west-africa-consolidation ; https://iconshipping.com/ship-from-baltimore | WebFetch | No prices published; quote only |
| MyUS Nigeria rates | https://www.myus.com/ng/ | WebFetch, then WebSearch | Timed out in research |
| Stackry | https://stackry.com/faq | WebFetch | Nigeria rate calculator only |
| USPS international prices | https://pe.usps.com/text/dmm300/notice123.htm | WebFetch | Nigeria = Price Group 9 (9th value; first column is Canada) |
| Amazon to Nigeria (guide) | https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work | WebFetch | Third party |
| Amazon import-fees deposit | https://www.amazon.com/gp/help/customer/display.html?nodeId=TLSm47vnDszgnXnq6J | WebFetch, then WebSearch | Returned 503; figures are [snippet] |
| $300 duty-free rule | https://www.premiumtimesng.com/business/business-news/819441-customs-board-approves-300-duty-free-limit.html (NAN reprint) ; https://businessday.ng/maritime/article/how-nigerias-300-duty-free-rule-affects-online-shoppers-international-travellers/ | WebFetch | The original NAN page returned 404 |
| BigShipment /NG and /USA | https://bigshipment.ng/NG/freight-shipping ; https://bigshipment.ng/USA/freight-shipping | WebFetch | Undated. The /NG page has both "$30 under 6 lb" and "$20 under 5 lb" |
| Delta bags to Nigeria | https://www.delta.com/us/en/baggage/checked-baggage/previous-baggage-fees | WebFetch, then Delta's baggage calculator | Previous-fees page; Delta doesn't confirm it is current. Tell users to check at booking |
| Grabr | https://collections.grabr.io/en ; https://help.grabr.io/hc/en-us/articles/115001499513-How-can-I-edit-the-traveler-reward | WebFetch, then WebSearch | Grabr help pages returned 403 and conflict with its own 10–20% |
| Qatar excess baggage | https://www.qatarairways.com/en/baggage/excess.html | WebFetch, then WebSearch | Returned 403 |
| Carryam4me (UK only) | https://carryam4me.com/ | WebFetch | Pre-launch band |
| GIG Logistics | https://giglogistics.com/shipping-price-calculator/ | — | Interactive calculator only; no rate table |
| Apple US prices | https://www.apple.com/shop/buy-iphone/iphone-17 ; https://www.apple.com/shop/buy-mac/macbook-air | WebFetch | For landed-cost comparisons |

## Pages with no recorded URL (find with WebSearch first)

| Topic | Suggested search |
|---|---|
| United, Turkish, Ethiopian, Emirates bags | `WebSearch(query="<airline> baggage allowance US to Lagos economy")` |
| Qrrier's own fee | `WebSearch(query="Qrrier traveller reward fee Nigeria")` |
| Nigerian bank card limits | `WebSearch(query="Nairametrics bank foreign spend limit naira card 2026")` |
| DHL Express US to Nigeria | `WebSearch(query="DHL Express US to Nigeria price 1 kg 2026")` |
| JOBOX, GIG, Splendid, BuyandShip | `WebSearch(query="<provider> US to Nigeria rate per lb")` |
| Local price in Nigeria | `WebFetch` a live Jumia listing for the exact model; note the seller and the page date |

## Things not to do

- Don't quote a figure as current without a label and a date.
- Don't fill a gap with an estimate. Say "no published rate found; ask for a quote".
- Don't treat a provider's "as low as" marketing as the price the user will pay.
