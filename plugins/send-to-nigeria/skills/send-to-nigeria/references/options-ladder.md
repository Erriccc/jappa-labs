# The options ladder: US to Nigeria

Research date: **28 Nov 2026**. Prices change, so re-check live before quoting (see [recheck-live.md](recheck-live.md)). Full per-provider figures and URLs are in [price-baseline.md](price-baseline.md).

**Labels:**
- **[fetched]**: the page was read.
- **[decoded]**: text extracted from a PDF.
- **[snippet]**: search summary only; the page was not read.
- **[secondary]**: a third-party site, not the provider.
- **[inference]**: a reading of the research, not a test.

Nothing here was tested at a live checkout.

Research behind this file:
- options ladder and landed cost vs buying in Lagos: https://github.com/Erriccc/jappa-labs/issues/12
- sending rules and bag allowances: https://github.com/Erriccc/jappa-labs/issues/16
- closures: https://github.com/Erriccc/jappa-labs/issues/17

## Quick guide: which route usually wins

| Item type | Usually wins | Usually loses |
|---|---|---|
| Bulky, low-value (air fryer, big box, appliance) | Traveller app, or a relative with spare bag allowance | Forwarders that bill dimensional weight |
| Phone or laptop | Nigerian forwarder with a flat all-in rate, duty included | Traveller apps (percentage reward on a high price) |
| Light items (shoes, clothes, small goods) | Forwarder (about $20–30) or a traveller; about even | Express couriers |
| Large volume, not urgent (household goods) | Sea or barrel via a forwarder | Air |
| Urgent, small | Express courier (DHL, FedEx, UPS) | (price) |
| Prohibited, blocked or over-expensive to land | Buy locally | Every shipping route |

---

## 1. A relative or friend carries it in their bag

**Typical cost:** free if it fits in their spare allowance. Otherwise an extra bag costs about $100 or more, depending on airline and fare.

Economy checked-bag rules, US to Lagos:

| Airline | Free 23 kg bags | Extra bag | Label |
|---|---|---|---|
| Delta | Delta Main Basic: 1st bag $75. Delta Main and above: 2nd bag $100. Delta Main 1st-bag fee: unsourced | $100 (2nd bag, Delta Main) | [fetched] https://www.delta.com/us/en/baggage/checked-baggage/previous-baggage-fees. This is Delta's previous-fees page, and Delta doesn't confirm these fees are current. **Check the fee at booking** |
| United | Standard: 1 free, 2nd about $100. Basic: about $75 / $100 | $200 per bag beyond that | [snippet] URL not recorded |
| Turkish | EcoFly 0, ExtraFly 1, FlexFly 2 | $120–295 | [snippet] URL not recorded |
| Ethiopian | 2 (general rule; no US–Lagos row found) | about $225 | [snippet] URL not recorded |
| Qatar | Classic and above: 2. Lite: 1 | $75–345. Extra bag up to 23 kg USD 255; up to 32 kg USD 345 | [snippet] of https://www.qatarairways.com/en/baggage/excess.html (direct fetch returned 403) |
| Emirates | Special: 1. Saver and above: 2 | about $200 at the airport, about $100 prepaid online | [snippet] URL not recorded |

- **Overweight bags (Delta and United):** 51–70 lb $100; 71–100 lb $200 [snippet; URL not recorded; not confirmed for Lagos].
- **Delta and Nigeria:** Nigeria is carved out of the free first bag that the rest of Africa gets on every fare [fetched, delta.com, same page as above].
- **Nonstop flights to Lagos:** Delta ATL–LOS, Delta JFK–LOS and United IAD–LOS (US BTS T-100 data, Dec 2024 and Dec 2025).

**Duty:** the $300 duty-free limit also applies to passenger baggage (see [nigeria-duty.md](nigeria-duty.md)). An $800 phone is over the limit even in a suitcase.

**Wins:** bulky, low-value goods when the relative already has a spare free bag.
**Loses:** when it means buying an extra bag ($100+) for a small item that a forwarder would ship for $20–30.
**Never:** for packages from strangers (see [prohibited-and-carry-warnings.md](prohibited-and-carry-warnings.md)).

## 2. Amazon ships direct (AmazonGlobal)

**Typical cost:** shipping about **$10–40**, 7–21 business days, plus an **import-fees deposit** [fetched, Getcleva, Apr 2026] https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work .
- Nigeria is listed for AmazonGlobal [snippet].
- Deposit rules: if the actual fees come in lower, the difference is refunded. You're never charged more. If no invoice arrives within 180 days, the whole deposit is refunded.
- Eligibility is decided per item. Electronics, some brands and US-only third-party sellers are often blocked (Getcleva, Apr 2026) [fetched]: https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work
- Phones are likely blocked [inference, not tested].
- Amazon often declines naira cards (see [paying-from-nigeria.md](paying-from-nigeria.md)).

**Wins:** eligible, light, non-electronic items when the shopper wants one checkout and no surprise fees.
**Loses:** blocked items (often electronics and phones), and anything a flat-rate forwarder ships for less.

## 3. Nigerian forwarders (US address to a Nigeria door, duty often included)

You buy from any US store and ship to the forwarder's US warehouse. It flies the goods to Nigeria, and many forwarders include Lagos customs clearance.

**Typical cost:** air to Lagos about **$3.50–5.80/lb**, and about **$7.85/lb to other states** (naijatipsland, 2 Nov 2026) [fetched, https://naijatipsland.com/ship-from-usa-to-nigeria/]. Examples:
- **BigShipment /NG:** new phone $70, laptop $80, **duty, VAT and clearing included** [fetched; page undated] https://bigshipment.ng/NG/freight-shipping .
- **BigShipment, Topship, SGK Global, Hont, Cargo Naija and others:** per-lb rates, minimums (BigShipment's page gives two that conflict) and duty treatment are in [price-baseline.md](price-baseline.md).

**Sea and barrels:** much cheaper per pound, but slow (SGK barrels from Stafford TX, Hont sea from Houston; figures in [price-baseline.md](price-baseline.md)).

**Wins:** phones and laptops (a flat all-in rate with duty included), light items ($20–30), and big non-urgent loads by sea.
**Loses:** bulky, light items, because of dimensional weight. A 10 lb air fryer in an 18.9 lb (dimensional) box costs about $45 by actual weight but **about $85** by dimensional weight at BigShipment [fetched, page undated] https://bigshipment.ng/NG/freight-shipping . Destinations outside Lagos also cost more.

## 4. Traveller apps (a traveller brings your item in their luggage)

**Typical cost:** a reward to the traveller, usually a percentage of the item price.
- **Grabr, iShopUship and Pikkah:** fees, labels and URLs are in [price-baseline.md](price-baseline.md). Grabr's own pages disagree (10–20% vs 15–25%), so the tables below use the combined 10–25% range; its platform fee is unknown. Pikkah's only fee figure comes from a competitor.
- **Qrrier:** reward plus 15%, with escrow [snippet; URL not recorded].
- **Carryam4me:** UK route only (from £28 up to 3 kg, all in). The page showed a pre-launch band, so it may not be live yet [fetched].
- **Never carry or send a sealed package for a stranger**, and remember a traveller is personally liable for what they carry: see [prohibited-and-carry-warnings.md](prohibited-and-carry-warnings.md).
- **Shypmate:** appears to be closed (Crunchbase lists it as "Envyl / Closed": https://www.crunchbase.com/organization/shypmate).

Traveller (at the Grabr range) vs the cheapest forwarder:

| Item | Traveller | Forwarder | Verdict |
|---|---|---|---|
| Sneakers, 3 lb, $120 | $12–30 | $20–30 | About even |
| Phone, 1 lb, $800 | $80–200 | $70 all-in (BigShipment /NG [fetched] https://bigshipment.ng/NG/freight-shipping ) | **Traveller loses.** The phone is also over the $300 limit, even in baggage |
| Air fryer, 10 lb, $100 | $10–25 | $81–85 (MyUS Budget $81.06 [snippet] https://www.myus.com/ng/ ; BigShipment /NG ~$85 dimensional [fetched] https://bigshipment.ng/NG/freight-shipping ) | **Traveller saves about $56–75** |

**Wins:** bulky, low-value goods.
**Loses:** phones and other high-value items, where a percentage reward costs more than a flat forwarder rate.

## 5. Global forwarders (MyUS, Shipito, Stackry, Planet Express, Aramex Shop & Ship)

These give you a US address and ship worldwide by your choice of carrier.

**Typical cost:**
- **MyUS** by speed tier, and the Shipito, Stackry and Planet Express fees: see [price-baseline.md](price-baseline.md). The MyUS Budget 5 and 10 lb figures are corroborated by naijatipsland (2 Nov 2026) [fetched, https://naijatipsland.com/ship-from-usa-to-nigeria/].
- **Shipito:** 1 lb from about $10; processing $3.25 [snippet; URL not recorded].
- **Aramex Shop & Ship:** no published Nigeria rate (calculator only). It takes naira payment and charges on gross weight.
- **Duty is not included.** It is collected separately.

**Wins:** buying from several stores and consolidating; choosing a speed tier; billing by actual weight (the air fryer is about $81 at MyUS Budget [snippet] https://www.myus.com/ng/ , against about $85 by dimensional weight at BigShipment [fetched] https://bigshipment.ng/NG/freight-shipping ).
**Loses:** phones and electronics. Shipping is cheap (MyUS 1 lb $17 [snippet] https://www.myus.com/ng/ ), but duty and VAT come on top: at least $60–220 on an $800 phone, a floor, not a total (see [nigeria-duty.md](nigeria-duty.md)).

## 6. DHL and other express couriers

**Typical cost:**
- **DHL, FedEx and UPS through MyUS**, and **USPS Priority Mail International** (Nigeria is Price Group 9): see [price-baseline.md](price-baseline.md). USPS bills in whole-pound steps, so a 1.5 lb parcel pays the 2 lb price.
- **DHL Express quote via Easyship:** $66.70 (weight not given). Other estimates: $100–150 [snippet; URL not recorded].
- **DHL fuel surcharge:** 46–48% in Oct 2026 [snippet; URL not recorded].

**Wins:** urgent, small shipments where speed matters more than price (Aramex 3–5 days via MyUS).
**Loses:** on price, for almost everything else.

## 7. Buy locally in Nigeria

**Typical cost:** the local price. The research found **no reliable, like-for-like Nigerian price**: the Jumia listings checked were stale or not reproducible, so none are quoted here.

To compare, fetch the live local listing (for example on Jumia) and set it against the landed cost of importing:

> US price + shipping + duty/VAT (if over $300) + card and FX fees

US reference prices (apple.com, fetched 28 Nov 2026):
- **iPhone 17:** from $899 with carrier activation; unlocked 256 GB $929; 512 GB $1,129 [fetched] https://www.apple.com/shop/buy-iphone/iphone-17 .
- **MacBook Air:** Apple's MacBook Air page now lists only M5 models, so there is no live M4 price.

**Wins:** when the item is prohibited, blocked or restricted; when the landed import cost is close to the local price; or when it's needed now.
**Loses:** when local prices carry a large markup. Resale guides describe Instagram sellers pricing above market [snippet; URL not recorded], but there is no published markup data for this corridor.

---

## Worked examples

The worked examples (sneakers, phone, air fryer) are costed route by route in the "Routes from any US city" tables of [size-classes.md](size-classes.md), classes 1, 3 and 4.

**Caveats:**
- Amazon eligibility is untested.
- MyUS figures are snippets.
- Neither BigShipment page is dated.
- Phone duty is unconfirmed.
- Grabr's own pages disagree on its reward range.
- The sneakers rows assume footwear clears; see the prohibition note in [prohibited-and-carry-warnings.md](prohibited-and-carry-warnings.md).
