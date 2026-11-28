# Research method: filling gaps live

Use this method when the user's **US city** has no scenario file, or the destination is **another West African country** (Ghana, Senegal and others). Nigeria is the only reviewed baseline. Everything you find with this method is **"found live on <date>, not yet reviewed"**.

Write the findings into the structure of [templates/scenario-template.md](templates/scenario-template.md).

## Source trust order (best first)

1. **Official government pages:**
   - the destination country's customs service;
   - US federal sources (eCFR, USPS, CBP);
   - official gazettes.
2. **The provider's own live pages:** pricing pages, FAQs, rate-card PDFs and conditions of carriage, plus the airline's own baggage pages.
3. **Reputable news reporting that cites an official notice** (named outlet, dated article).
4. **Third-party guides, blogs and aggregators.** Use them only to find leads, then confirm on a page from tiers 1–2.
5. **Search-result snippets.** Label them [snippet]. Never treat a snippet as confirmed.

Record the URL, the page's own date (or "undated") and today's date for every figure.

## Variable 1: Origin city and distance to the nearest forwarder hub or port

- **Why it matters:** heavy goods and barrels often leave from one hub. For example, SGK's barrels go via Stafford TX, so senders elsewhere pay a first-mile leg.
- **Steps:**
  1. `WebSearch(query="ship to <COUNTRY> from <US CITY> forwarder per lb")`
  2. `WebSearch(query="<US CITY> barrel shipping to <COUNTRY>")`
  3. `WebFetch` each forwarder's city page. Ask: does it offer pickup in this city, and what does pickup cost? Where is the drop-off warehouse? Which airport or port does it ship from?
- **Record:** the pickup fee, the drop-off address, the hub, and the first-mile leg cost. If there is no figure, write "not found".

## Variable 2: Destination country and city

- **Why it matters:** rates outside the main city are often higher or unpublished (in Nigeria, beyond-Lagos rates are higher).
- **Steps:**
  1. `WebFetch` the forwarder's rate page. Ask: is there a rate for <CITY>, a surcharge outside the capital or main port city, and a doorstep or office-collection option?
  2. `WebSearch(query="<COUNTRY> domestic courier rate <CITY>")` for the last mile.

## Variable 3: The destination country's duty-free threshold and import bans

- **Never reuse Nigeria's $300 rule.** Every country sets its own rule.
- **Steps:**
  1. `WebSearch(query="<COUNTRY> customs duty free threshold personal import e-commerce")`, then `WebFetch` the customs authority's own page.
  2. `WebSearch(query="<COUNTRY> customs import prohibition list")` and `WebSearch(query="<COUNTRY> customs passenger baggage allowance")`.
  3. Check whether the rule applies per consignment or per item, how often it can be used, and whether it covers baggage.
- **If no official page can be found**, say so. Give the news source as [secondary], and don't state a threshold as fact.

## Variable 4: Which forwarders serve the corridor

- **Steps:**
  1. `WebSearch(query="US to <COUNTRY> shipping forwarder")` and `WebSearch(query="shop and ship US address <COUNTRY>")`.
  2. For global forwarders, `WebFetch` the provider's country page. MyUS uses the pattern https://www.myus.com/ng/ for Nigeria; find the equivalent for the destination country.
  3. Check whether duty is included, and how billing works (actual or dimensional weight, divisor, minimums, flat bands).
- **Watch for:** closed services. Search `"<provider> shut down"` or `"<provider> stopped shipping"` before recommending a provider you haven't seen before.

## Variable 5: Traveller routes and airline bag allowances

- **Steps:**
  1. `WebSearch(query="nonstop flights <US AIRPORT> to <DESTINATION AIRPORT>")`.
  2. `WebFetch` the airline's own baggage page. Ask: how many free checked bags in economy on the <US>–<DESTINATION> route, the extra-bag fee, and the overweight fee.
  3. `WebSearch(query="<traveller app> <COUNTRY> traveller reward fee")`.
- **Always** include the carry-for-strangers warnings ([prohibited-and-carry-warnings.md](prohibited-and-carry-warnings.md)) and the airline's own rule on third-party items.

## Variable 6: Payment options

- **Steps:**
  1. `WebSearch(query="<COUNTRY> virtual dollar card fees <YEAR>")`, then `WebFetch` the card provider's own fee page.
  2. `WebSearch(query="<COUNTRY> bank card international spend limit <YEAR>")`.
  3. Check that the card works with the store (for example, Amazon) and with the forwarder.

## Output rules

- **Label every figure:** "found live on <date>, not yet reviewed", plus [fetched] or [snippet] and the URL.
- **Keep these figures separate.** Never mix them into, or present them as part of, the reviewed Nigeria baseline.
- **Never estimate a missing figure.** Write "not found" and suggest asking for a quote.
- **Offer the user a link to contribute** what you found: https://github.com/Erriccc/jappa-labs/issues/new. **Do not file the issue yourself.**
- **This is not legal or customs advice.** Say so.
