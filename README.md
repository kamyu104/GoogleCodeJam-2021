# [GoogleCodeJam 2021](https://codingcompetitions.withgoogle.com/codejam) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-20%20%2F%2022-ff69b4.svg)

Python solutions of Google Code Jam 2021. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

* [Code Jam 2020](https://github.com/kamyu104/GoogleCodeJam-2020)
* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2021#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2021#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2021#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2021#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2021#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2021#round-2)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Reversort](https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c)| [Python](./Qualification%20Round/reversort.py)| _O(N^2)_ | _O(1)_ | Easy | | Simulation |
|B| [Moons and Umbrellas](https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145)| [Python](./Qualification%20Round/moons_and_umbrellas.py)| _O(N)_ | _O(1)_ | Easy | | DP |
|C| [Reversort Engineering](https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7)| [Python](./Qualification%20Round/reversort_engineering.py) [Python](./Qualification%20Round/reversort_engineering2.py)| _O(N)_ | _O(1)_ | Easy | | Greedy |
|D| [Median Sort](https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1284)| [Python](./Qualification%20Round/median_sort.py) |  _O(N^2)_ | _O(1)_ | Medium | | Ternary Search, Insertion Sort |
|E| [Cheating Detection](https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155)| [Python](./Qualification%20Round/cheating_detection.py) [Python](./Qualification%20Round/cheating_detection2.py) [Python](./Qualification%20Round/cheating_detection3.py) [Python](./Qualification%20Round/cheating_detection4.py) |  _O(S * Q)_ | _O(S + Q)_ | Hard | | Uniform Distribution, Inversions Counting, Correlation Coefficient |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Append Sort](https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5)| [Python](./Round%201A/append_sort.py) [Python](./Round%201A/append_sort2.py) | _O(N * log(MAX_X))_ | _O(1)_ | Easy | | Greedy |
|B| [Prime Time](https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007543d8)| [Python](./Round%201A/prime_time.py)| _O((MAX_P * logX) * (M + logX))_ | _O(1)_ | Medium | | Math, Prime Factorization, Pruning |
|C| [Hacked Exam](https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/0000000000754750)| [Python](./Round%201A/hacked_exam.py) | precompute: _O(MAX_Q^2)_<br>runtime: _O(Q)_ | _O(MAX_Q^2)_ | Hard | | Binomial Coefficients, DP, Math, Expected Value |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Broken Clock](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694)| [Python](./Round%201B/broken_clock.py) | _O(1)_ | _O(1)_ | Medium | | Math, Linear Congruence |
|B| [Subtransmutation](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae4aa)| [Python](./Round%201B/subtransmutation.py) [Python](./Round%201B/subtransmutation2.py) | _O(MAX_M^2)_ | _O(MAX_M)_ | Medium | | Math, Bézout's Identity, Greedy |
|C| [Digit Blocks](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae37b)| [Python](./Round%201B/digit_blocks.py) | precompute: _O(N^3 * B * D)_<br>runtime: _O(N * B)_ | _O(N^3 * B * D)_ | Hard | | DP, Math, Expected Value |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Closest Pick](https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00)| [Python](./Round%201C/closest_pick.py) | _O(NlogN)_ | _O(N)_ | Easy | | Math, Sort |
|B| [Roaring Years](https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01)| [Python](./Round%201C/roaring_years.py) | _O(D^2 * logD)_ | _O(D)_ | Medium | | Math, Binary Search |
|C| [Double or NOTing](https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139)| [Python](./Round%201C/double_or_noting.py) [Python](./Round%201C/double_or_noting2.py) [Python](./Round%201C/double_or_noting3.py) | _O(\|E\| + \|S\|)_ | _O(\|E\| + \|S\|)_ | Hard | | Math, Bit Manipulation, KMP Algorithm |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Minimum Sort](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc51c)| [Python](./Round%202/minimum_sort.py) | _O(ClogN)_ | _O(1)_ | Easy | | Selection Sort |
|B| [Matrygons](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dbf06)| [Python](./Round%202/matrygons.py) | precompute: _O(NlogN)_<br>runtime: _O(1)_ | _O(N)_ | Medium | | Precompute, DP |
|C| [Hidden Pancakes](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc20c)| [Python](./Round%202/hidden_pancakes.py) [Python](./Round%202/hidden_pancakes2.py) | _O(N)_ | _O(N)_ | Medium | | Math, Binomial Coefficients, DP |
|D| [Retiling](https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc2de)| [Python](./Round%202/retiling.py) | _O((R * C)^3)_ | _O((R * C)^2)_ | Hard | | Weighted Bipartite Matching, Hungarian Algorithm |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Build-A-Pair](https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813aa8)| [PyPy](./Round%203/build_a_pair.py) [PyPy](./Round%203/build_a_pair2.py) [Python](./Round%203/build_a_pair3.py)  | _O(N)_ | _O(1)_ | Easy | | Enumeration, Greedy |
|B| [Square Free](https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1a)| [Python](./Round%203/square_free.py) | _O(R * C)_ | _O(R + C)_ | Medium | | Max Flow, Greedy |
|C| [Fence Design](https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813bc7)| | | | Hard | | |
|D| [Binary Search Game](https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1b)| | | | Hard | | |
