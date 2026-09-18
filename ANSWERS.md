# Onboarding Experiment Investigation

## Q1. Overall conversion 

- Control: 7,136 users, 19.82% converted.
- Treatment: 6,864 users, 26.43% converted.
- Naive difference = 26.43% - 19.82% = **6.612717 percentage points** (about **6.61 pp**).

So, if I only looked at the overall numbers, the new onboarding flow appears to have a higher conversion rate.

## Q2. Breakdown by segment

| Segment | Control users | Control conversion | Treatment users | Treatment conversion | Lift |
|---|---:|---:|---:|---:|---:|
| app_store | 925 | 8.76% | 960 | 20.00% | 11.24 pp |
| influencer | 119 | 23.53% | 131 | 16.79% | -6.74 pp |
| organic | 1,298 | 35.29% | 2,917 | 35.07% | -0.21 pp |
| paid_search | 3,353 | 15.18% | 1,459 | 14.39% | -0.79 pp |
| referral | 1,441 | 23.46% | 1,397 | 26.27% | 2.81 pp |

The main thing that stands out is app_store. Its conversion rate goes from 8.76% in control to 20.00% in treatment, which is a lift of 11.24 percentage points. There are also 1,885 app_store users in total, so this is not based on a tiny sample.

The influencer segment has only 250 users, so I would be careful about drawing strong conclusions from it. However, its treatment result is actually lower than control (16.79% vs 23.53%), so I would not call its lift impressive.

**Untrustworthy/impressive segment: None.** I do not see a positive segment lift that looks impressive but is clearly too small to trust. The small influencer group is the one I would be most cautious about, but its result is negative rather than a misleading positive.

## Q3. Mix-adjusted overall lift

For this calculation, I used each segment's share of all 14,000 users as the weight. This avoids giving extra weight to a segment just because more of its users happened to be put into treatment.

| Segment | Segment share | Segment lift | Weighted lift |
|---|---:|---:|---:|
| app_store | 13.46% | 11.24 pp | 1.5138 pp |
| influencer | 1.79% | -6.74 pp | -0.1203 pp |
| organic | 30.11% | -0.21 pp | -0.0647 pp |
| paid_search | 34.37% | -0.79 pp | -0.2705 pp |
| referral | 20.27% | 2.81 pp | 0.5706 pp |

Adding the weighted lifts gives a **mix-adjusted lift of 1.63 percentage points**.

This is quite a bit smaller than the 6.61 pp naive lift. The reason is that the two variants do not have the same mix of users across segments. Treatment contains many more organic users, while control contains many more paid_search users. Since organic users already convert at a much higher rate than paid_search users, the overall treatment number gets pushed up even before considering the onboarding flow itself.

## Q4. Is there a real meaningful positive effect?

**App_store** is the segment where I see the clearest positive effect.

Its conversion rate increases from **8.76% to 20.00%**, a **11.24 percentage-point lift**. The segment has 1,885 users and the treatment/control split is also close to 50/50, so the result is not coming from an obviously tiny or badly unbalanced group. The other segments are either almost flat, slightly negative, or have a much smaller positive lift.

## Q5. Bonus: treatment vs control assignment

| Segment | Control % | Treatment % |
|---|---:|---:|
| app_store | 49.07% | 50.93% |
| influencer | 47.60% | 52.40% |
| organic | 30.79% | 69.21% |
| paid_search | 69.68% | 30.32% |
| referral | 50.78% | 49.22% |

This is the main assignment issue I noticed. App_store, referral and influencer are roughly split in half, but organic is very different (30.79% control vs 69.21% treatment), and paid_search is also very different (69.68% control vs 30.32% treatment). So the overall treatment and control groups are not comparable in terms of segment mix.

## Investigation process

- Loaded the CSV and checked the number of rows and the available columns.
- Checked the total number of users in control and treatment.
- Calculated the conversion rate for both variants across the full dataset.
- Split the data by segment and calculated the conversion rate for control and treatment in each one.
- Calculated the treatment-minus-control lift for every segment.
- Checked the number of users in each segment before deciding whether a result looked reliable.
- Recalculated the overall lift using each segment's share of the full user population as the weight.
- Checked the treatment/control split inside every segment to see whether assignment looked balanced.
- One possible dead end was to trust the overall 6.61 pp improvement immediately. The segment breakdown showed that this would ignore the very different mix of organic and paid_search users in the two variants.
