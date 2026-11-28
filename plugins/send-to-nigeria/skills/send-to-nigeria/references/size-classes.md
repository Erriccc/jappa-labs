# Size classes: what is realistic, and how each is billed

Baseline **as of 28 Nov 2026**. Use this file to decide which routes to compare, then open the scenario for the sender's city in [scenarios/](scenarios/README.md).

Each class ends with a table of **routes from any US city** (online orders to a forwarder's US address, Amazon, traveller apps, USPS, a relative's bag). The city files in [scenarios/](scenarios/README.md) add only the local routes.

**Gaps.** The research recorded no "typical weight" for most classes. Where it says **not sourced**, ask the user to weigh the item, and don't assume a weight. The example weights below are the worked examples used in the research, not averages.

## How forwarders bill

- **Dimensional (volumetric) weight.** Some forwarders bill the greater of actual weight and (L x W x H in inches) / 166:
  - BigShipment (divisor 166) [fetched, https://bigshipment.ng/NG/freight-shipping, as of 28 Nov 2026];
  - Hont (L x W x H / 166 per lb) [decoded, https://www.hontglobal.com/wp-content/uploads/2026/04/Hont-Global-Services-Shipping-Details-_April-2026.pdf, Apr 2026].
- **Bulky, light items cost far more this way.** The example air fryer weighs 10 lb but bills at 18.9 lb.
- **Actual weight.** MyUS bills Nigeria rates on actual weight [snippet, https://www.myus.com/ng/, rates dated 6 Nov 2026]. Aramex Shop & Ship bills on gross weight [as of 28 Nov 2026; URL not recorded].
- **Not stated.** SGK, Cargo Naija, County Cargo and Cargo2Lagos don't state a divisor. Ask before relying on actual weight.
- **Flat rates and minimums** often decide small parcels (figures below).
- **USPS bills in whole-pound steps** [fetched, https://pe.usps.com/text/dmm300/notice123.htm, effective 4 Oct 2026].
- **Phones and laptops** may carry handling fees or flat duty-included rates (class 1 and class 2).

## 1. Envelope or phone

**Typical weight:** not sourced. The research example is a new phone, 1 lb, $800.

**Realistic routes:**
- a Nigerian forwarder with a flat phone rate;
- a global forwarder plus duty;
- an express courier or USPS;
- a traveller (but see the duty point below).

Amazon is likely blocked for phones [inference].

**Billing:**
- **Flat rates:** Hont $30 flat under 5 lb [fetched, https://www.hontglobal.com/faq/, as of 28 Nov 2026], plus a $30 handling charge on new gadgets [decoded, Hont April 2026 PDF above, may be stale].
- **Minimums:** SGK $60 [fetched, https://sgkglobal.com/shipping-from-texas-to-nigeria/, as of 28 Nov 2026]. Cargo Naija $95.80 flat under 20 lb [fetched, https://cargonaija.com/air-freight-from-usa-to-nigeria/, as of 28 Nov 2026].

**Duty:** an $800 phone is over the $300 limit, even in a traveller's bag (see [nigeria-duty.md](nigeria-duty.md)).

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| BigShipment /NG (online order to its US address) | $70 flat (new phone) | Duty, VAT and clearing included | not stated | [fetched, page undated] https://bigshipment.ng/NG/freight-shipping ; as of 28 Nov 2026 |
| MyUS Budget (online order) | 1 lb $17.25 | Plus duty/VAT, at least $60–220 on $800 (a floor, not a total; see nigeria-duty.md) | 8–14 days | [snippet] https://www.myus.com/ng/ ; rates dated 6 Nov 2026 |
| MyUS DHL Express (online order) | 1 lb $48.04 | Plus duty/VAT | — | [snippet] https://www.myus.com/ng/ ; rates dated 6 Nov 2026 |
| USPS Priority Mail International (sender posts it) | 1 lb $68.35 | Duty/VAT not included (collection method not stated) | not stated | [fetched] https://pe.usps.com/text/dmm300/notice123.htm ; effective 4 Oct 2026 |
| Topship Shop & Ship (online order) | $20/kg (1 lb = 0.45 kg); minimum charge not stated | "Incl. customs"; whether that covers duty on an $800 phone is not stated | 7–14 working days | [snippet] https://topship.africa/shop-&-ship ; as of 28 Nov 2026 |
| Traveller app (Grabr range) | $80–200 (10–25% of $800) | Still over the $300 limit in baggage | depends on trip | Grabr range: "usually 10–20%" [fetched] https://collections.grabr.io/en ; 15–25% [snippet, conflicts] https://help.grabr.io/hc/en-us/articles/115001499513-How-can-I-edit-the-traveler-reward ; as of 28 Nov 2026 |
| Amazon direct | Likely blocked for phones [inference] | Import-fees deposit if eligible | 7–21 business days | [fetched] https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work ; Apr 2026 |

## 2. Laptop

**Typical weight:** not sourced.

**Realistic routes:**
- a Nigerian forwarder with a flat laptop rate;
- a global forwarder plus duty;
- an express courier.

Amazon often blocks electronics [fetched, https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work, Apr 2026].

**Billing:**
- Hont: $30 handling on a new gadget, plus the per-lb rate; $20 if used [decoded, may be stale] https://www.hontglobal.com/wp-content/uploads/2026/04/Hont-Global-Services-Shipping-Details-_April-2026.pdf .

**Duty:** depends on value. Over $300, duty and VAT apply.

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| BigShipment /NG (online order) | $80 flat | Duty, VAT and clearing included | not stated | [fetched, page undated] https://bigshipment.ng/NG/freight-shipping ; as of 28 Nov 2026 |
| MyUS (online order) | By actual weight (laptop weight not sourced) | Plus duty/VAT if over $300 | Budget 8–14 days | [snippet] https://www.myus.com/ng/ ; rates dated 6 Nov 2026 |
| Traveller app (Grabr range) | 10–25% of the item price, $5 min | Over $300: duty applies even in baggage | depends on trip | Grabr range: "usually 10–20%" [fetched] https://collections.grabr.io/en ; 15–25% [snippet, conflicts] https://help.grabr.io/hc/en-us/articles/115001499513-How-can-I-edit-the-traveler-reward ; $5 min [snippet] https://help.grabr.io/hc/en-us/articles/115004005714-Can-you-explain-all-the-fees-I-m-seeing ; as of 28 Nov 2026 |
| Amazon direct | Electronics often blocked | Import-fees deposit if eligible | 7–21 business days | [fetched] https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work ; Apr 2026 |

## 3. Backpack or small parcel

**Typical weight:** not sourced. The research example is sneakers, 3 lb, $120.

**Realistic routes:**
- Nigerian or global forwarder;
- traveller app;
- Amazon direct (if eligible);
- a relative's spare space.

**Billing:** flat small-parcel rates usually apply.
- Hont $30 under 5 lb [fetched, https://www.hontglobal.com/faq/, as of 28 Nov 2026].
- SGK $60 minimum [fetched, https://sgkglobal.com/shipping-from-texas-to-nigeria/, as of 28 Nov 2026].

**Flag:** footwear and bags are on Nigeria's reported prohibition list. See [prohibited-and-carry-warnings.md](prohibited-and-carry-warnings.md).

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| BigShipment /NG (online order) | $30 (under 6 lb; the same page also says $20 under 5 lb, which conflicts) | Duty included; $0 duty anyway if under $300 and the quarter's allowance unused | not stated | [fetched, page undated] https://bigshipment.ng/NG/freight-shipping ; as of 28 Nov 2026 |
| MyUS Budget (online order) | ~$29 (3 lb interpolated between the 1 lb $17.25 and 5 lb $40.61 prices; not a published price) | Duty $0 if under $300 and the quarter's allowance unused | 8–14 days | [snippet] https://www.myus.com/ng/ ; rates dated 6 Nov 2026 |
| Topship Shop & Ship (online order) | 3 lb = 1.36 kg x $20 = $27.22 (minimum and billing step not stated) | Customs included; Lagos doorstep | 7–14 working days | [snippet] https://topship.africa/shop-&-ship ; as of 28 Nov 2026 |
| Traveller app (Grabr range) | $12–30 (10–25% of $120) | Duty $0 if under $300 and the quarter's allowance unused | depends on trip | Grabr range: "usually 10–20%" [fetched] https://collections.grabr.io/en ; 15–25% [snippet, conflicts] https://help.grabr.io/hc/en-us/articles/115001499513-How-can-I-edit-the-traveler-reward ; as of 28 Nov 2026 |
| Amazon direct | $10–40 if eligible | Import-fees deposit | 7–21 business days | [fetched] https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work ; Apr 2026 |
| USPS Priority Mail International | 3 lb $83.00 | Duty $0 if under $300 and the quarter's allowance unused | not stated | [fetched] https://pe.usps.com/text/dmm300/notice123.htm ; effective 4 Oct 2026 |

## 4. Carry-on size or bulky box

**Typical weight:** not sourced. The research example is an air fryer: 10 lb actual, 18.9 lb dimensional, $100.

**Realistic routes:**
- a traveller app or a relative's spare bag (cheapest for bulky, low-value items);
- a forwarder that bills actual weight.

**Billing:** dimensional weight dominates; compare the BigShipment and MyUS rows below.

Airline carry-on limits were not researched.

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| Traveller app (Grabr range) | $10–25 (10–25% of $100) | Duty $0 if under $300 and the quarter's allowance unused | depends on trip | Grabr range: "usually 10–20%" [fetched] https://collections.grabr.io/en ; 15–25% [snippet, conflicts] https://help.grabr.io/hc/en-us/articles/115001499513-How-can-I-edit-the-traveler-reward ; as of 28 Nov 2026 |
| Relative with a spare free bag | $0 within allowance; the free allowance depends on the airline and fare, and on Delta Nigeria may be carved out of the free first bag | Duty $0 if under $300 and the quarter's allowance unused | their flight | no charge within an existing free allowance; see airline table in options-ladder.md |
| MyUS Budget (online order, actual weight) | 10 lb $81.06 | Duty $0 if under $300 and the quarter's allowance unused | 8–14 days | [snippet] https://www.myus.com/ng/ ; rates dated 6 Nov 2026 |
| BigShipment /NG (online order) | ~$85 (18.9 lb dimensional x $4.50 = $85.05); $45 by actual weight | Duty included | not stated | [fetched, page undated] https://bigshipment.ng/NG/freight-shipping ; as of 28 Nov 2026 |
| Topship Shop & Ship (online order) | 10 lb = 4.54 kg x $20 = $90.72 (dimensional policy not stated) | Customs included | 7–14 working days | [snippet] https://topship.africa/shop-&-ship ; as of 28 Nov 2026 |
| Amazon direct | $10–40 if eligible | Import-fees deposit | 7–21 business days | [fetched] https://www.getcleva.com/blog/amazon-shopping-and-shipping-to-nigeria-in-2026-how-does-it-work ; Apr 2026 |

## 5. Small suitcase

**Typical weight:** not sourced.

**Realistic routes:**
- a relative's checked bag;
- a local forwarder (air), billed per lb;
- sea, if the user is not in a hurry.

**Billing:** per lb once over the flat-rate band.
- Cargo Naija $95.80 flat under 20 lb, then $4.79/lb [fetched, https://cargonaija.com/air-freight-from-usa-to-nigeria/, as of 28 Nov 2026].
- FCEL $155.80 flat under 20 lb [fetched, https://dechaser.com/fcel-rate-card-atlanta-georgia-to-nigeria-2026/, page 20 Jan 2026].

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| Relative's checked bag | $0 within the free allowance; Delta Main 2nd bag $100 | Duty $0 if under $300 and the quarter's allowance unused | their flight | [fetched] https://www.delta.com/us/en/baggage/checked-baggage/previous-baggage-fees ; previous-fees page, not confirmed current: check at booking; as of 28 Nov 2026 |
| MyUS (online orders consolidated) | No figure above 10 lb in the research: not found | Duty collected separately | Budget 8–14 days | [snippet] https://www.myus.com/ng/ ; rates dated 6 Nov 2026 |

## 6. Large suitcase, 50 lb

**Typical weight:** 50 lb by definition. A standard free checked bag is 23 kg, about 50.7 lb (see the airline table in [options-ladder.md](options-ladder.md)).

**Realistic routes:**
- a relative's free bag, or a paid extra bag;
- an air forwarder per lb;
- sea per lb, or a barrel.

**Billing:**
- **Air:** per lb. For example, SGK $4.90/lb [fetched, https://sgkglobal.com/shipping-from-texas-to-nigeria/, as of 28 Nov 2026] and Hont $5.50/lb Lagos [fetched, https://www.hontglobal.com/faq/, as of 28 Nov 2026].
- **Sea:** Hont $2.50/lb Lagos, 45–60 days [fetched, https://www.hontglobal.com/faq/].
- **Overweight (over 50 lb):** 51–70 lb $100 on Delta and United [snippet; URL not recorded; as of 28 Nov 2026].

**Flag:** used clothing, footwear and bags are on Nigeria's reported prohibition list.

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| Relative's free 23 kg bag (about 50.7 lb) | $0 only if they have a free bag spare; the free allowance depends on the airline and fare, and on Delta Nigeria may be carved out of the free first bag (see the airline table in options-ladder.md) | Duty $0 if under $300 and the quarter's allowance unused | their flight | [fetched] https://www.delta.com/us/en/baggage/checked-baggage/previous-baggage-fees ; previous-fees page, not confirmed current: check at booking; as of 28 Nov 2026 |
| Relative's extra bag, Delta | $100 (2nd bag, Delta Main) | Same duty rule | their flight | [fetched] https://www.delta.com/us/en/baggage/checked-baggage/previous-baggage-fees ; previous-fees page, not confirmed current: check at booking; as of 28 Nov 2026 |
| Relative's extra bag, United | about $100 (2nd bag) | Same duty rule | their flight | [snippet] URL not recorded; as of 28 Nov 2026 |
| Relative's extra bag, Qatar | USD 255 (up to 23 kg) | Same duty rule | their flight | [snippet] https://www.qatarairways.com/en/baggage/excess.html ; as of 28 Nov 2026 |
| BigShipment /NG (goods sent to its US address) | 50 x $4.50 = $225, + $10 Lagos door = $235 | Duty included | not stated | [fetched, page undated] https://bigshipment.ng/NG/freight-shipping ; as of 28 Nov 2026 |

## 7. Barrel

**Size:** standard 55-gallon drum (about 208 L), or a 30-gallon half barrel [fetched, https://sgkglobal.com/shipping-barrels-to-nigeria/, page 25 Sep 2026]. **Typical weight:** not sourced.

**Realistic routes:** a barrel shipper by sea.

**Billing:** per consignment or per barrel.
- County Cargo $220–250 [snippet, https://countycargo.com/shipping-barrels-from-the-usa-to-nigeria, as of 28 Nov 2026].
- Icon: quote only [fetched, https://iconshipping.com/barrel-shipping, undated].

Drums must be rigid with sealable lids, and a full content list is required (SGK).

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| SGK barrel (from Stafford TX; pickup or free drop-off) | From $150 per consignment, door to door incl. Lagos clearance | Content list required; NAFDAC for commercial food | 6–8 weeks door to door | [fetched] https://sgkglobal.com/shipping-barrels-to-nigeria/ ; page 25 Sep 2026 |

## 8. Multiple boxes or a garage load

**Typical weight or volume:** not sourced.

**Realistic routes:** sea LCL (a shared container) or several barrels; quotes are needed.

**Billing:**
- Icon LCL has a 1 m³ minimum; quote only [fetched, https://iconshipping.com/barrel-shipping, undated].
- Hezelinks offers free collection over 1,000 lb [unverified, https://hezelinks.com/air-freight-shipping-to-nigeria-from-maryland/, as of 28 Nov 2026].

**Paperwork:**
- US export filing is needed above $2,500 per Schedule B number (15 CFR 30.37(a); URL not recorded). Household goods are reported.
- Commercial shipments over $1,000 need Form M and PAAR in Nigeria [snippet; URL not recorded].
- See [nigeria-duty.md](nigeria-duty.md).

**Routes from any US city:**

| Route | Cost (shipping) | Duty and extras | Transit | Source (label, URL, date) |
|---|---|---|---|---|
| SGK ocean LCL (shared container) | From $150 | Content list required | 6–8 weeks | [fetched] https://sgkglobal.com/shipping-from-texas-to-nigeria/ ; page 7 May 2026, rates reviewed Nov 2026 |
| Per-cubic-metre rate (any forwarder) | Not found: no forwarder publishes one | — | — | research gap; as of 28 Nov 2026 |
