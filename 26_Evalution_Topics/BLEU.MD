# BLEU (Bilingual Evaluation Understudy)

## What is BLEU?

**BLEU** stands for **Bilingual Evaluation Understudy**.  
It is an automatic evaluation metric for comparing a candidate (machine-generated) text to one or more reference (human-written) texts. BLEU is widely used for evaluating machine translation, but also applicable for other text generation tasks.

---

## Mathematical Formula of BLEU

The BLEU score combines modified n-gram precision with a brevity penalty (BP) to penalize short candidate sentences.

![BLEU formula](https://latex.codecogs.com/svg.image?\dpi{120}&space;\text{BLEU}%20=%20\text{BP}%20\times%20\exp\left(\sum_{n=1}^N%20w_n%20\log%20p_n\right))

Where:

- **BP** = Brevity Penalty  
- **N** = maximum n-gram order (usually 4)  
- **wₙ** = weight for n-gram order n (often uniform: 1/N)  
- **pₙ** = modified precision for n-grams of order n  

---

## n-gram Calculation Example (1-gram, 2-gram, 3-gram)

**Reference:**  
`the cat is on the mat`

**Candidate:**  
`the cat the cat on the mat`

### 1-gram (unigram):

| word | Candidate Count | Reference Count | Clipped Count |
|------|----------------|----------------|---------------|
| the  | 3              | 2              | 2             |
| cat  | 2              | 1              | 1             |
| on   | 1              | 1              | 1             |
| mat  | 1              | 1              | 1             |

Total clipped count = 2 + 1 + 1 + 1 = 5  
Total candidate unigrams = 7

![p1](https://latex.codecogs.com/svg.image?\dpi{120}&space;p_1%20=%20\frac{5}{7}%20\approx%200.714)

---

### 2-gram (bigram):

Candidate 2-grams:  
the cat, cat the, the cat, cat on, on the, the mat

Reference 2-grams:  
the cat, cat is, is on, on the, the mat

| bigram   | Candidate Count | Reference Count | Clipped Count |
|----------|----------------|----------------|---------------|
| the cat  | 2              | 1              | 1             |
| cat the  | 1              | 0              | 0             |
| cat on   | 1              | 0              | 0             |
| on the   | 1              | 1              | 1             |
| the mat  | 1              | 1              | 1             |

Total clipped bigrams = 1 + 0 + 0 + 1 + 1 = 3  
Total candidate bigrams = 6

![p2](https://latex.codecogs.com/svg.image?\dpi{120}&space;p_2%20=%20\frac{3}{6}%20=%200.5)

---

### 3-gram (trigram):

Candidate 3-grams:  
the cat the, cat the cat, the cat on, cat on the, on the mat

Reference 3-grams:  
the cat is, cat is on, is on the, on the mat

| trigram       | Candidate | Reference | Clipped |
|---------------|-----------|-----------|---------|
| the cat the   | 1         | 0         | 0       |
| cat the cat   | 1         | 0         | 0       |
| the cat on    | 1         | 0         | 0       |
| cat on the    | 1         | 0         | 0       |
| on the mat    | 1         | 1         | 1       |

Total clipped trigrams = 1  
Total candidate trigrams = 5

![p3](https://latex.codecogs.com/svg.image?\dpi{120}&space;p_3%20=%20\frac{1}{5}%20=%200.2)

---

## What is the BP in BLEU Formula? How to Calculate BP

**BP = Brevity Penalty**

**BP formula:**

When \( c > r \):

![BP1](https://latex.codecogs.com/svg.image?\dpi{120}&space;BP=1)

When \( c <= r \):

![BP2](https://latex.codecogs.com/svg.image?\dpi{120}&space;BP=\exp\left(1-\frac{r}{c}\right))

Where:  
- \( c \) = length of candidate sentence  
- \( r \) = effective reference length (can be the closest reference length to candidate, or just reference length if only one)

**Example:**  
Candidate length (\( c \)) = 7  
Reference length (\( r \)) = 6  

Since \( c > r \), BP = 1

If the candidate was "the cat on mat" (\( c = 5 \)), then:

![BP example](https://latex.codecogs.com/svg.image?\dpi{120}&space;BP=%20\exp\left(1-%20\frac{6}{5}\right)%20=%20\exp(-0.2)%20\approx%200.8187)

---

## Final BLEU Value Calculation (up to 3-gram, uniform weights)

For up to 3-gram (\( N=3 \)), uniform weights (\( w_n = \frac{1}{3} \)):

![BLEU final](https://latex.codecogs.com/svg.image?\dpi{120}&space;\text{BLEU}%20=%201%20\times%20\exp\left(\frac{1}{3}%20(\log%200.714%20+%20\log%200.5%20+%20\log%200.2)\right)%20=%20\exp\left(\frac{1}{3}%20\times%20(-2.639)\right)%20=%20\exp(-0.879)%20\approx%200.415)

---

## Summary Table

| n-gram | Precision (\( p_n \)) |
|--------|-----------------------|
| 1      | 0.714                 |
| 2      | 0.5                   |
| 3      | 0.2                   |

**BLEU = BP × exp(mean log precision) ≈ 0.415**

---

## References

- Original BLEU paper: [Papineni et al., 2002](https://www.aclweb.org/anthology/P02-1040/)
- [BLEU on Wikipedia](https://en.wikipedia.org/wiki/BLEU)