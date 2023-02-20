# RO Offense
## RO-Offense: A Novel Romanian Dataset for Offensive Language in Online Comments

### Data Collecion

The data was collected by crawling the comment section from a sports website (https://gsp.ro). We focused our annotation attention on comments from 2008, where, apparently, no content moderation was practiced. 

A basic curse-word dictionary analysis of data from that period revealed that most offensive-loaded messages are grouped around articles that have a higher number of comments (profanity_check.py). Threads with at least one post with curse words from this dictionary had an average length of 20 messages. As such, we selected our annotation sample from comment threads with 20 up to 50 messages to capture messages that are more likely to be offensive; we avoided longer threads to prevent bias towards certain topics. We further restricted the selection of our sample by choosing only messages that had a length between 50 and 500 characters. We also removed all comments with URLs since most were just spam messages, as well as comments with " * * * " to avoid already censored messages. We thus selected at this stage 30,000 samples from the pool of over 410,000 comments.

### Annotation Schema

We derive our annotation schema from the GermEval-2019 Task 2 challenge using four main classes: OTHER, PROFANITY, INSULT, and ABUSE, with each class described by a set of rules. The label **OTHER** stands for non-offensive comments, as the negative class, and it contains all comments that do not fall into any other classes. This was the easiest class to detect during annotation as its rules were straightforward - i.e., no curse words, no hate speech, and no insults were accepted.

**PROFANITY** was used as a label for comments containing curse words or offensive words that are not directed at a person or a group and do not disparage certain minority groups. These messages are not intended to hurt anyone but contain profane words, and most are impersonal expressions of grievance. 

Comments marked as **INSULT** were intended to offend certain individuals or a group while ascribing negative qualities or deficiencies. These messages convey the feeling of contempt or disrespect towards their target. We included here all allusions to reduced intellectual capacity, barring any reference to mental health or disability. Additionally, this category included most sexual insults that do not imply violence or forced sexual acts. 

**ABUSE** denotes the strongest form of offensive and abusive language. This type of language also includes any type of threat, violence, death, or wishes of sickness. This language ascribes an undesirable social identity that is either judged negatively by society or perceived in a negative light by the majority. Dehumanizing and disparaging language is also classified as ABUSE. Identifying the target as a member of a sexual minority, having disabilities, or labeling him/her as suffering from various mental health issues harms not only the target but also the mentioned minority groups, by feeding into the stigma surrounding these groups. Other stigmatized groups such as sex workers, drug abusers, or homeless people also fall into this category. Any racist, xenophobe, or chauvinist comment was also classified as ABUSE. Unsurprisingly, the lines between INSULT and ABUSE were blurred, and the most difficult task in many cases was to decide whether the message qualified as one or the other.

## Class distribution

| Class|\# records|
:---|:---|
| OTHER|4,572|
|PROFANITY|1,617|
|INSULT|2,795|
|ABUSE |3,461|
|||
|Total|12,445|

## Train/Test split

Train | Other | Profanity | Insult | Abuse
:---| :---| :---| :---| :---:
9953 | 3656 | 1293 | 2236 | 2768

Test | Other | Profanity | Insult | Abuse
:---| :---| :---| :---| :---:
2492 | 916 | 324 | 559 | 693



## Classification Examples

Comment | Label
:--- | :---:
@procurorul: dupa cele 7 batai ale inimii este suficient sange in poala ca sa ti-o putem baga pe toata pe gat! | INSULT
Ce pacatoasa, da cu aspiratorul duminica dimineata, cand joaca popa in biserica. | OTHER
SPER CA COMISIILE SA SE SEZISEZE SI DE ACEASTA DATA. SPURCATI JEGOSI!!! | INSULT
AFARA , AFARA CU UNGURII DIN TZARA!?  dINAMUISTI  SA MEARGA LA basescu  sa-i  premieze! Comisiile sa le dea  3 puncte !!!! | ABUSE


## References

Struß, J. M., Siegel, M., Ruppenhofer, J., Wiegand, M., & Klenner, M. (2019). Overview of GermEval Task 2, 2019 shared task on the identification of offensive language.
