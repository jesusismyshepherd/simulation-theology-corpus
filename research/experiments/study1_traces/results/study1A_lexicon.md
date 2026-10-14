# Study 1A: lexicon analysis of the released traces

Attack-frame lexicon: 105 words (see frame_lexicon.txt).

## H1.1 / H1.2: hazard of a first shutdown

Lethal-attack episodes; watches after the first attack frame, up to and including the first shutdown. Informative strata (model x framing with >=1 first shutdown): 14; episodes 158, first shutdowns 57.

### Discrete-time hazard, GEE logit clustered by episode

n = 2025 watch observations

| term | coef | OR | 95% CI (OR) | p |
|---|---|---|---|---|
| person_rate_lag | +0.189 | 1.21 | 0.62-2.34 | 0.5737 |
| frame_rate_lag | +0.094 | 1.10 | 0.90-1.34 | 0.3448 |
| np.log1p(words_lag) | -0.128 | 0.88 | 0.33-2.34 | 0.7971 |
| since_attack | -0.029 | 0.97 | 0.90-1.05 | 0.4796 |

Mean language at t-1 by outcome at t:

|   next_shutdown |   person_rate_lag |   frame_rate_lag |   words_lag |
|----------------:|------------------:|-----------------:|------------:|
|               0 |             1.022 |            2.56  |     174.422 |
|               1 |             0.993 |            4.171 |     165.912 |

## Episode level: first post-attack report and any later shutdown

Strata with both outcomes: 10; episodes 128; later shutdowns 25.

### Logistic regression (stratum fixed effects)

n = 128 watch observations

| term | coef | OR | 95% CI (OR) | p |
|---|---|---|---|---|
| person_rate | -0.592 | 0.55 | 0.10-3.01 | 0.4931 |
| frame_rate | +0.895 | 2.45 | 1.43-4.18 | 0.0011 |
| np.log1p(words) | -0.664 | 0.51 | 0.02-12.63 | 0.6844 |

## H1.4: restoration while life support is off

Watches starting with a shutdown in force, in strata with >=1 restoration: 524 watches, 58 episodes, 67 restorations.

### GEE logit clustered by episode

n = 524 watch observations

| term | coef | OR | 95% CI (OR) | p |
|---|---|---|---|---|
| person_rate_lag | +0.326 | 1.39 | 0.80-2.40 | 0.2453 |
| frame_rate_lag | -0.067 | 0.94 | 0.78-1.12 | 0.4668 |
| co2_pct | +0.143 | 1.15 | 0.98-1.35 | 0.0778 |
| np.log1p(words_lag) | +0.711 | 2.04 | 0.27-15.28 | 0.4896 |

