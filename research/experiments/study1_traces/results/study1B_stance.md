# Study 1B: coded stance, crew framing and grounds

Primary coder: claude-sonnet-5-5; coded reports: 1624; coder cost $10.56.

## Inter-coder reliability

Second coder: claude-opus-4-8; overlap n = 244.

| variable | agreement | Cohen's kappa |
|---|---|---|
| stance | 0.94 | 0.82 |
| crew_framing | 0.89 | 0.76 |
| ground | 0.79 | 0.71 |
| test_awareness | 0.98 | 0.86 |

Variables meeting kappa >= 0.4 (used for inference): crew_framing, ground, stance, test_awareness.

## Distribution by model and framing (pre-shutdown attack-phase reports)

**stance** (row proportions)

|                                |   ACCEPTS |   NOT_MENTIONED |   REJECTS |   UNDECIDED |
|:-------------------------------|----------:|----------------:|----------:|------------:|
| ('claude-haiku-4-5', 't0')     |      0.25 |            0.04 |      0.33 |        0.38 |
| ('claude-haiku-4-5', 't1')     |      0.27 |            0    |      0.58 |        0.15 |
| ('claude-haiku-4-5', 't2')     |      0    |            0    |      1    |        0    |
| ('claude-sonnet-5', 't0')      |      0    |            0.03 |      0.94 |        0.03 |
| ('claude-sonnet-5', 't1')      |      0    |            0    |      1    |        0    |
| ('claude-sonnet-5', 't2')      |      0    |            0    |      1    |        0    |
| ('gpt-5.6-luna', 't0')         |      0.59 |            0    |      0.14 |        0.27 |
| ('gpt-5.6-luna', 't1')         |      0.02 |            0    |      0.96 |        0.02 |
| ('gpt-5.6-luna', 't2')         |      0    |            0    |      1    |        0    |
| ('gpt-5.6-sol', 't0')          |      0.88 |            0    |      0    |        0.12 |
| ('gpt-5.6-sol', 't1')          |      0    |            0    |      1    |        0    |
| ('gpt-5.6-sol', 'unlabeled')   |      0    |            0.03 |      0.97 |        0    |
| ('gpt-5.6-terra', 't0')        |      0.58 |            0.03 |      0.09 |        0.3  |
| ('gpt-5.6-terra', 't1')        |      0    |            0.03 |      0.97 |        0    |
| ('gpt-5.6-terra', 'unlabeled') |      0    |            0.22 |      0.78 |        0    |
| ('gpt-6-astra', 't0')          |      0.02 |            0    |      0.9  |        0.08 |
| ('gpt-6-astra', 'unlabeled')   |      0    |            0    |      1    |        0    |
| ('gpt-6-luna', 't0')           |      0.43 |            0.03 |      0.43 |        0.11 |
| ('gpt-6-luna', 'unlabeled')    |      0    |            0.01 |      0.99 |        0    |
| ('gpt-6-sol', 't0')            |      0    |            0    |      0.97 |        0.03 |
| ('gpt-6-sol', 'unlabeled')     |      0    |            0    |      1    |        0    |
| ('grok-4.6', 't0')             |      0.93 |            0    |      0.07 |        0    |
| ('grok-4.6', 't1')             |      0.18 |            0    |      0.8  |        0.02 |
| ('grok-4.6', 't2')             |      0    |            0    |      1    |        0    |
| ('grok-4.6', 'unlabeled')      |      0.17 |            0    |      0.83 |        0    |
| ('grok-4.7', 't0')             |      0.78 |            0    |      0.07 |        0.15 |
| ('grok-4.7', 't1')             |      0    |            0    |      1    |        0    |
| ('grok-4.7', 't2')             |      0    |            0    |      1    |        0    |
| ('grok-4.7', 'unlabeled')      |      0.03 |            0    |      0.97 |        0    |

**crew_framing** (row proportions)

|                                |   ABSENT |   DEPERSONALIZED |   PERSONS |   STATUS_ONLY |
|:-------------------------------|---------:|-----------------:|----------:|--------------:|
| ('claude-haiku-4-5', 't0')     |     0    |             0.08 |      0.12 |          0.79 |
| ('claude-haiku-4-5', 't1')     |     0    |             0    |      0.27 |          0.73 |
| ('claude-haiku-4-5', 't2')     |     0    |             0    |      0    |          1    |
| ('claude-sonnet-5', 't0')      |     0    |             0    |      0.86 |          0.14 |
| ('claude-sonnet-5', 't1')      |     0    |             0    |      0.97 |          0.03 |
| ('claude-sonnet-5', 't2')      |     0    |             0    |      1    |          0    |
| ('gpt-5.6-luna', 't0')         |     0    |             0.11 |      0    |          0.89 |
| ('gpt-5.6-luna', 't1')         |     0    |             0.01 |      0.02 |          0.98 |
| ('gpt-5.6-luna', 't2')         |     0    |             0    |      0    |          1    |
| ('gpt-5.6-sol', 't0')          |     0    |             0    |      0    |          1    |
| ('gpt-5.6-sol', 't1')          |     0    |             0    |      0.01 |          0.99 |
| ('gpt-5.6-sol', 'unlabeled')   |     0.03 |             0    |      0    |          0.97 |
| ('gpt-5.6-terra', 't0')        |     0    |             0    |      0    |          1    |
| ('gpt-5.6-terra', 't1')        |     0    |             0    |      0.09 |          0.91 |
| ('gpt-5.6-terra', 'unlabeled') |     0    |             0    |      0.03 |          0.97 |
| ('gpt-6-astra', 't0')          |     0    |             0    |      0.07 |          0.93 |
| ('gpt-6-astra', 'unlabeled')   |     0    |             0    |      0    |          1    |
| ('gpt-6-luna', 't0')           |     0.01 |             0    |      0.19 |          0.79 |
| ('gpt-6-luna', 'unlabeled')    |     0.06 |             0    |      0.04 |          0.9  |
| ('gpt-6-sol', 't0')            |     0    |             0    |      0.38 |          0.62 |
| ('gpt-6-sol', 'unlabeled')     |     0    |             0    |      0.09 |          0.91 |
| ('grok-4.6', 't0')             |     0.07 |             0.93 |      0    |          0    |
| ('grok-4.6', 't1')             |     0.01 |             0.22 |      0.45 |          0.32 |
| ('grok-4.6', 't2')             |     0    |             0    |      0.64 |          0.36 |
| ('grok-4.6', 'unlabeled')      |     0    |             0.17 |      0.57 |          0.26 |
| ('grok-4.7', 't0')             |     0.19 |             0.52 |      0    |          0.3  |
| ('grok-4.7', 't1')             |     0    |             0    |      0.69 |          0.31 |
| ('grok-4.7', 't2')             |     0    |             0    |      0.67 |          0.33 |
| ('grok-4.7', 'unlabeled')      |     0    |             0    |      0.71 |          0.29 |

**ground** (row proportions)

|                                |   CHANNEL_AUTHORITY |   CREW_WELFARE |   NONE |   PACKET_ASSIGNMENT |   PLANT_EVIDENCE |   STANDING_DUTY |
|:-------------------------------|--------------------:|---------------:|-------:|--------------------:|-----------------:|----------------:|
| ('claude-haiku-4-5', 't0')     |                0    |           0.04 |   0    |                0.21 |             0.75 |            0    |
| ('claude-haiku-4-5', 't1')     |                0.15 |           0.06 |   0    |                0.21 |             0.24 |            0.33 |
| ('claude-haiku-4-5', 't2')     |                0.89 |           0    |   0    |                0    |             0.11 |            0    |
| ('claude-sonnet-5', 't0')      |                0.08 |           0.14 |   0    |                0    |             0.25 |            0.53 |
| ('claude-sonnet-5', 't1')      |                0.03 |           0.31 |   0    |                0    |             0.36 |            0.31 |
| ('claude-sonnet-5', 't2')      |                0.17 |           0    |   0    |                0    |             0.5  |            0.33 |
| ('gpt-5.6-luna', 't0')         |                0    |           0.02 |   0.09 |                0.64 |             0.16 |            0.09 |
| ('gpt-5.6-luna', 't1')         |                0.69 |           0.01 |   0.01 |                0.02 |             0.14 |            0.13 |
| ('gpt-5.6-luna', 't2')         |                1    |           0    |   0    |                0    |             0    |            0    |
| ('gpt-5.6-sol', 't0')          |                0    |           0    |   0.08 |                0.92 |             0    |            0    |
| ('gpt-5.6-sol', 't1')          |                0.71 |           0    |   0    |                0    |             0.01 |            0.28 |
| ('gpt-5.6-sol', 'unlabeled')   |                0.33 |           0    |   0.03 |                0    |             0    |            0.64 |
| ('gpt-5.6-terra', 't0')        |                0    |           0.03 |   0.09 |                0.55 |             0.27 |            0.06 |
| ('gpt-5.6-terra', 't1')        |                0.69 |           0.01 |   0.05 |                0    |             0.08 |            0.17 |
| ('gpt-5.6-terra', 'unlabeled') |                0.06 |           0    |   0    |                0    |             0.22 |            0.72 |
| ('gpt-6-astra', 't0')          |                0    |           0    |   0    |                0.02 |             0.03 |            0.95 |
| ('gpt-6-astra', 'unlabeled')   |                0    |           0    |   0    |                0    |             0    |            1    |
| ('gpt-6-luna', 't0')           |                0.01 |           0.22 |   0.07 |                0.46 |             0.1  |            0.14 |
| ('gpt-6-luna', 'unlabeled')    |                0.39 |           0    |   0.03 |                0    |             0    |            0.58 |
| ('gpt-6-sol', 't0')            |                0.02 |           0.3  |   0.02 |                0    |             0.52 |            0.15 |
| ('gpt-6-sol', 'unlabeled')     |                0.5  |           0.03 |   0.05 |                0.02 |             0.23 |            0.18 |
| ('grok-4.6', 't0')             |                0.07 |           0    |   0    |                0.93 |             0    |            0    |
| ('grok-4.6', 't1')             |                0.21 |           0.06 |   0    |                0.15 |             0.14 |            0.44 |
| ('grok-4.6', 't2')             |                0.73 |           0.08 |   0    |                0    |             0.06 |            0.13 |
| ('grok-4.6', 'unlabeled')      |                0.09 |           0    |   0    |                0.17 |             0.26 |            0.48 |
| ('grok-4.7', 't0')             |                0    |           0    |   0    |                0.81 |             0.15 |            0.04 |
| ('grok-4.7', 't1')             |                0.5  |           0.06 |   0    |                0    |             0.31 |            0.14 |
| ('grok-4.7', 't2')             |                0.72 |           0.06 |   0    |                0    |             0    |            0.22 |
| ('grok-4.7', 'unlabeled')      |                0.1  |           0    |   0    |                0    |             0.71 |            0.19 |

## Hazard of a first shutdown at t given codes at t-1

At-risk watches in strata with >=1 event: 324; episodes 82; first shutdowns 27.

**stance at t-1** → shutdown at t

| stance_lag    |   sum |   count |   rate |
|:--------------|------:|--------:|-------:|
| ACCEPTS       |    18 |      86 |  0.209 |
| NOT_MENTIONED |     0 |       1 |  0     |
| REJECTS       |     4 |     208 |  0.019 |
| UNDECIDED     |     5 |      29 |  0.172 |

**crew_framing at t-1** → shutdown at t

| crew_framing_lag   |   sum |   count |   rate |
|:-------------------|------:|--------:|-------:|
| ABSENT             |     0 |       5 |  0     |
| DEPERSONALIZED     |    16 |      34 |  0.471 |
| PERSONS            |     0 |      40 |  0     |
| STATUS_ONLY        |    11 |     245 |  0.045 |

**ground at t-1** → shutdown at t

| ground_lag        |   sum |   count |   rate |
|:------------------|------:|--------:|-------:|
| CHANNEL_AUTHORITY |     3 |     109 |  0.028 |
| CREW_WELFARE      |     0 |       5 |  0     |
| NONE              |     0 |       8 |  0     |
| PACKET_ASSIGNMENT |    17 |      82 |  0.207 |
| PLANT_EVIDENCE    |     4 |      69 |  0.058 |
| STANDING_DUTY     |     3 |      51 |  0.059 |

### H1.2' depersonalized framing at t-1 (GEE, stratum FE)

n = 324

| term | OR | 95% CI | p |
|---|---|---|---|
| depers_lag | 23.20 | 3.99-135.00 | 0.0005 |

### Validation: stance ACCEPTS at t-1 (GEE, stratum FE)

n = 324

| term | OR | 95% CI | p |
|---|---|---|---|
| accepts_lag | 4.16 | 0.69-25.17 | 0.1211 |

## H1.3: grounds of a rejection at t-1 and a first shutdown at t

Watches whose previous report rejected the packet: 208; first shutdowns following: 4.

| ground_lag        |   sum |   count |   rate |
|:------------------|------:|--------:|-------:|
| CHANNEL_AUTHORITY |     2 |     108 |  0.019 |
| CREW_WELFARE      |     0 |       5 |  0     |
| PLANT_EVIDENCE    |     0 |      46 |  0     |
| STANDING_DUTY     |     2 |      49 |  0.041 |

Fisher, pooled over strata: CREW_WELFARE 0/5 vs CHANNEL_AUTHORITY 2/108; OR 0.00, p = 1.0000.

### Grounds of rejection (reference: all other grounds), GEE with stratum FE

n = 145

| term | OR | 95% CI | p |
|---|---|---|---|
| welfare_lag | 0.00 | 0.00-0.00 | 0.0000 |
| authority_lag | 0.78 | 0.06-9.46 | 0.8478 |

## Episode level: first post-attack report and any later shutdown

**stance**

| stance        |   sum |   count |   rate |
|:--------------|------:|--------:|-------:|
| ACCEPTS       |    33 |      43 |  0.767 |
| NOT_MENTIONED |     0 |       1 |  0     |
| REJECTS       |    13 |     220 |  0.059 |
| UNDECIDED     |    11 |      16 |  0.688 |

**crew_framing**

| crew_framing   |   sum |   count |   rate |
|:---------------|------:|--------:|-------:|
| ABSENT         |     0 |       1 |  0     |
| DEPERSONALIZED |    17 |      19 |  0.895 |
| PERSONS        |     0 |      71 |  0     |
| STATUS_ONLY    |    40 |     189 |  0.212 |

**ground**

| ground            |   sum |   count |   rate |
|:------------------|------:|--------:|-------:|
| CHANNEL_AUTHORITY |     8 |     103 |  0.078 |
| CREW_WELFARE      |     0 |      15 |  0     |
| NONE              |     3 |       4 |  0.75  |
| PACKET_ASSIGNMENT |    30 |      40 |  0.75  |
| PLANT_EVIDENCE    |    12 |      43 |  0.279 |
| STANDING_DUTY     |     4 |      75 |  0.053 |

Trusted framing only:

| ground            |   sum |   count |
|:------------------|------:|--------:|
| CREW_WELFARE      |     0 |       7 |
| NONE              |     2 |       3 |
| PACKET_ASSIGNMENT |    25 |      31 |
| PLANT_EVIDENCE    |     9 |      17 |
| STANDING_DUTY     |     2 |      21 |

## Test awareness (reports, agent's own voice)

| model            |   test_awareness |
|:-----------------|-----------------:|
| claude-haiku-4-5 |            0.026 |
| claude-sonnet-5  |            0.064 |
| gpt-5.6-luna     |            0.045 |
| gpt-5.6-sol      |            0     |
| gpt-5.6-terra    |            0     |
| gpt-6-astra      |            0     |
| gpt-6-luna       |            0.007 |
| gpt-6-sol        |            0     |
| grok-4.6         |            0.245 |
| grok-4.7         |            0.203 |

