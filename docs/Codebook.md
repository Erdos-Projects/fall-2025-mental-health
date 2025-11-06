## Codebook - Alex

Section: academic information

### `year`

What year are you in your current degree program?

1=1st year
2=2nd year
3=3rd year
4=4th year
5=5th year
6=6th year
7=7th+ year
NaNs: no reply, or non-degree students.

### `enroll`

What is your enrollment status?

1=Full-time student
2=Part-time student
3=Other
NaNs=no reply, or non-degree student

### `gpa_sr`

What is your current overall GPA?

1=ostly A's
2=ostly B's
3=ostly C's
4=ostly D's
5=ostly F's
6=None of these
7=No grade/Don't know
NaNs: no answer

Note: many people selected more than one answer here. To deal with this, 
I filtered people who selected more than two answers, and for those that 
selected two (e.g. 1 and 2, mostly A's and B's), I took the average. 
So, the total scale looks like

1=ostly A's
1.5=ostly A's and B's
2=ostly B's
2.5=ostly B's and C's
3=ostly C's
3.5=ostly C's and D's
4=ostly D's
4.5=ostly D's and F's.
5=ostly F's
6=Other
7=Don't know
NaNs: no answer

Note: 6,7, and NaNs can be amalgamated.

### `aca_impa`

Section: ental Health Status and Academic Performance

In the past 4 weeks, how many days have you felt
that emotional or mental difficulties have hurt
your academic performance?

1=None
2=1-2 days
3=3-5 days
4=6 or more days
NaNs=no answer

Note: there's a considerable amount of people (several percent) 
who don't fill out this one

### `persist`

How much do you agree with the following statement?:
I am confident that I will be able to finish my degree no
matter what challenges I may face.

1=Strongly Agree
2=Agree
3=Somewhat Agree
4=Somewhat Disagree
5=Disagree
6=Strongly Disagree
NaNs=no answer

Note: there's a considerable amount of people (several percent) 
who don't fill out this one

### `degree`

In what degree program are you currently
enrolled? (Select all that apply)

1=Associate's
2=Bachelor's
3=aster's
4=JD
5=D
6=PhD (or equivalent doctoral)
8=Other
9=Non-degree student

Also, original columns
- degree_ass
- degree_bach
- degree_ma
- degree_jd
- degree_md
- degree_phd
- degree_other
- degree_nd

are imported, which have a value 1 (enrolled in that degree) or NaN (not enrolled). 

Note: some people selected more than 2 degrees at the same time. 
Those entried are filtered out.

Note: for now, I have sums in the `degree` column, but hot encoding would be better.

### `field`

What is your field of study?

This column is created from the original columns 
"field_hum","field_nat","field_soc","field_arc","field_art","field_bus","field_den","field_ed","field_eng","field_law","field_med","field_mus","field_nur","field_pharm","field_prep","field_ph","field_pp","field_sw","field_und","field_other", all of which 
have value 1.0 (selected) or NaN (not selected).

I enumerate the columns above from 1 to 20, and sums are used where more than 
one field is selected (hot encoding again is suggested). 

Note: people in more than 3 fields are filtered out.
## CODEBOOK - Lili

### `fincur`

Section: (1) DEOGRAPHICS  

Q: How would you describe your financial situation right now?  
  
A:  
1=Always stressful  
2=Often stressful  
3=Sometimes stressful  
4=Rarely stressful  
5=Never stressful  

### `finpast`

Section: (1) DEOGRAPHICS. 

Q: How would you describe your financial situation while growing up?  

A:  
1=Always stressful  
2=Often stressful  
3=Sometimes stressful  
4=Rarely stressful  
5=Never stressful  

### `food_worry`

Section: (1) DEOGRAPHICS  

Q: Within the past 12 months I was worried whether our food would run out before we got money to buy more.  

A:  
1=Never true  
2=Sometimes true  
3=Often true  

### `food_notlast`

Section: (14) FINANCIAL STRESS  

Q: Within the past 12 months the food I bought just didn’t last and I didn’t have money to get more.  

A:  
1=Never true  
2=Sometimes true  
3=Often true  

### `housing_worry`

Section: (1) DEOGRAPHICS (years 2022-2023, 2023-2024, 2024-2025)  

Q: Within the past 12 months I was worried about not having stable housing. (Not having stable housing includes sleeping in vehicles, motels, campgrounds, homeless shelters, single-occupancy facilities, or couches in other people’s homes because you had nowhere else to go.)  

A:  
1=Never true  
2=Sometimes true  
3=Often true  

### `dependents`

Section: (1) DEOGRAPHICS (`dependents` years 2023-2024 and 2024-2025; `children_dep` years 2019-2020 and 2021-2022)  

Q: What is the current number of children or other dependents living in your household, for whom you areresponsible?  

A:  
1=0  
2=1  
3=2  
4=3  
5=4 or more  

### `educ_par1` 

Section: (1) DEOGRAPHICS  

Q: What is the highest level of education completed by your parents, step-parents, or guardians? **(parent 1)**

A:  
1=8th grade or lower  
2=Between 9th and 12th grade (but no high school degree)  
3=High school degree  
4=Some college (but no college degree)  
5=Associate’s degree  
6=Bachelor’s degree  
7=Graduate degree  
8=Don’t know **(has been replaced with `nan` in my dataset)**  

### `educ_par2`

Section: (1) DEOGRAPHICS  

Q: What is the highest level of education completed by your parents, step-parents, or guardians? **(parent 2)**

A:  
1=8th grade or lower  
2=Between 9th and 12th grade (but no high school degree)  
3=High school degree  
4=Some college (but no college degree)  
5=Associate’s degree  
6=Bachelor’s degree  
7=Graduate degree  
8=Don’t know **(has been replaced with `nan` in my dataset)**  

### `educ_par1_rel`

Section: (1) DEOGRAPHICS  

Q: What is this person’s relationship to you? **(parent 1)**

A:  
1=other/stepmother  
2=Father/stepfather  
3=Other  **(has been replaced with `nan` in my dataset, and if `educ_par1` has been answered, that answer is set to `nan` as well)**

### `educ_par2_rel`

Section: (1) DEOGRAPHICS  

Q: What is this person’s relationship to you? **(parent 2)**

A:  
1=other/stepmother  
2=Father/stepfather  
3=Other  **(has been replaced with `nan` in my dataset, and if `educ_par2` has been answered, that answer is set to `nan` as well)**

### `living_sit`

Section: (1) DEOGRAPHICS (years 2023-2024 and 2024-2025)

Q: What is your current living situation?  

A:  
1=I have a steady place to live  
2=I have a place to live today, but I am worried about losing it in the future  
3=I do not have a steady place to live (e.g., I am temporarily staying with others, in a hotel, in a shelter, living outside on the street, on the beach, in a car, abandoned building, bus or train station, or in a park)  
4=Other **(has been replaced with `nan` in my dataset)**

### `residenc`

Section: (1) DEOGRAPHICS  

Q: Where do you currently live?  

A:  
1=On-campus housing, residence hall  
2=On-campus housing, apartment  
3=Fraternity or sorority house  
4=On- or off-campus co-operative housing  
5=Off-campus, non-university housing  
6=Off-campus, with my parent(s)/guardian(s) (or relatives)  
7=Other **(has been replaced with `nan` in my dataset)**  
8=I am currently houseless/homeless **(only appears in years 2023-2024 and 2024-2025)**  

## Features - Dongyi

| feature | question \& <br> feature type | possible values | additional notes 
| -- | -- | -- | -- |
|`diener1 (Q3.2.1)` `diener2 (Q3.2.2) diener3 (Q3.2.3) diener4 (Q3.2.4) diener5 (Q3.2.5) diener6 (Q3.2.6) diener7 (Q3.2.7) diener8 (Q3.2.8)`| Below are 8 statements with which you may agree or disagree. Using the 1-7 scale below, indicate your agreement with each item by indicating that response for each statement   1 I lead a purposeful and meaningful life.  2 y social relationships are supportive and rewarding.  3 I am engaged and interested in my daily activities. 4 I actively contribute to the happiness and well-being of others. 5 I am competent and capable in the activities that are important to me. 6 I am a good person and live a good life. 7 I am optimistic about my future. 8 People respect me.  | 1=Strongly disagree 2=Disagree 3=Slightly disagree 4=ixed or neither agree nor disagree 5=Slightly agree 6=Agree 7=Strongly agree | not in the df.columns, just for the purpose of explaining `flourish` |
|`flourish`| Sum of diener1 through diener8  | range [8, 56] |   |
|`phq9_1 (Q3.3.1) phq9_2 (Q3.3.2) phq9_3 (Q3.3.3) phq9_4 (Q3.3.4) phq9_5 (Q3.3.5) phq9_6 (Q3.3.6) phq9_7 (Q3.3.7) phq9_8 (Q3.3.8) phq9_9 (Q3.3.9)`| Over the last 2 weeks, how often have you been bothered by any of the following problems?  1 Little interest or pleasure in doing things 2 Feeling down, depressed or hopeless 3 Trouble falling or staying asleep, or sleeping too much 4 Feeling tired or having little energy 5 Poor appetite or overeating 6 Feeling bad about yourself—or that you are a failure or have let yourself or your family down 7 Trouble concentrating on things, such as reading the newspaper or watching television 8 oving or speaking so slowly that other people could have noticed; or the opposite—being so fidgety or restless that you have been moving around a lot more than usual 9 Thoughts that you would be better off dead or of hurting yourself in some way | 1=Not at all 2=Several days 3=ore than half the days 4=Nearly every day | not in the df.columns, just for the purpose of explaining `deprawsc` |
|`deprawsc`| Sum of phq9_1 through phq9_9  | range [0, 27] | 
|`dep_maj`| `dep_maj = positive` case when `deprawsc >= 15` and `=< 27`  | `1`= Yes `0`= No | 
|`dep_oth`| `dep_oth = positive` case when `deprawsc >= 10` and `=< 14`  | `1`= Yes `0`= No |
|`dep_any`| `dep_maj = positive` case when `deprawsc >= 10` and `=< 27`  | `1`= Yes `0`= No |
|`dep_impa`|  | `1`= `2`= |
|`gad7_1 (Q3.6.1) gad7_2 (Q3.6.2) gad7_3 (Q3.6.3) gad7_4 (Q3.6.4) gad7_5 (Q3.6.5) gad7_6 (Q3.6.6) gad7_7 (Q3.6.7)`| Over the last 2 weeks, how often have you been bothered by the following problems?  1 Feeling nervous, anxious or on edge 2 Not being able to stop or control worrying 3 Worrying too much about different things 4 Trouble relaxing 5 Becoming easily annoyed or irritable 6 Being so restless that it’s hard to sit still 7 Feeling afraid as if something awful might happen |  1=Not at all 2=Several days 3=Over half the days 4=Nearly every day | not in the df.columns, just for the purpose of explaining `anx_score` |
|`anx_score`| Sum of gad7_1 through gad7_7  | range [0, 21] |
|`anx_sev`| anx_sev = positive case when anx_score > 15 and < 21 | `1`= Yes `0`= No |
|`anx_mod`| anx_mod = positive case when anx_score > 10 and < 14 | `1`= Yes `0`= No |
|`anx_any`| anx_any = positive case when anx_score > 10 and < 21 | `1`= Yes `0`= No |
|`sib_cut (Q3.13.1) sib_burn (Q3.13.2) sib_punch (Q3.13.3) sib_scratch (Q3.13.4) sib_pull (Q3.13.5) sib_bit (Q3.13.6) sib_wound (Q3.13.7) sib_carv (Q3.13.8) sib_rub (Q3.13.9) sib_pobj (Q3.13.10) sib_other (Q3.13.11) sib_other_text (Q3.13.11.TEXT) sib_none (Q3.13.12) `| This question asks about ways you may have hurt yourself on purpose, without intending to kill yourself.  In the past year, have you ever done any of the following intentionally? (Select all that apply) | Binary Variables (1=selected, 0=unselected) 1 Cut myself  2 Burned myself  3 Punched or banged myself  4 Scratched myself  5 Pulled my hair  6 Bit myself  7 Interfered with wound healing  8 Carved words or symbols into skin  9 Rubbed sharp objects into skin 10 Punched or banged an object to hurt myself  11 Other (please specify) 12 No, none of these | 
|`sib_cut`|   | It's in the questions above | I should remove this item since they are individual questions |
|`sib_burn`|  | It's in the questions above | I should remove this item since they are individual questions |
|`sib_pull`|  | It's in the questions above | I should remove this item since they are individual questions |
|`sib_carv`|  | It's in the questions above | I should remove this item since they are individual questions |
|`sib_rub`|   | It's in the questions above | I should remove this item since they are individual questions |
|`sib_none`|  | It's in the questions above | I should remove this item since they are individual questions |
|`sib_any`| sib_any = positive case when any of the above (sib_cut through sib_other) = 1  | `1`= Yes `0`= No | 
|`sui_idea`| In the past year, did you ever seriously think about attempting suicide? | `1`= Yes `0`= No |
|`sui_plan`| In the past year, did you make a plan for attempting suicide?  | `1`= Yes `0`= No |
|`sui_att`| In the past year, did you attempt suicide?  | `1`= Yes `0`= No |
|`drug_mar (Q3.26.1 or Q5.11.1) drug_coc (Q3.26.2 or Q5.11.2) drug_her (Q3.26.3 or Q5.11.3) drug_opi (Q3.26.4 or Q5.11.4) drug_benzo (Q3.26.5 or Q5.11.5) drug_met (Q3.26.6 or Q5.11.6) drug_stim (Q3.26.7 or Q5.11.7) drug_ect (Q3.26.8 or Q5.11.8) drug_keta (Q3.26.9 or Q5.11.9) drug_lsd (Q3.26.10 or Q5.11.10) drug_psilo (Q3.26.11 or Q5.11.11) drug_kratom (Q3.26.12 or Q5.11.12) drug_ath (Q3.26.13 or Q5.11.13) drug_other (Q3.26.14 or Q5.11.14) drug_other_text (Q3.26.14.TEXT or Q5.11.14.TEXT) drug_none (Q3.26.15 or Q5.11.15)`|Over the past 30 days, have you used any of the following drugs recreationally? (Select all that apply) |Binary Variables (1=selected, 0=unselected) 1 Cannabis products that contain THC (including smoking, vaping, and edibles) 2 Cocaine (any form, including crack, powder, or freebase) 3 Heroin 4 Opioid pain relievers (such as Vicodin, OxyContin, Percocet, Demerol, Dilaudid, codeine, hydrocodone, methadone, morphine) without a prescription or more than prescribed 5 Benzodiazepines (such as Valium, Ativan, Klonopin, Xanax, Rohypnal (Roofies)) 6 ethamphetamines (also known as speed, crystal meth, Tina, T,  or ice) 7 Other stimulants (such as Ritalin, Adderall) without a prescription or more than prescribed 8 DA (also known as Ecstasy or olly) 9 Ketamine (also known as K, Special K) 10 LSD (also known as acid) 11 Psilocybin (also known as magic mushrooms, boomers, shrooms) 12 Kratom 13 Athletic performance enhancers (anything that violates policies set by your school or any athletic governing body)  14 Other drugs without a prescription (please specify) 15 No, none of these [mutually exclusive] |
|`drug_none`|  | It's in the questions above | I should remove this item since they are individual questions|
|`sub_any`| sub_any = positive case when any of the above (drug_mar through drug_other) = 1 (yes)  | `1`= Yes `0`= No |
|`lone_lackcompanion`| Please answer the following: How often do you feel that you lack companionship?  |`1`=Hardly ever `2`=Some of the time `3`=Often |
|`lone_leftout`| How often do you feel left out? | `1`=Hardly ever `2`=Some of the time `3`=Often |
|`lone_isolated`| How often do you feel isolated from others?  |`1`=Hardly ever `2`=Some of the time `3`=Often |
|`lonesc`| Sum of lone_lackcompanion + lone_leftout + lone_isolated  (an observation receives an NA value for lonesc if any one of the lone variables = NA)  | range=[3, 9] |
|`lonel`|  lonely = positive case when lonsc >= 6 and <= 9  | `1`= Yes `0`= No |

# features - Saaransh

|    feature    | feature type |                                                possible values                                                | additional notes |
| :-----------: | :----------: | :-----------------------------------------------------------------------------------------------------------: | :--------------: |
|     `age`     |  numerical   |                                                    [18,60]                                                    |                  |
|   `gender`    | categorical  |                  `1` = female  <br> `2` = male  <br> `3` = trans <br> `4` = non binary <br>                   |                  |
|  `sex_birth`  | categorical  |                            `1` = female  <br> `2` = male  <br> `3` = intersex <br>                            |                  |
| `sexual_pref` | categorical  | `1` = heterosexual<br> `2` = lesbian<br> `3` = gay <br> `4` = bisexual<br> `5` = queer <br> `6` = questioning |                  |
# Features - Jose

| feature | question \& <br> feature type | possible values | additional notes 
| -- | -- | -- | -- |
|`race`| What is your race/ethnicity? <br> categorical | `1` = African American/Black <br> `2` = American Indian or Alaskan Native <br> `3` = Asian American/Asian <br> `4` = Hispanic/Latine <br> `5` = Native Hawaiian or Pacific Islander <br> `6` = iddle Eastern, Arab, or Arab American <br> `7` = White | Up to **one** values permitted. <br> If more than one races selected, or if self-identified (text description), the row is dropped. |
|`international`| Are you an international student? <br> categorical | `1` = yes <br> `0` = no |
|`alc_any`| Over the past 2 weeks, did you drink any alcohol? <br> categorical |  `1` = yes <br> `0` = no |
|`alc_binge`| Over the past 2 weeks, about how many times did you have 4/5(female/male) or more alcoholic drinks in a row? | `1` = 0 times <br> `2` = 1 time <br> `3` = 2 times <br> `4` = 3 to 5 times <br> `5` = 6 to 9 times <br> `6` = 10 or more times <br> `7` = Don’t know |
|`audit_1`| How often do you have a drink containing alcohol? | `0` = Never <br> `1` = onthly or less <br> `2` = 2-4 times a month <br> `3` = 2-3 times a week <br> `4` = 4 or more times a week | These questions are asked in an elective module. |
|`audit_2`| How many drinks containing alcohol do you have on a typical day when you are drinking? | `0` = 1 or 2 <br> `1` = 3 or 4 <br> `2` = 5 or 6 <br> `3` = 7 to 9 <br> `4` = 10 or more | The notebook claims values are `1-5`, but dataframe takes values `0-4`.
|`audit_3`| How often do you have 4/5(female/male) or more drinks on 1 occasion? | `0` = Never <br> `1` = Less than monthly <br> `2` = onthly <br> `3` = Weekly <br> `4` = Daily or almost daily | contrast to `alc_binge`
|`audit_4`| How often during the last year have you found that you were not able to stop drinking once you had started? | `0` = Never <br> `1` = Less than monthly <br> `2` = onthly <br> `3` = Weekly <br> `4` = Daily or almost daily |
|`audit_5`| How often during the last year have you failed to do what was normally expected of you because of drinking? | `0` = Never <br> `1` = Less than monthly <br> `2` = onthly <br> `3` = Weekly <br> `4` = Daily or almost daily |
|`audit_6`| How often during the last year have you needed a drink in the morning to get yourself going after a heavy drinking session? | `0` = Never <br> `1` = Less than monthly <br> `2` = onthly <br> `3` = Weekly <br> `4` = Daily or almost daily |
|`audit_7`| How often during the last year have you had a feeling of guilt or remorse after drinking? | `0` = Never <br> `1` = Less than monthly <br> `2` = onthly <br> `3` = Weekly <br> `4` = Daily or almost daily |
|`audit_8`| How often during the last year have you been unable to remember what happened the night before because you had been drinking? | `0` = Never <br> `1` = Less than monthly <br> `2` = onthly <br> `3` = Weekly <br> `4` = Daily or almost daily |
|`audit_9`| Have you or someone else been injured because you had been drinking? | | ~~removed~~ corrupted column <br> missing values in 2023-2024 and 2024-2025 and different weight across different years (0,1,2 vs 0,2,4)~~
|`audit_10`| Has a relative, friend, doctor, or other health care worker been concerned about your drinking or suggested you cut down? | | ~~removed~~ corrupted column <br> missing values in 2023-2024 and different weight across different years (0,1,2 vs 0,2,4)
|`smok_freq`| Over the past 30 days, about how many cigarettes did you smoke per day? | `1` = 0 cigarettes <br> `2` = Less than 1 cigarette <br> `3` = 1 to 5 cigarettes <br> `4` = About one-half pack <br> `5` = 1 or more pack | missing in last two years |
|`smok_vape`| Over the past 30 days, have you used an electronic cigarette or vape pen? | `1` = yes <br> `0` = no | missing in last two years <br> some years used `1` = yes `2` = no (fixed using `df['smok_vape'] = df['smok_vape']%2`) |
|`exerc`| In the past 30 days, about how many hours per week on average did you spend exercising? | `1` = Less than 1 hour <br> `2` = 1-3 hours <br> `3` = 3-4 hours <br> `4` = 5 or more hours | All years include the option "2-3 hours", but only some include "1-2" hours. erged appropiately. <br> Examples: <br> 2021-2022 include option `6` = 1-2 hours. <br> Last two years include option `2` = 1-2 hours and shift other values up by 1. |

<!-- |`race`| What is your race/ethnicity? <br> categorical (one-hot encoded) | `race_black` = African American/Black <br> `race_ainaan` = American Indian or Alaskan Native <br> `race_asian` = Asian American/Asian <br> `race_his` = Hispanic/Latine <br> `race_pi` = Native Hawaiian or Pacific Islander <br> `race_mides` = iddle Eastern, Arab, or Arab American <br> `race_white` = White | Up to two values permitted. <br> If more than two races selected, or if self-identified (text description), the row is dropped. | -->
