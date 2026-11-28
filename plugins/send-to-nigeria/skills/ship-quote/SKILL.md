---
name: ship-quote
description: Walks the user step by step through a US-to-Nigeria shipping quote (item, size, weight, value, US city, pickup or drop-off, Nigerian city, urgency), then returns two or three ranked routes with sourced, dated costs.
argument-hint: "[item description]"
disable-model-invocation: true
---

# Ship quote: US to Nigeria

The user wants a quote for getting something from the US to Nigeria. If they typed a description after the command, start from it: $ARGUMENTS

**This is general information, not legal, customs or tax advice.** Say so in the final answer.

## 1. Ask, in this order

Ask one short question at a time. Skip anything the user has already told you.

1. **What is it, and do you already have it, or are you buying it online?** An online order can ship straight to a forwarder's US address.
2. **Size, weight and value.**
   - Which size class: envelope/phone, laptop, backpack, carry-on, small suitcase, large 50 lb suitcase, barrel, or several boxes?
   - The actual weight, and the box size (L x W x H in inches) if it is bulky.
   - The value in USD, and whether the whole order is under $300.
   - New or used?
3. **Which US city or ZIP code** is it starting from?
4. **Pickup or drop-off?**
5. **Which city in Nigeria** is it going to? (Lagos, or another state?)
6. **How soon does it need to arrive?** Days, or are weeks fine?

## 2. Work it out

Use the reference files in [../send-to-nigeria/references/](../send-to-nigeria/references/) (paths below are relative to that folder):
1. **Screen for blockers** in `prohibited-and-carry-warnings.md`. Flag any problem before giving prices.
2. **Read the size class** in `size-classes.md`.
3. **Read the matching city file** in `scenarios/`: `chicago.md`, `dc-baltimore.md`, `houston-texas.md` or `atlanta.md`. Go to the section for the user's size class.
4. **Check the duty position** in `nigeria-duty.md`. Never suggest splitting an order to stay under $300.
5. **Re-check the shortlisted providers live** by following `recheck-live.md`, with WebFetch first and WebSearch as the fallback.
6. **If the city or country is not covered**, follow `research-method.md` and `templates/scenario-template.md`. Label every figure "found live on <date>, not yet reviewed".
   - Never reuse Nigeria's duty rule for another country.
   - Offer the user the link https://github.com/Erriccc/jappa-labs/issues/new to share what was found. Do not file anything yourself.

## 3. Answer

Give two or three **ranked routes**. For each one:
- **Route and provider.**
- **Total cost:** shipping + duty/VAT + fees, with the arithmetic shown.
- **Transit time.**
- **Risks:** prohibited items, duty uncertainty, minimums, dimensional weight, and traveller or carry risks (see [prohibited-and-carry-warnings.md](../send-to-nigeria/references/prohibited-and-carry-warnings.md)).
- **Source URL and as-of date** for every figure, labelled [fetched today], [baseline, as of 28 Nov 2026], [snippet] or [unverified].

Never invent a number. If a figure isn't sourced, say "not found; ask for a quote".

End with the reminder that this is general information, not legal, customs or tax advice.
