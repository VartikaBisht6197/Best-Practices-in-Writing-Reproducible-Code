# Best Practices in Writing Reproducible Code
Ensuring your research is reproducible can be a difficult task. Scripting your analysis is a start, but this in and of itself is no guarantee that you, or someone else, can faithfully repeat your work at a later stage. In this workshop, we will help you not only to make your work reproducible, but also to increase the efficiency of your workflow. We do this by teaching you a few good programming habits: how to set up a good project structure, how to code and comment well, and how to document your code so that it can be used by others. We will furthermore introduce you to Git and GitHub, which are essential tools in managing and publishing code. Reproducibility requires extra effort, but we will focus on teaching you skills that will save you much more time in the long run than they cost to implement.<br />

Mor information about the workshop can be found on : https://www.uu.nl/en/research/research-data-management/training-workshops/best-practices-for-writing-reproducible-code

## Hidden Markov models example
Hidden Markov models (HMMs) are a formal foundation for making probabilistic models of linear sequence 'labeling' problems. They provide a conceptual toolkit for building complex models just by drawing an intuitive picture. They are at the heart of a diverse range of programs, including genefinding, profile searches, multiple sequence alignment and regulatory site identification. HMMs are the Legos of computational sequence analysis. <br />
 <br />
A hidden Markov model (HMM) is a probabilistic model of a multiple sequence alignment (msa) of proteins. In the model, each column of symbols in the alignment is represented by a frequency distribution of the symbols (called a "state"), and insertions and deletions are represented by other states. One moves through the model along a particular path from state to state in a Markov chain (i.e., random choice of next move), trying to match a given sequence. The next matching symbol is chosen from each state, recording its probability (frequency) and also the probability of going to that state from a previous one (the transition probability). State and transition probabilities are multiplied to obtain a probability of the given sequence. The hidden nature of the HMM is due to the lack of information about the value of a specific state, which is instead represented by a probability distribution over all possible values. This article discusses the advantages and disadvantages of HMMs in msa and presents algorithms for calculating an HMM and the conditions for producing the best HMM.

![687474703a2f2f6373652d77696b692e756e6c2e6564752f77696b692f696d616765732f652f65662f50726f66696c65484d4d2e676966](https://user-images.githubusercontent.com/53393505/119949430-7eab2d80-bfb7-11eb-9d76-0355b14e91bd.gif)


## LICENSE
<p align="center">
                                                     GNU GENERAL PUBLIC LICENSE<br/ >
                                                       Version 3, 29 June 2007<br/ >
 </p>
<p align="center">
 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/><br />
 Everyone is permitted to copy and distribute verbatim copies<br />
 of this license document, but changing it is not allowed.<br />
 </p>
