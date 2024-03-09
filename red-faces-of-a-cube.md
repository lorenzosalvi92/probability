**Statement of the problem**

The outside of an n $\times$ n $\times$ n cube is painted red. The cube then is chopped into $n^3$ unit cubes. The latter are thoroughly mixed up and put into a bag. One small cube is withdrawn at random from the bag and tossed acrossed the table. What is the probability that the cube stops with the red face on top? (source: https://www.cut-the-knot.org/Probability/RedFaces.shtml)

**Solution**

For $n=1$, all the faces are red. The sought probabilty is therefore 1.
For $n>1$, the $n^3$ unit cubes have can have a different number of red faces. Let us list all the possible cases:
* 0 unit cube have **between 4 and 6 painted faces**.
* 8 unit cubes have **3 painted faces**. Those are the unit cubes placed at the 8 vertices of the big cube.
* $12(n-2)$ unit cubes have **2 painted faces**. Those are the unit cubes that build the edges of the big cube, excluding the unit cubes at the vertices.
* $6(n-2)^2$ unit cubes have **1 painted face**. Those are the unit cubes that build the faces of the big cubes, excluding the unit cubes building the edges and the ones at the vertices.
* $(n-2)^3$ unit cubes have **0 painted faces**. Those are the inner unit cubes.

Let us make an example for $n=3$.
* 0 unit cubes have between 4 and 6 painted faces.
* 8 unit cubes have 3 painted faces.
* $12(3-2)=12$ unit cubes have 2 painted faces.
* $6(3-2)^2=6$ unit cubes have 1 painted face.
* $(3-2)^3=1$ unit cube has 0 painted faces.

In total we then have $0+8+12+6+1=27$ unit cubes - which makes total sense, given that $3^3=27$.

Now let us find it what the sought probability is.\\
The first step is finding out what the probabilty of drawing a unit cube with $j$ painted faces is. This can be expressed as follows: (Number of unit cubes with j red faces)/(Total number of unit cubes).
For the different cases we have:
* (Number of unit cubes with between 4 and 6 red faces)/(Total number of unit cubes)= $\frac{0}{n^3}=0$
* (Number of unit cubes with 3 red faces)/(Total number of unit cubes)= $\frac{8}{n^3}$
* (Number of unit cubes with 2 red faces)/(Total number of unit cubes)= $\frac{12(n-2)}{n^3}$
* (Number of unit cubes with 1 red face)/(Total number of unit cubes)= $\frac{6(n-2)^2}{n^3}$
* (Number of unit cubes with 0 red faces)/(Total number of unit cubes)= $\frac{(n-2)^3}{n^3}$

The second step is finding the probability of the drawn unit cube stopping with the red faces on top *given* that this unit cube has $j$ red faces.
* Probability of the drawn unit cube stopping with the red face on top given that this unit cube has 3 red faces = $1/2$
* Probability of the drawn unit cube stopping with the red face on top given that this unit cube has 2 red faces = $1/3$
* Probability of the drawn unit cube stopping with the red face on top given that this unit cube has 1 red faces = $1/6$
* Probability of the drawn unit cube stopping with the red face on top given that this unit cube has 0 red faces = $0$

We now have all the elements to answer the question.\\
The probability that the unit cube that has been drawn from the bag and tossed across the table stops with the red face on top is 
```math
\frac{8}{n^3}\frac{1}{2}+\frac{12(n-2)}{n^3}\frac{1}{3}+\frac{6(n-2)^2}{n^3}\frac{1}{6}+\frac{(n-2)^3}{n^3}\frac{0}{6} = \frac{4}{n^3}+\frac{4(n-2)}{n^3}+\frac{(n-2)^2}{n^3}=\frac{4+4n-8+n^2+4-4n}{n^3}=\frac{n^2}{n^3}=\frac{1}{n}
```


