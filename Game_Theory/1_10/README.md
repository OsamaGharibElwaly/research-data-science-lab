# Game Theory 101 — Comprehensive Study Document
**Based on: Game Theory 101 complete course, Videos 1–10 (William Spaniel series)**
*A compact university-textbook-style chapter. Note on accuracy: these videos are an introductory sequence on the normal (strategic) form; where I add standard game-theoretic knowledge beyond the videos, connections to other fields, or new examples, this is flagged as **[Beyond video]** or **[Added example]**. Nothing is invented from the instructor.*

---

## Part 0 — Orientation

### Learning Roadmap

The 10 videos build a single logical arc:

```
Game & strategy basics (V1) → Dominance (V2) → Iterated dominance (V3)
→ Nash equilibrium, pure (V4, V5) → Best responses (V6)
→ Nash equilibrium, mixed (V7) → Solving mixed equilibria algorithmically (V8)
→ Precision with mixed equilibria (V9) → Coordination games & multiple equilibria (V10)
```

The end state of Videos 1–10: given **any two-player, finite, normal-form game**, you can (1) describe it formally, (2) eliminate dominated strategies, (3) find pure-strategy Nash equilibria by best-response inspection, and (4) compute mixed-strategy Nash equilibria with the indifference algorithm — and, critically, you can *interpret* what those equilibria mean and what they do **not** mean.

### Concept Dependencies

| Concept | Depends on |
|---|---|
| Strict dominance (V2) | Games, strategies, payoffs (V1) |
| Iterated elimination (V3) | Strict dominance (V2) |
| Pure-strategy Nash equilibrium (V4–V5) | Best responses (V6 conceptually; V6 formalizes the tool used in V4–V5) |
| Mixed strategies (V7) | Pure NE; probability & expected utility (V1 payoff idea generalized) |
| Mixed-strategy algorithm (V8) | Indifference principle (V7), algebra of expected values |
| Proper NE notation (V9) | Everything above |
| Battle of the Sexes (V10) | Multiple pure NE + mixing; coordination logic (Stag Hunt, V4) |

### Prerequisites

* **Basic algebra**: solving linear equations (essential for V7–V8).
* **Probability**: a randomization that plays A with probability $p$ and B with $1-p$; expected value of a lottery.
* **Optimization intuition**: a rational player picks the strategy that maximizes payoff *given beliefs about others* — game theory is multi-person optimization, not single-person optimization.
* No calculus is needed for Videos 1–10.

### Key Concepts Covered

Game, player, strategy (pure/mixed), normal form, payoff matrix, strict dominance, iterated elimination of strictly dominated strategies (IESDS), best response, pure-strategy Nash equilibrium, mixed-strategy Nash equilibrium, indifference principle, expected utility, coordination games, multiple equilibria (Stag Hunt, Battle of the Sexes), and the "mutual best response" interpretation of equilibrium.

---

## Video 1 — Introduction

### Core Concepts
Game theory is the formal study of strategic interaction: situations where the outcome for *you* depends on the choices of *others*, and their outcomes depend on your choice. The videos focus on the **normal (strategic) form**: a simultaneous-move game represented by a payoff matrix.

### Important Definitions
* **Game**: a formal description of players, their available strategies, and the payoffs each combination of strategies produces.
* **Player**: a decision-maker $i \in \{1, 2, \dots, n\}$.
* **Strategy**: a complete plan of action. In these videos, a pure strategy is one definite choice.
* **Payoff**: a number (utility) $u_i(s_1, s_2)$ summarizing how much player $i$ likes outcome $(s_1, s_2)$. **Crucially: bigger is better; payoffs are *ordinal/utility* summaries, not necessarily money.**
* **Normal form**: the game as a matrix/table of payoffs, assuming moves are effectively simultaneous (no one can condition on having observed the other's move).

### Intuition — "What does this really mean?"
Everyday decisions become games the moment your best choice depends on what someone else will do (pricing against a competitor, merging into traffic, nuclear deterrence). Game theory gives a *language* (players, strategies, payoffs) and a *solution standard* (what outcomes are stable when everyone is rational). The payoff matrix is not just bookkeeping — it is a complete model of the incentives, so almost all the analytical power of the field comes from building the right matrix.

### Mathematical Formulation
A two-player normal-form game is a triple
$$G = \langle N, (S_i)_{i \in N}, (u_i)_{i \in N} \rangle$$
where $N = \{1, 2\}$, $S_1, S_2$ are strategy sets, and $u_i : S_1 \times S_2 \to \mathbb{R}$ maps strategy profiles to payoffs. A **strategy profile** is $s = (s_1, s_2) \in S_1 \times S_2$.

*Symbols: $N$ — set of players; $S_i$ — player $i$'s strategy set; $s_i$ — one of player $i$'s strategies; $u_i$ — player $i$'s utility function; $\times$ — Cartesian product (all ordered pairs of strategies).*

### Step-by-Step Example
Prisoner's Dilemma (payoff pairs are written *(row, column)*, the convention used throughout the course):

|  | C | D |
|---|---|---|
| **C** | 3, 3 | 0, 5 |
| **D** | 5, 0 | 1, 1 |

### Real-World Applications
Arms races, price wars, doping in sports, overfishing (the "tragedy of the commons" is a multi-player dilemma), and advertising budgets are all Prisoner's-Dilemma-shaped: individually rational defection leads to collectively worse outcomes.

### Common Mistakes
* Confusing **payoffs** with **money** — payoffs model preferences.
* Thinking games require literal simultaneous moves; what matters is that neither player can condition on the other's observed action.
* Reading the matrix from the wrong player's perspective (always check whose payoff is listed first — here, row first).

### Key Takeaways
* A game = players + strategies + payoffs.
* Normal form handles simultaneous moves.
* Payoff numbers encode *everything* about preferences that matters for strategic analysis.

---

## Video 2 — The Prisoner's Dilemma and Strict Dominance

### Core Concepts
Some strategies are so bad that *no belief* about the opponent can justify playing them. If one strategy always yields a strictly worse payoff than another, **regardless** of what the opponent does, it is **strictly dominated** — and a rational player never plays it.

### Important Definitions
* Strategy $s_i'$ is **strictly dominated** by $s_i$ if $u_i(s_i, s_{-i}) > u_i(s_i', s_{-i})$ for **every** strategy $s_{-i}$ of the opponent. ($s_{-i}$ = "the strategy profile of everyone except player $i$", standard notation.)
* A **strictly dominant** strategy strictly beats every alternative against every opponent strategy.

### Intuition
Strict dominance is an extremely strong argument: it requires no guesswork about the other player, no assumption that they are rational, no equilibrium reasoning. "Whatever they do, I'd be better off doing X" eliminates everything else. This is why the Prisoner's Dilemma's outcome is so robust — and so unsettling.

### Mathematical Formulation
In the PD matrix above, for the row player:
* vs. C: $u_1(D, C) = 5 > 3 = u_1(C, C)$
* vs. D: $u_1(D, D) = 1 > 0 = u_1(C, D)$

Both inequalities are strict → **D strictly dominates C** (and symmetrically for the column player). Note the definition must hold for *all* columns; one failure breaks strict dominance.

### Strategic Analysis
* Players: two prisoners (or firms, nations, athletes).
* Actions: Cooperate / Defect.
* Payoffs: mutual cooperation best jointly (3,3), but D is each player's individual best response to either opponent choice.
* Incentives: defect is the **dominant strategy** for both.
* Solution: $(D, D)$ with payoff $(1,1)$ — strictly worse for both than $(C, C)$.

**Why rational players choose D:** because D is best *whatever the other does*, rationality *alone* (no mind-reading, no trust) forces D. The dilemma is that this ironclad individual logic produces a collectively poor outcome. This is the foundational tension game theory exposes: **individual rationality ≠ collective optimality**.

### Real-World Application **[Added example]**
*Players:* two smartphone makers. *Strategies:* moderate advertising budget vs. aggressive budget. *Payoffs:* if both moderate, each keeps high margins (3,3); if one goes aggressive it steals share (0,5 / 5,0); if both go aggressive, margins collapse (1,1). *Game:* Prisoner's Dilemma. *Solution:* both aggressive. *Interpretation:* the advertising war is individually rational but destroys joint profit — explaining why collusion/cartels tempt firms and why regulators watch "wasteful" competitive spending. *Limitation:* real firms repeat the game (future videos/chapters), discounting, and incomplete information complicate the one-shot logic.

### Common Mistakes
* Claiming "players should cooperate because (C,C) is better for both" — dominance reasoning shows why they *won't* without enforcement.
* Using $\geq$ instead of $>$ : if two strategies ever *tie*, strict dominance fails (weak dominance is a different, weaker tool — **[Beyond video]**).

### Key Takeaways
* Strict dominance: better against *every* opponent strategy, with strict inequality everywhere.
* A strictly dominated strategy is never a rational choice; a strictly dominant strategy always is.
* PD shows individually rational play can be collectively disastrous.

---

## Video 3 — Iterated Elimination of Strictly Dominated Strategies

### Core Concepts
Dominance logic compounds. If I eliminate your dominated strategies, some of *my* strategies may become dominated in the *reduced* game — which may eliminate more of yours, and so on. This **iterated elimination of strictly dominated strategies (IESDS)** can shrink a game to a single prediction.

### Important Definitions
**IESDS procedure**: (1) find all strictly dominated strategies; (2) delete them; (3) repeat on the smaller game until no strictly dominated strategies remain. The surviving profiles are those consistent with **common knowledge of rationality** (everyone is rational, everyone knows everyone is rational, everyone knows that, ad infinitum).

### Intuition
Each round of elimination encodes one deeper layer of "I know that you know that I know..." rationality. IESDS is a sieve: the first pass removes strategies a *merely* rational player wouldn't use; the second removes strategies a rational player wouldn't use *against a rational opponent*; and so on. When the sieve leaves exactly one cell, dominance reasoning *alone* (no equilibrium concept) solves the game.

### Step-by-Step Numerical Example **[Added example]**
Row player: U, M, D. Column player: L, C, R.

|  | L | C | R |
|---|---|---|---|
| **U** | 4,3 | 5,1 | 6,2 |
| **M** | 2,1 | 8,4 | 3,6 |
| **D** | 3,0 | 9,6 | 2,8 |

*Round 1:* For the column player, C is strictly dominated by R? Check vs. U: R gives 2, C gives 1 ✔; vs. M: 6 > 4 ✔; vs. D: 8 > 6 ✔ → **delete C**.
*Round 2:* In the reduced game (columns L, R): for the row player, M vs U: vs. L, 2 < 4; D vs U: vs. L, 3 < 4 → M and D are dominated by U (vs. L: 4 > 2, 4 > 3; vs. R: 6 > 3, 6 > 2) → **delete M, D**. Only U remains.
*Round 3:* Column player now compares L vs R against U alone: 2 > 1 → **delete L**.
*Prediction:* $(U, R)$ with payoff $(6, 2)$.

Observe: M was eliminated only *after* C was deleted — it survived the first pass. Order-of-elimination subtleties exist **[Beyond video]**, but for strict dominance the surviving set is independent of the order eliminated — a standard result.

### Mathematical Statement
Common knowledge of rationality ⇒ players play only strategies surviving IESDS. **[Beyond video]** The converse also holds for two-player games: any strategy surviving IESDS is justifiable by some (possibly strange) higher-order beliefs about the opponent — this is the epistemic foundation of the procedure.

### Strategic Analysis
IESDS asks: what can we predict *before* invoking any equilibrium concept, using only "players are rational and this is common knowledge"? Answer: the IESDS survivor set. If it's a singleton, dominance reasoning solves the game completely.

### Real-World Application **[Added example]**
Bidding in a first-price auction with known valuations: bids above your valuation are strictly dominated (never profitable); once those are eliminated, other bids become dominated in the reduced game; iterating converges toward equilibrium bidding logic — an early taste of why auction theory (a later GT topic) is built on iterative reasoning.

### Common Mistakes
* Eliminating on the basis of one column only (dominance needs *all* columns).
* Forgetting that in later rounds you compare payoffs only in the *reduced* matrix.
* Believing IESDS always leaves one outcome — Stag Hunt and Battle of the Sexes will show games where dominance gets you nothing.

### Key Takeaways
* IESDS = repeated strict dominance on successively smaller games.
* It formalizes common knowledge of rationality.
* When it yields a unique profile, no equilibrium concept is needed at all.

---

## Video 4 — Pure Strategy Nash Equilibrium and the Stag Hunt

### Core Concepts
Dominance fails in many games. The central solution concept of game theory — the **Nash equilibrium** — instead asks a stability question: is there a profile where no one regrets their choice *given what others actually did*? The **Stag Hunt** illustrates both the concept and the problem of **multiple equilibria** and risk.

### The Stag Hunt Matrix
|  | Stag | Hare |
|---|---|---|
| **Stag** | 3, 3 | 0, 2 |
| **Hare** | 2, 0 | 2, 2 |

(Payoff story: a stag requires coordinated effort to catch; a hare can be caught alone. Mutual stag-hunting yields the biggest prize but leaves you with nothing if your partner defects to hare.)

### Important Definitions
* A **pure-strategy Nash equilibrium (PSNE)** is a strategy profile where each player's strategy is a **best response** to the others': $u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*)$ for all $s_i \in S_i$ and all $i$.
* **Payoff-dominant equilibrium**: the equilibrium best for *everyone* (here, (Stag, Stag) at (3,3)).
* **Risk-dominant equilibrium** **[Beyond video]**: the equilibrium you'd pick if you feared the other player might miscoordinate (here, (Hare, Hare): hare guarantees 2 regardless).

### Intuition — "What does this really mean?"
A Nash equilibrium is a **self-enforcing agreement**. No police, contract, or communication is required: at a Nash profile, each person looks at what happened and thinks "given what they did, I did the best I could — I'd choose the same again." Stag Hunt dramatizes the gap between *payoff dominance* and *safety*: hunting stag is better *if coordinated*, but hare insures you against a partner who fails to show up. Society's trust problem, formalized.

### Mathematical Formulation
Check each cell for profitable one-shot deviations:
* (Stag, Stag): row deviating to Hare gets 2 < 3. Hold. Column symmetric. Hold. → **PSNE**.
* (Hare, Hare): row deviating to Stag gets 0 < 2. Hold. → **PSNE**.
* (Stag, Hare): row gets 0; deviating to Hare gives 2 > 0 → **not** NE.
* (Hare, Stag): column similarly deviates → **not** NE.

Two pure equilibria: $(3,3)$ and $(2,2)$. The Pareto ranking does not select between them.

### Strategic Analysis
*Players:* two hunters. *Actions:* Stag / Hare. *Information:* simultaneous. *Best responses:* Stag is best only if partner plays Stag; Hare is best against Hare **and** against Stag (since 2 > 0) — hare is *safe*, not dominant (3 > 2 when both hunt stag). *Nash equilibria:* two, differing in both efficiency and risk. *Possible deviations:* at (Hare, Hare) nobody wants to deviate *unilaterally*, even though both would gain from a *coordinated* move to stag — the signature of a coordination failure.

### Real-World Applications
* Technology adoption with network effects: adopt the new standard (stag) only if partners also adopt **[Added example]**.
* International disarmament: disarming is best if the rival disarms; arming is safe otherwise.
* Teams choosing ambitious vs. safe project goals.

### Common Mistakes
* Assuming a better-for-everyone equilibrium must be played — Stag Hunt has no dominance logic that selects it.
* Confusing "no profitable *unilateral* deviation" with "no better outcome exists."

### Key Takeaways
* PSNE = mutual best responses; a self-enforcing resting point of strategic reasoning.
* Games can have zero, one, or several pure equilibria — multiplicity is a feature, not a bug.
* Stag Hunt: payoff dominance vs. risk/safety — the game of trust.

---

## Video 5 — What Is a Nash Equilibrium?

### Core Concepts
This video consolidates the definition and, importantly, the **interpretations** of Nash equilibrium and its **limitations**: equilibrium does not require that players consciously compute it; it is a *prediction/steady state*, and some games (e.g., Matching Pennies, Video 7) have **no** pure-strategy Nash equilibrium at all.

### Important Definitions
Restated formally: $s^* = (s_1^*, \dots, s_n^*)$ is a Nash equilibrium if for every player $i$ and every alternative strategy $s_i'$:
$$u_i(s_i^*, s_{-i}^*) \geq u_i(s_i', s_{-i}^*).$$

### Intuition
Three legitimate readings:
1. **No-regret / self-enforcement**: given the outcome, no one wishes they had acted differently unilaterally.
2. **Steady state of learning**: if the game is repeated and players adjust toward better responses, observed play may settle at a Nash profile.
3. **Focal prediction**: when players can coordinate expectations (by convention, communication, or symmetry), they may land on an equilibrium.

Equilibrium is **not** a claim that the outcome is good, fair, unique, or reached by conscious calculation. PD's (D,D) is a Nash equilibrium — and it's terrible for everyone.

### Mathematical Formulation & the Deviation-Checking Algorithm
A practical NE test (used constantly from here on):
1. Fix the opponent's strategy at the candidate cell.
2. Compute player $i$'s payoff in the cell and from each *deviation*.
3. If any deviation strictly improves $i$'s payoff → not NE.
4. Repeat for all players.

### Worked Example
PD: test (D,D). Row deviating to C: 0 < 1. Column: symmetric. (D,D) is NE — despite (C,C) being better for both. This is the definition doing real work: NE filters profiles for *individual stability*, not social optimality.

### Connections **[Beyond video]**
* **Economics**: competitive market equilibrium and Nash equilibrium of supply/demand decisions; oligopoly models (Cournot) are literally games solved for NE.
* **Optimization**: NE generalizes "optimize against fixed parameters" to "optimize against others who are optimizing."
* **Machine Learning / Multi-Agent AI**: multi-agent RL seeks (approximate) Nash policies; GAN training is a two-player game whose oscillations reflect the absence of pure equilibria in some settings.

### Common Mistakes
* "Equilibrium = best possible outcome." (No — it is *stable*, not optimal.)
* "Every game has exactly one pure NE." (No — zero, one, many are all possible.)
* "Players must know game theory to play Nash." (No — interpretations 2 and 3 allow convergence without calculation.)

### Key Takeaways
* NE = mutual best responses; the workhorse solution concept of the whole field.
* Checking NE is mechanical: rule out every profitable unilateral deviation.
* Pure NE may fail to exist — motivating mixed strategies (V7).

---

## Video 6 — Best Responses

### Core Concepts
Best responses are the *atom* of equilibrium analysis. A **best response** is the strategy (or set of strategies) maximizing a player's payoff *given a belief about the opponent's play*. Nash equilibrium is nothing more than a profile in which every strategy played is a best response to the others.

### Important Definitions
* $BR_i(s_{-i}) = \arg\max_{s_i \in S_i} u_i(s_i, s_{-i})$ — the set of strategies that maximize $i$'s payoff against $s_{-i}$.
* A profile $s^*$ is NE iff $s_i^* \in BR_i(s_{-i}^*)$ for every $i$.

### Intuition
"Best response" shifts the analytic question from *"what should I do?"* (which seems to require predicting the opponent) to *"what would I do for each possible opponent action?"* Once the full best-response mapping is laid out, equilibria are found by inspection — where the answers "cross." This is the same move calculus makes with derivatives, and the same move ML makes with argmax — and it converts equilibrium-finding into bookkeeping.

### Worked Example — Stag Hunt best-response table
* If column plays Stag: row's payoffs are Stag 3, Hare 2 → **BR = {Stag}**.
* If column plays Hare: Stag 0, Hare 2 → **BR = {Hare}**.
Symmetric for the column player. A cell is NE iff each label matches the actual action — (Stag,Stag) ✔ and (Hare,Hare) ✔.

### Worked Example — a game without pure NE **[Added example]**
Matching Pennies (introduced fully in V7): row wins if pennies match, column wins if they differ.

|  | H | T |
|---|---|---|
| **H** | 1, −1 | −1, 1 |
| **T** | −1, 1 | 1, −1 |

* If column plays H: row's BR = H. But at (H,H), column's BR = T (column wins on difference). At (H,T), row's BR = T. At (T,T), column's BR = H. At (T,H), row's BR = H. Around the cycle we go — **no cell is a mutual best response**. This is exactly why mixed strategies are needed.

### Strategic Analysis
Best responses make incentives explicit: a player's BR summarizes *everything* about how they react to others. Equilibrium existence, dominance (a strictly dominated strategy is never a BR), and the mixed-strategy algorithm of V8 all rest on the BR concept.

### Connections
* **Algorithms**: computing BRs is a linear scan over strategies — $O(|S_i|)$ per opponent profile; finding pure NE is then $O(|S_1||S_2|)$ cell inspections.
* **ML/RL**: a Q-learning agent updates toward the best-response action given others' current policies; "Nash" requires simultaneous best responses — a much stronger condition.

### Common Mistakes
* Confusing "best response to the opponent's equilibrium strategy" with "best response in general" — BRs are always *conditional*.
* Treating BR as unique; when ties occur, $BR$ is a set.

### Key Takeaways
* Best response = argmax of payoff given the opponent's (believed) action.
* NE ⟺ mutual best responses. Learn to see games as BR tables.
* Cycling BRs signal: no pure equilibrium — prepare to mix.

---

## Video 7 — Mixed Strategy Nash Equilibrium and Matching Pennies

### Core Concepts
When no pure equilibrium exists, rationality still offers a prediction: **randomize**. A **mixed strategy** assigns probabilities to pure strategies; players then maximize **expected utility**. In equilibrium of a two-player game, a player mixes *only over strategies that give equal expected payoff* — the **indifference principle** — because mixing something worse would be irrational.

### Important Definitions
* **Mixed strategy** $\sigma_i$: a probability distribution over $S_i$; $\sigma_i(s_i) \geq 0$, $\sum_{s_i} \sigma_i(s_i) = 1$.
* **Expected utility** of $\sigma_i$ against $\sigma_{-i}$: $U_i(\sigma_i, \sigma_{-i}) = \sum_{s} \sigma_i(s_i)\,\sigma_{-i}(s_{-i})\, u_i(s_i, s_{-i})$.
* **Mixed-strategy Nash equilibrium (MSNE)**: a profile of mixed strategies, each a best response to the others.

### Intuition
Matching Pennies is a guessing game: if the row player is predictable, the column player exploits them, and vice versa. The only stable play is **unpredictability** — randomize 50/50 — which makes the opponent indifferent, which removes their exploitable pattern. Equilibrium mixing is not indecision; it is the *optimal* level of unpredictability, enforced by the requirement that you not be exploitable.

### Mathematical Formulation — Matching Pennies
Row mixes H with probability $p$, T with $1-p$. Make column indifferent:
* Column's EU from H: $p(-1) + (1-p)(1) = 1 - 2p$.
* Column's EU from T: $p(1) + (1-p)(-1) = 2p - 1$.
Indifference: $1 - 2p = 2p - 1 \Rightarrow 4p = 2 \Rightarrow p = \tfrac{1}{2}$.
By symmetry (the game is symmetric and zero-sum), column also mixes H with probability $\tfrac{1}{2}$.

*Symbols: $p$ — probability row plays H; EU — expected utility; indifference equation — the heart of mixed equilibria.*

**Why must the mixer be indifferent?** If column strictly preferred H, she'd play H for sure — but then row would exploit that with H (matching), destroying the premise. Only when column is indifferent is her randomization itself a best response. This is the deepest single insight of the video: **in equilibrium, players randomize to make others indifferent; they themselves mix because they are indifferent.**

### Strategic Analysis
*Players:* two penny-flippers. *Actions:* H/T. *Information:* simultaneous; each wants to read the other. *Payoffs:* constant-sum (zero-sum: one wins what the other loses). *Best responses:* pure BRs cycle (V6). *Nash equilibrium:* unique, fully mixed, 50/50 each. *Deviations:* any bias in $p$ gives the opponent a strictly better response — equilibrium demands exact unpredictability.

### Real-World Applications
* Penalty kicks in soccer, tennis serve direction, bluffing frequencies in poker — any contest where predictability is punished **[Added example]**.
* Security patrol scheduling: randomize checkpoints so attackers cannot exploit a pattern.
* Rock-paper-scissors: the folk version of "unexploitability via mixing."

### Common Mistakes
* Believing mixing 50/50 is always optimal — the *equilibrium* mixture depends on payoffs (V8 shows non-50/50 mixing).
* Thinking "randomize" means "I don't care": mixing must leave opponents indifferent, which is a precise constraint, not apathy.
* Assuming a player mixes over a strictly dominated strategy — dominated strategies get probability 0.

### Key Takeaways
* MSNE exists even where PSNE fails (indeed, Nash's theorem **[Beyond video]** guarantees existence of *some* (possibly mixed) equilibrium in every finite game).
* Indifference principle: the mixing player must make the opponent indifferent among the strategies being mixed over.
* Matching Pennies: 50/50 each — the canonical anti-coordination game.

---

## Video 8 — The Mixed Strategy Algorithm

### Core Concepts
A mechanical procedure for finding MSNE in 2×2 games: **(1) guess which strategies each player mixes over; (2) write the opponent's indifference equations; (3) solve for the mixing probabilities; (4) verify.** The same four steps scale to larger games with more unknowns.

### The Algorithm
For a 2×2 game with row mixing $(p, 1-p)$ over {A, B} and column mixing $(q, 1-q)$ over {C, D}:
1. Row's mix $(p, 1-p)$ must make column indifferent between C and D: solve one linear equation in $p$.
2. Column's mix $(q, 1-q)$ must make row indifferent between A and B: solve one linear equation in $q$.
3. Check $0 < p, q < 1$ (a solution outside $[0,1]$ means the *guess about who mixes* was wrong — e.g., an equilibrium is pure, or mixing is over a different support).
4. Verify no player profits by deviating to an unused strategy.

### Worked Example **[Added example]**
|  | L | R |
|---|---|---|
| **U** | 2, 1 | 0, 0 |
| **D** | 0, 0 | 1, 2 |

Step 1 (column indifferent between L and R against row's mix $(p, 1-p)$ over U,D):
* EU_col(L) = $p(1) + (1-p)(0) = p$.
* EU_col(R) = $p(0) + (1-p)(2) = 2 - 2p$.
* $p = 2 - 2p \Rightarrow 3p = 2 \Rightarrow p = \tfrac{2}{3}$.

Step 2 (row indifferent between U and D against column's mix $(q, 1-q)$ over L,R):
* EU_row(U) = $2q$.
* EU_row(D) = $1 - q$.
* $2q = 1 - q \Rightarrow q = \tfrac{1}{3}$.

Step 3: both in $(0,1)$ ✔. Step 4: both pure strategies already included, and at these mixtures each player's EU is $\tfrac{2}{3}$; deviating outside the support is impossible (only two strategies each). **MSNE: row plays U with probability 2/3; column plays L with probability 1/3.**

**Notice the "crossing" pattern**: $p$ is pinned down by *column's* payoffs, and $q$ by *row's* payoffs. You solve for your own probability using the *opponent's* payoffs — this trips up nearly every beginner (see Video 9).

### Strategic Interpretation
Row mixes U two-thirds of the time because that exact frequency makes column's two options equally attractive — denying column any exploitable tendency. The equilibrium mixture is a *defensive* instrument even though players don't observe it being constructed.

### Computational Perspective **[Beyond video]**
* Each indifference equation is linear → MSNE computation in 2×2 games is closed-form.
* General games: NE computation is PPAD-complete (Daskalakis–Goldberg–Papadimitriou 2006) — believed intractable in the worst case; practical methods include support enumeration (try all subsets as candidate mixing supports — exponential but fine for small games), Lemke–Howson (for two-player games), and learning dynamics (fictitious play, no-regret algorithms).
* Pseudocode (support enumeration sketch):
```
for each support S1 ⊆ S_row, S2 ⊆ S_col with |S1|=|S2|:
    solve indifference + probability-sum equations for (σ1, σ2)
    if all probabilities in [0,1] and no outside deviation pays more:
        output MSNE candidate
```

### Common Mistakes
* Using row's own payoffs to solve for row's mixing probability (backwards!).
* Forgetting the support-size / verification step — solving equations can yield probabilities outside [0,1] or an exploitable outside deviation.
* Assuming both players must mix in *every* MSNE — asymmetric and boundary equilibria (some pure, some mixing) exist in larger games.

### Key Takeaways
* Four-step algorithm: guess support → indifference equations → solve → verify.
* Solve for $p$ using the *opponent's* payoffs.
* Verification is mandatory: probabilities must be valid and no deviation profitable.

---

## Video 9 — How NOT to Write a Mixed Strategy Nash Equilibrium

### Core Concepts
Precision matters. The video (in the spirit of the course's careful treatment) corrects a common sloppiness: writing down a MSNE with the wrong variables, wrong probabilities, or describing mixing when the equilibrium is actually pure. The lessons generalize into rules for correctly *reporting* equilibria.

### The Correct Statement of an MSNE
An MSNE is a **full profile of probability distributions** — one distribution per player — over their own strategies, e.g.:
$$\text{MSNE: } \sigma_1 = \left(\tfrac{2}{3}, \tfrac{1}{3}\right) \text{ over } (U, D); \qquad \sigma_2 = \left(\tfrac{1}{3}, \tfrac{2}{3}\right) \text{ over } (L, R).$$
Each number is *that player's* probability over *their own* strategies. The probability row assigns to U is chosen to make column indifferent — so a statement like "row plays U with the probability that makes row indifferent" is doubly wrong.

### Common Errors Enumerated
1. **Mislabeled variables**: solving for the probability of the wrong player's strategy, or writing "$p$ = probability column plays X" while $p$ was defined for the row player. *Fix*: define every variable at the start; solve for $p$ from the opponent's indifference equation.
2. **Confusing the mixing player with the indifferent player**: the player who *mixes* must make the *other* player indifferent. Writing "row mixes so that row is indifferent" inverts the logic.
3. **Probabilities not summing to 1** or falling outside $[0,1]$ — arithmetic slips that invalidate the "distribution."
4. **Calling a pure equilibrium "mixed"** (a strategy played with probability 1 is degenerate mixing; it's cleaner to report it as pure).
5. **Reporting only one player's mixture**: an equilibrium is a profile — both players' strategies (and payoffs) belong in the answer.

### Worked Precision Check
Using the V8 example: the correct full answer is
> Row: U with $p=\tfrac{2}{3}$, D with $1-p=\tfrac{1}{3}$. Column: L with $q=\tfrac{1}{3}$, R with $1-q=\tfrac{2}{3}$. Expected payoffs: row $=\tfrac{2}{3}$, column $=\tfrac{2}{3}$.

Verify the logic chain: $p=\tfrac23$ comes from *column's* indifference ($EU_{col}(L)=p$, $EU_{col}(R)=2-2p$); $q=\tfrac13$ from *row's* ($EU_{row}(U)=2q$, $EU_{row}(D)=1-q$). Expected payoffs: row: $2q = \tfrac23$; column: $p = \tfrac23$ (using column's EU expressions at the solution). Symmetric payoffs here are a coincidence of the example, not a rule.

### Key Takeaways
* An MSNE is a complete profile of distributions with valid probabilities.
* Mixing probabilities come from the *opponent's* indifference conditions.
* Presentation errors are concept errors: a wrong label usually signals inverted logic.

---

## Video 10 — Battle of the Sexes

### Core Concepts
The final video's game has **two pure-strategy Nash equilibria** plus a **mixed-strategy Nash equilibrium** — three equilibria in one small game — and the mixed equilibrium is *worse in expectation* than either pure one. It completes the course's tour: dominance → pure NE → mixed NE → games rich enough to contain all of the above simultaneously.

### The Matrix
|  | Ballet | Fight |
|---|---|---|
| **Ballet** | 3, 2 | 0, 0 |
| **Fight** | 0, 0 | 2, 3 |

(The classic story: two players want to coordinate on the same event, but each prefers a different one.)

### Pure-Strategy Nash Equilibria
Deviation check:
* (Ballet, Ballet): row deviating → 0 < 3; column deviating → 0 < 2. **PSNE.**
* (Fight, Fight): row deviating → 0 < 2; column deviating → 0 < 3. **PSNE.**
* Cross cells: someone always gets 0 and would deviate. Not equilibria.

### Mixed-Strategy Nash Equilibrium
Let row play Ballet with probability $p$; column play Ballet with probability $q$.

*Column indifferent* between Ballet and Fight (uses column's payoffs):
* EU_col(Ballet) = $p(2) + (1-p)(0) = 2p$.
* EU_col(Fight) = $p(0) + (1-p)(3) = 3 - 3p$.
* $2p = 3 - 3p \Rightarrow 5p = 3 \Rightarrow p = \tfrac{3}{5}$.

*Row indifferent* between Ballet and Fight (uses row's payoffs):
* EU_row(Ballet) = $3q$.
* EU_row(Fight) = $2 - 2q$.
* $3q = 2 - 2q \Rightarrow 5q = 2 \Rightarrow q = \tfrac{2}{5}$.

**MSNE: row mixes $(\tfrac35 \text{ Ballet}, \tfrac25 \text{ Fight})$; column mixes $(\tfrac25 \text{ Ballet}, \tfrac35 \text{ Fight})$.**

### Expected Payoffs in the MSNE
* Row: $3q = 3 \cdot \tfrac25 = \tfrac65 = 1.2$.
* Column: $2p = 2 \cdot \tfrac35 = \tfrac65 = 1.2$.

### Intuition — the shocking comparison
| Equilibrium | Row payoff | Column payoff |
|---|---|---|
| (Ballet, Ballet) | 3 | 2 |
| (Fight, Fight) | 2 | 3 |
| MSNE | 1.2 | 1.2 |

The mixed equilibrium is *worse for both players than either pure equilibrium* — coordination fails $\tfrac{6}{25}+\tfrac{6}{25} = \tfrac{12}{25}$ of the time (probability of miscoordination $= p(1-q) + (1-p)q = \tfrac35\tfrac35 + \tfrac25\tfrac25 = \tfrac{9}{25}+\tfrac{4}{25}$... careful: miscoordination is (Ballet, Fight) or (Fight, Ballet): $p(1-q) + (1-p)q = \tfrac35 \cdot \tfrac35 + \tfrac25 \cdot \tfrac25 = \tfrac{13}{25} = 52\%$). **[Added precision]** The lesson: *more equilibria is not more welfare.* Without a coordination device, players may be stuck at the worst of the three outcomes. This is the formal reason real institutions (contracts, conventions, communication, focal points) matter.

### Strategic Analysis
*Best responses:* each player's BR is to match the partner (Ballet against Ballet, Fight against Fight) — a pure coordination motive — but matching at one's *preferred* event pays more. *Equilibria:* two pure (asymmetric payoffs), one symmetric mixed (symmetric payoffs, miscoordination risk). *Deviations:* at the MSNE no one can profit by deviating — the indifference conditions guarantee it — yet the outcome is fragile: any asymmetry in beliefs destroys it.

### Real-World Applications
* Standards and platform choices: firms/users coordinate on a platform while preferring their own **[Added example]**.
* Bargaining over meeting times/venues; choosing project frameworks in joint ventures.
* Parking-lot chicken and traffic conventions: coordination games are everywhere conventions live.

### Common Mistakes
* Reporting only the two pure equilibria and missing the MSNE (or vice versa).
* Miscalculating miscoordination probability by adding the wrong cells.
* Believing symmetric payoffs in the MSNE mean it's "fair and good" — it's symmetric but bad.

### Key Takeaways
* One 2×2 game can contain three equilibria (2 pure + 1 fully mixed).
* The mixed equilibrium can be Pareto-dominated by pure equilibria.
* BoS + Stag Hunt + Matching Pennies = the three fundamental 2×2 archetypes: coordination-with-agreement, coordination-without-agreement-preference, and anti-coordination.

---

## Part 11 — Concept Integration

```text
Games & payoffs (V1)
   → strict dominance: eliminate strategies no belief can justify (V2)
   → IESDS: layer dominance into common knowledge of rationality (V3)
   → best responses: the atom of strategic reasoning (V6)
   → PSNE: mutual best responses → self-enforcing outcomes (V4, V5)
   → when BRs cycle (V6): pure NE fails → randomize (V7)
   → indifference principle → MSNE algorithm: solve, verify (V8)
   → precision in stating equilibria (V9)
   → archetype games reveal structure: PD (dominance), Stag Hunt/BoS
     (coordination & multiplicity), Matching Pennies (mixing)
```

How the material builds toward advanced Game Theory: finite normal-form games are the base layer. Next steps the videos set up: **extensive form & backward induction** (timing), **repeated games** (PD cooperation via shadow of the future), **incomplete information / Bayesian games** (uncertainty about payoffs/types), **mechanism design and auctions** (designing games with desired equilibria), and **evolutionary game theory** (population play as a dynamic).

---

## Part 12 — Master Summary

### Formula Sheet
| Concept | Formula/Condition | Meaning |
|---|---|---|
| Strict dominance | $u_i(s_i, s_{-i}) > u_i(s_i', s_{-i}) \ \forall s_{-i}$ | $s_i$ beats $s_i'$ against everything |
| Expected utility | $U_i(\sigma) = \sum_s \prod_j \sigma_j(s_j)\, u_i(s)$ | Weighted average over random outcomes |
| Best response | $BR_i(s_{-i}) = \arg\max_{s_i} u_i(s_i, s_{-i})$ | Optimal action given the others |
| Pure NE | $u_i(s_i^*, s_{-i}^*) \geq u_i(s_i', s_{-i}^*) \ \forall i, s_i'$ | Mutual best responses |
| Indifference (mixing) | $U_{-i}(s_a, \sigma_i) = U_{-i}(s_b, \sigma_i)$ | Opponent indifferent ⇒ they can mix |
| 2×2 MSNE algorithm | solve opponent's EU equality for your probability; verify | Mechanical equilibrium finder |

### Glossary
* **Strategy profile**: one strategy per player, $s = (s_1, s_2)$.
* **Strictly dominated**: always strictly worse, whatever others do.
* **IESDS**: repeatedly delete strictly dominated strategies.
* **Best response**: payoff-maximizing action given the others' play.
* **Nash equilibrium**: profile of mutual best responses; no profitable unilateral deviation.
* **Mixed strategy**: probability distribution over pure strategies.
* **Indifference principle**: a mixer must make the opponent indifferent over the mixed support.
* **Payoff- vs risk-dominance**: best-if-coordinated vs safest choice.
* **Zero-sum game**: payoffs sum to a constant; one player's gain is the other's loss.

### Comparison Tables
**Easily confused concepts:**

| Pair | Key difference |
|---|---|
| Dominant strategy vs. NE strategy | Dominant = best vs *all*; NE = best vs *the equilibrium profile of others* |
| Pure vs. mixed NE | Deterministic choice vs. probability distribution; existence guaranteed only with mixing allowed |
| Stag Hunt vs. Battle of the Sexes | Both coordination games; Stag: same preferred outcome (trust issue); BoS: conflicting preferred outcomes |
| Best response vs. equilibrium | BR is a reaction function; equilibrium is a fixed point of all BRs simultaneously |
| Payoff dominance vs. risk dominance | Efficiency vs. safety under strategic uncertainty |

**The three archetype 2×2 games:**

| Game | Structure | Equilibria | Lesson |
|---|---|---|---|
| Prisoner's Dilemma | Dominance | 1 pure | Individual rationality ≠ collective good |
| Stag Hunt | Coordination | 2 pure | Trust & risk |
| Battle of the Sexes | Coordination + conflict | 2 pure + 1 mixed | Institutions for coordination |
| Matching Pennies | Anti-coordination (zero-sum) | 1 mixed | Unpredictability as equilibrium |

### Top 10 Conceptual Insights
1. A game is fully specified by players, strategies, and payoffs — the matrix *is* the model.
2. Strict dominance requires no assumptions about opponents; equilibrium reasoning requires minimal ones.
3. IESDS formalizes common knowledge of rationality.
4. Nash equilibrium = no profitable unilateral deviation; stable ≠ optimal.
5. Best responses are the atom; equilibria are their fixed points.
6. Pure NE need not exist; randomization rescues existence (Nash's theorem).
7. Mixing is a weapon: make the opponent indifferent so they cannot exploit you.
8. In 2×2 MSNE, solve for *your* probability from the *opponent's* payoffs.
9. Multiplicity (Stag Hunt, BoS) is real: equilibrium selection is a separate, deep problem.
10. The mixed equilibrium of BoS is worse for everyone — institutions, conventions, and communication exist to escape bad equilibria.

### Reusable Problem-Solving Framework
```
1. FORMALIZE: players, strategies, payoffs → matrix.
2. SIMPLIFY: strict dominance? IESDS? (If unique survivor → done.)
3. BEST-RESPOND: build BR table / check each cell for deviations → pure NE.
4. MIX (if no/further equilibria exist): guess supports → opponent indifference
   equations → solve probabilities → CHECK p,q ∈ [0,1] → verify no deviation.
5. REPORT: full profile + payoffs; label pure vs mixed.
6. INTERPRET: stability, efficiency, risk; then map to the real world.
```

---

## Part 13 — Practice

### Conceptual Questions
**Q1.** Why does the Prisoner's Dilemma's (D,D) outcome persist even if both players are perfectly altruistic toward the *group*? Or does it? Explain carefully.
**Q2.** In the Stag Hunt, why is hunting hare *not* a dominant strategy even though it's the safe choice?
**Q3.** Give a real situation that is BoS-shaped rather than Stag-Hunt-shaped, and explain what distinguishes them.
**Q4.** "A Nash equilibrium is where players cannot improve by *changing strategies*." What's wrong with omitting the word *unilaterally*?
**Q5.** Why must a mixing player make the *opponent* indifferent rather than themselves?

### Mathematical Problems
**Q6.** Show via deviation checks whether the following game has pure NE: row {U,D}, column {L,R}; payoffs (U,L)=(4,4), (U,R)=(1,3), (D,L)=(3,1), (D,R)=(2,2).
**Q7.** Find the MSNE of the game: (U,L)=(3,0), (U,R)=(0,1), (D,L)=(0,1), (D,R)=(1,0). [Check: it's like matching pennies with bias.]
**Q8.** In the V8 example game, verify that no pure strategy is a best response to the opponent's equilibrium mixture — i.e., confirm both players are exactly indifferent at the MSNE.
**Q9.** Construct a 2×2 game where one player has a strictly dominant strategy and the other does not; find the unique NE.
**Q10.** In Matching Pennies, suppose row wins 2 (column loses 2) on a match of H but only 1 on a match of T (asymmetry). Find the MSNE — what is each player's expected payoff?

### Applied Problems
**Q11.** **Supply chain:** two suppliers choose simultaneously whether to invest in capacity (High/Low). Payoffs (millions): both High (5,5); one High one Low: High gets 1, Low gets 8; both Low (3,3). Identify the game archetype, all NE, and advise a manager.
**Q12.** **Security:** a guard patrols Left or Right; an intruder attacks Left or Right. If they meet, intruder is caught (−5 for intruder, +5 guard); if not, intruder succeeds (+10 intruder, −10 guard). Find the optimal patrol/attack mix and the value of the game.
**Q13.** **Product launch:** two firms simultaneously choose launch region (A or B). If both choose A: (2,1); both B: (1,2); split: (0,0). Find all equilibria and the probability of miscoordination under the MSNE; discuss a contractual fix.

### Challenging Problems
**Q14.** **Three equilibria, one mixed-support trap.** In BoS (V10), show there is no MSNE in which a player mixes over only one pure strategy with probability 1 (degenerate) *other than* the two pure equilibria — i.e., confirm the MSNE found is the unique non-degenerate one.
**Q15.** **Design question:** modify the BoS payoffs (keeping coordination payoffs positive and miscoordination zero) so that the mixed equilibrium's miscoordination probability *exceeds* 50%. Derive the general condition on the payoff matrix for miscoordination probability > ½ in the fully mixed equilibrium.

### Hints
*H6.* Check all four cells; look for a dominated strategy first.
*H7.* Two indifference equations; watch the asymmetry — the answer is not 50/50.
*H8.* Plug $p=\tfrac23, q=\tfrac13$ into EU expressions; both pairs must be equal.
*H10.* Write column's EU for H vs T using row's mix $(p,1-p)$; asymmetry shifts $p$ away from ½; compute row's payoff at the solution.
*H12.* Zero-sum → guard maximizes minimum; equalize the intruder's payoffs across targets. Expected payoff of game = value.
*H14.* A "mix" with a 1 or 0 probability collapses to a pure strategy; deviation-check pure cells only.
*H15.* Miscoordination probability is $p(1-q)+(1-p)q$; express it in terms of the four payoff entries and impose > ½.

### Solutions

**S6.** Check (U,L): row deviating to D: 3 < 4 ✔; column deviating to R: 3 < 4 ✔ → **NE (4,4)**. Check others: (U,R): column deviates to L (4 > 3) ✗. (D,L): row deviates to U (4 > 3) ✗. (D,R): row deviates (4 > 2) ✗. Unique PSNE (U,L).

**S7.** Row mixes U with $p$: column's EU(L) = $p(0)+(1-p)(1) = 1-p$; EU(R) = $p(1)+(1-p)(0) = p$. Indifference: $1-p = p \Rightarrow p = \tfrac12$. Column mixes L with $q$: row's EU(U) = $3q$; EU(D) = $1-q$. $3q = 1-q \Rightarrow q = \tfrac14$. MSNE: row (½,½), column (¼,¾). (Biased matching pennies: column should lean R.)

**S8.** At $p=\tfrac23$: column's EU(L) = $\tfrac23$; EU(R) = $2 - 2\cdot\tfrac23 = \tfrac23$ — equal ✔. At $q=\tfrac13$: row's EU(U) = $\tfrac23$; EU(D) = $1-\tfrac13 = \tfrac23$ — equal ✔. Both players indifferent between their two strategies, so any mixture (including the equilibrium one) is a best response — consistent.

**S9.** Example: (U,L)=(3,1),(U,R)=(3,0),(D,L)=(2,1),(D,R)=(4,0)? Check U vs D for row: vs L: 3>2 ✔; vs R: 3<4 ✗ — no dominance there. Correct construction: (U,L)=(3,0),(U,R)=(2,1),(D,L)=(1,0),(D,R)=(0,1). Row: U vs D: vs L 3>1 ✔; vs R 2>0 ✔ → U strictly dominant. Column has none (vs U prefer R: 1>0; vs D prefer R: 1>0 — actually R dominant here too). Adjust: make column's best depend on row: (U,L)=(3,1),(U,R)=(2,0),(D,L)=(1,0),(D,R)=(0,1). Row: U vs D: 3>1, 2>0 → U dominant. Column: vs U prefer L (1>0); vs D prefer R (1>0) → no dominant. IESDS: delete D (dominated); column best-responds L; unique NE (U,L) payoff (3,1).

**S10.** Row mixes H with $p$. Column EU(H) = $p(-2) + (1-p)(1) = 1 - 3p$; EU(T) = $p(1) + (1-p)(-1) = 2p - 1$. Set equal: $1 - 3p = 2p - 1 \Rightarrow p = \tfrac25$. Row's EU(H) vs column mix $(q, 1-q)$: EU(H) = $2q - (1-q) = 3q - 1$; EU(T) = $-q + (1-q) \cdot 1 \cdot (-1)$... compute directly: row's EU(T) = $q(-1) + (1-q)(1) = 1 - 2q$. Indifference: $3q - 1 = 1 - 2q \Rightarrow q = \tfrac25$. MSNE: both play H with probability 2/5. Expected payoff: row = $3q - 1 = \tfrac15$; column = $-(3q-1)$-related: column's EU(H) at $p=\tfrac25$: $1 - \tfrac65 = -\tfrac15$. Sum = 0 ✔ (zero-sum).

**S11.** Matrix: (H,H)=(5,5),(H,L)=(1,8),(L,H)=(8,1),(L,L)=(3,3). Check dominance: vs H, L gives 8>5; vs L, L gives 3<... wait, for a player: vs opponent H: L→8 > H→5; vs opponent L: H→1 < L→3. No dominant. Check cells: (H,H): deviate to L → 8 > 5 ✗ not NE... wait, deviating player at (H,H) who switches to L gets 8 > 5 → profitable → (H,H) NOT NE. (L,L): deviate to H → 1 < 3 ✔ hold for both → **NE (3,3)**. (H,L): row at L switching to H? Row plays H already... (H,L): row=H gets 1; deviating to L gives 3 > 1 ✗. (L,H): symmetric ✗. Unique NE (L,L)! It's a Prisoner's-Dilemma-like structure (investment is dominated in effect... check strict dominance properly: is H strictly dominated by L? vs H: 8 > 5 ✔; vs L: 3 > 1 ✔ → **L strictly dominates H**!). Yes — underinvestment equilibrium, classic. Advice: contracts/repeated interaction to sustain (H,H).

**S12.** Payoffs (guard, intruder): meet at target: (5,−5); miss: (−10,10). Guard mixes Left with $p$. Intruder's EU(attack L) = $p(-5) + (1-p)(10) = 10 - 15p$; EU(attack R) = $p(10) + (1-p)(-5) = 15p - 5$. Equal: $10 - 15p = 15p - 5 \Rightarrow p = \tfrac12$. By symmetry intruder attacks each side with probability ½. Value of game: intruder's EU = $10 - 15(\tfrac12) = 2.5$ > 0 — the intruder has the advantage in these numbers; guard's expected payoff = −2.5. Policy insight: change payoffs (detection tech) or patrol more targets.

**S13.** This is BoS. Equilibria: (A,A) payoff (2,1), (B,B) payoff (1,2), MSNE: column indifferent: EU_col(A) = $p(1)$; EU_col(B) = $(1-p)(2) = 2-2p$ → $p = 2-2p \Rightarrow p=\tfrac23$. Row indifferent: EU_row(A) = $2q$; EU_row(B) = $(1-q)(1) = 1-q$ → $q = \tfrac13$. MSNE: row (⅔A), column (⅓A). Miscoordination probability = $p(1-q) + (1-p)q = \tfrac23\tfrac23 + \tfrac13\tfrac13 = \tfrac59 ≈ 56\%$. Contractual fix: alternating preference, side payment, or commitment device.

**S14.** A degenerate "mix" is a pure strategy. The only pure NE are (Ballet,Ballet) and (Fight,Fight) (deviation checks in V10). Any non-degenerate mixture must put positive probability on both own strategies; then the opponent must be indifferent between both of theirs — the V10 computation is the unique solution $(p,q)=(\tfrac35,\tfrac25)$ — hence the unique fully mixed NE.

**S15.** Let (B,B) = (a,b) row,col payoffs; (F,F) = (c,d); miscoordination = 0. Column indifference: $p \cdot b = (1-p) \cdot d \Rightarrow p = \tfrac{d}{b+d}$. Row indifference: $q \cdot a = (1-q) \cdot c \Rightarrow q = \tfrac{c}{a+c}$. Miscoordination probability: $P_{mis} = p(1-q) + (1-p)q = \tfrac{bd + ac}{(a+c)(b+d)}$. Condition $P_{mis} > \tfrac12$ ⟺ $2(bd + ac) > (a+c)(b+d) = ab + ad + bc + cd$ ⟺ $2bd + 2ac - ab - ad - bc - cd > 0$ ⟺ $(a - d)(c - b) + (ad - ... )$ — cleanest form: $bd + ac > \tfrac12(ab + ad + bc + cd)$. Example: a=b=c=d=1 gives $P_{mis} = \tfrac12$; making b=d large and a,c small (e.g., a=c=1, b=d=3): $p = \tfrac{3}{6}=\tfrac12$, $q=\tfrac12$, $P_{mis} = \tfrac12$. Try a=1,c=3 (row prefers F), b=3,d=1 (column prefers B): $p = \tfrac{1}{4}$, $q = \tfrac34$, $P_{mis} = \tfrac14\cdot\tfrac14 + \tfrac34\cdot\tfrac34 = \tfrac{10}{16} = \tfrac58 > \tfrac12$ ✔. General lesson: when each player prefers the *other's* favorite event more strongly than their own... precisely, miscoordination exceeds ½ when preferences are "crossed" strongly enough: $(c - a)(b - d) > 0$ is not sufficient alone — the boxed inequality is the condition.

### Active-Recall Questions (15–20)
1. State the three components that fully define a game.
2. Write the strict-dominance inequality and explain each symbol.
3. Why is $(D,D)$ in PD a Nash equilibrium *despite* being Pareto-dominated?
4. What assumption does IESDS encode beyond "players are rational"?
5. Define best response; define NE in terms of best responses.
6. Why does Matching Pennies have no pure NE? Trace the cycle.
7. State the indifference principle in one sentence.
8. In a 2×2 MSNE, whose payoffs do you use to solve for the row player's mixing probability?
9. List the three equilibria of Battle of the Sexes and each expected payoff.
10. Which equilibrium of Stag Hunt is risk-dominant, and why might players end up there?
11. What does it mean that the MSNE of BoS is "worse for everyone," and what real-world institutions does this justify?
12. Give the verification checklist after solving a mixed equilibrium.
13. Why can't a strictly dominated strategy be played with positive probability in any NE?
14. Compare payoff dominance and risk dominance with a one-line example each.
15. What is the computational complexity status of finding NE in general games (name the class)?
16. In zero-sum games, what is the "value of the game"?
17. Convert this to a payoff matrix: two cafes simultaneously choose price High/Low; High/High → (4,4); High/Low → (1,5); Low/High → (5,1); Low/Low → (2,2). Then solve.
18. What are the next topics this course naturally leads to (list four)?
19. Why is "equilibrium" not a synonym for "good outcome"?
20. Explain why mixing must leave the *opponent* indifferent, using the exploitability argument.

---

*End of Part 1 of the Game Theory study series (Videos 1–10). Bring the next 10 titles/transcripts to continue.*
