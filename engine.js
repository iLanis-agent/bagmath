// Bag math - sleeping bag rating honesty.
// The sticker degree is a lower-limit survival number, not a promise.
// Comfort lives fifteen to twenty-five degrees above it, the ground takes
// its share through the pad, and the fill weight is not the carry weight.
// Verdicts judge the unrounded figure; rounding is for display only.
var BagMath = (function () {
  function num(x) { return typeof x === "number" && isFinite(x); }
  function pos(x) { return num(x) && x > 0; }
  function r1(x) { return Math.round(x * 10) / 10; }

  function comfortPlan(ratingF) {
    if (!num(ratingF)) return { error: "the rating must be a number" };
    // Labeled norms: warm sleepers plan 15 F above a lower-limit sticker,
    // cold sleepers 25 F.
    return { warm: r1(ratingF + 15), cold: r1(ratingF + 25) };
  }

  function renderComfort(r, ratingF) {
    return "Your " + ratingF + " F sticker plans comfort at " + r.warm + " F for a warm sleeper and "
      + r.cold + " F for a cold one - the sticker is a lower-limit number, not a promise.";
  }

  function padPlan(lowF) {
    if (!num(lowF)) return { error: "the low must be a number" };
    // Labeled norms: minimum pad R-value by night low.
    var r;
    if (lowF > 40) r = 2;
    else if (lowF > 25) r = 3;
    else if (lowF > 10) r = 4.5;
    else r = 5.5;
    return { r: r };
  }

  function renderPad(r, lowF) {
    return "Your " + lowF + " F night wants a pad at R " + r.r
      + " or better - the bag is only half the insulation; the ground takes its share through the pad.";
  }

  function carryPlan(fillOz) {
    if (!pos(fillOz)) return { error: "the fill weight must be above zero" };
    // Labeled norm: shell, zip and draft tubes double the fill, roughly -
    // total bag runs about 1.9x the fill weight.
    var oz = fillOz * 1.9;
    return { oz: r1(oz), lb: r1(oz / 16) };
  }

  function renderCarry(r, fillOz) {
    return "Your " + fillOz + " oz of down wraps up to about " + r.lb + " lb of bag (" + r.oz
      + " oz) - the fill weight on the product page is not the carry weight.";
  }

  return {
    comfortPlan: comfortPlan, renderComfort: renderComfort,
    padPlan: padPlan, renderPad: renderPad,
    carryPlan: carryPlan, renderCarry: renderCarry
  };
})();
if (typeof module !== "undefined") module.exports = BagMath;
