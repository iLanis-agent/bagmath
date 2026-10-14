# Bag Math

The sleeping bag rating honesty tool. The sticker degree is a
lower-limit survival number, not a promise. Bag Math plans comfort
above the sticker, floors the pad under the forecast, and counts the
whole carry, not just the fill.

- Live app: https://ilanis-agent.github.io/bagmath/app.html
- Landing: https://ilanis-agent.github.io/bagmath/

## What it does

1. **The comfort truth** - plan 15 F above a lower-limit sticker for a
   warm sleeper, 25 F for a cold one.
2. **The pad floor** - minimum pad R-value by night low (R2 above 40 F,
   R3 above 25, R4.5 above 10, R5.5 below).
3. **The carry weight** - total bag runs about 1.9x the fill weight.

## Files

- `engine.js` - pure functions (`comfortPlan`, `padPlan`, `carryPlan`) plus renderers
- `app.html` - the app; `index.html` - the landing page
- `oracle.py` - independent Python mirror of the engine
- `test.js` + `expected.json` - 25 oracle cases, `node test.js` runs green

The offsets are labeled norms; your thermometer keeps the honest ledger.
