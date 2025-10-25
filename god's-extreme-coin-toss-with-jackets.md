**Statement of the problem**

God flips a fair coin. If heads, he creates one person with a red jacket. If tails, he creates one person with a red jacket, and a million people with blue jackets. 
* Darkness: God keeps the lights in all the rooms off. You wake up in darkness and can't see your jacket. What should your credence be on heads?

**Solution proposal**

Let us first write down the probabilities that the events of our sample space occur.
* The coin is fair. Therefore $P(H)=P(T)=0.5$.
* If the result of the coin flip is heads, my jacket is sure to be red. Formally, $P(R|H)=1$ (and $P(B|H)=0$).
* If the result of the coin flip is tails, then my jacket is red with probability $\frac{1}{1.000.001}$ and blue with probability $\frac{1.000.000}{1.000.001}$. Formally $P(R|T)=\frac{1}{1.000.001}$ and $P(B|T)=\frac{1.000.000}{1.000.001}$.

This amounts to saying that, with the same probabilty, I could be in one of two worlds:
* A world inhabited by a single person, myself. In that case, my jacket would be red.
* A world inhabited by 1.000.0001 people. In that case, my jacket could be either red or blue.

But does the color really play a role here? After all, the room is dark and I can't see. All I know is that I have a jacket on.  
What I can do is to compute $P(H|J)$, i.e. the probability that God flips heads *given the fact* that I have a jacket on.
```math
P(H|J)=\frac{P(J|H)P(H)}{P(J)}=\frac{1 \times 1/2}{1}=1/2
```
Since no information on the color is available, my estimate coincides with the probability of getting heads. 
