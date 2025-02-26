---
title: "Initial Guess Generation for Low-Thrust Trajectory Design with Robustness to Missed-Thrust-Events"
collection: publications
permalink: /publication/2025-01-25-initial-guess
excerpt: 'We propose a novel initial guess generation strategy for missed thrust design which leverages solutions from problems with lower problem complexity, demonstrating superior convergence properties relative to conventional global search methods in high-dimensional nonlinear programs.'
date: 2025-01-25
venue: 'Journal of Guidance, Control, and Dynamics (submitted)'
paperurl: 'https://arxiv.org/abs/2501.06694'
citation: 'Sinha, Amlan, and Beeson, Ryne. (2024). "Initial Guess Generation for Low-Thrust Trajectory Design with Robustness to Missed-Thrust-Events." <i>arXiv preprint</i>. arXiv:2501.06694.'
---

<div style="text-align: center">
    <img src="/images/papers/initial-guess/initial-guess-schematic.png" alt="Conditional Global Search" style="width: 600px; max-width: 100%;"/>
    <p><em>Conditional Global Search</em></p>
</div>

Preliminary mission design requires efficient solution frameworks for exploring the solution space on a rapid cadence under evolving operational constraints. Contemporary methods for missed thrust design rely on high-dimensional nonlinear programming, where the generation of effective initial conditions presents a significant computational challenge. In this paper, we compare two initial guess generation strategies: a *conventional global search* approach which samples initial guesses from an a-priori chosen static distribution, and a novel *conditional global search* which leverages solutions from simpler problems with lower robustness requirements. The latter allows for a hierarchical search strategy for solving increasingly difficult missed thrust design problems. Validation studies demonstrate that our methodology yields substantial improvements in both convergence rates and solution quality, establishing its efficacy for preliminary robust trajectory design applications.
