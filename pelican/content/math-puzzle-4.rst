Math puzzle
###########
:date: 2012-12-04 21:48
:author: nasser
:category: Math, Programming
:slug: math-puzzle-4

| Yesterday, I was asked to solve a math puzzle that goes like this:
|  You have a 3x3 matrix where you have to fill it with the numbers 1-9,
 as follows:

+------+------+------+
| N1   | N2   | N3   |
+------+------+------+
| N4   | N5   | N6   |
+------+------+------+
| N7   | N8   | N9   |
+------+------+------+

| Where,
|  N1 + N4 = N7 and
|  N2 + N5 = N8 and
|  N3 + N6 = N9
|  and no repetition is allowed!
|  So I spent sometime trying to solve it. Then I wrote a little Python
script to help me solve it, but it too didn't work. It was a bit
frustrating, to be honest, so I thought about it differently. We know
that an Even number + another Even number will yield an Even number. and
an Odd number + an Odd number will also yield an Even number. The only
case where we can get an Odd number is when we add an Even number with
an Odd number. Let me state these in a clear way.
|  **\* O + O = E
 \* E + E = E
 \* O + E = O**
|  So I counted the Odds and Evens in the list, which are:
|  1 -- O
|  2 -- E
|  3 -- O
|  4 -- E
|  5 -- O
|  6 -- E
|  7 -- O
|  8 -- E
|  9 -- O
|  **\* 5 Odds**
|  **\* 4 Evens**
|  Now, no matter how you arrange the first two rows of the matrix, you
can't come up with a formation that will satisfy these constraints :)
|  Here are some illustrations:

+-----+-----+-----+
| O   | O   | O   |
+-----+-----+-----+
| O   | O   | E   |
+-----+-----+-----+
| E   | E   | O   |
+-----+-----+-----+

An Even number remains.

+-----+-----+-----+
| O   | O   | O   |
+-----+-----+-----+
| O   | E   | E   |
+-----+-----+-----+
| E   | O   | O   |
+-----+-----+-----+

An Even number remains.

+-----+-----+-----+
| O   | O   | O   |
+-----+-----+-----+
| E   | E   | E   |
+-----+-----+-----+
| O   | O   | O   |
+-----+-----+-----+

An Even number remains.

+-----+-----+-----+
| E   | O   | O   |
+-----+-----+-----+
| E   | E   | O   |
+-----+-----+-----+
| E   | O   | E   |
+-----+-----+-----+

An Odd number remains.

+-----+-----+-----+
| E   | E   | O   |
+-----+-----+-----+
| E   | O   | O   |
+-----+-----+-----+
| E   | O   | E   |
+-----+-----+-----+

| An Odd number remains.
|  etc...
|  Thus! (I've always liked to say THUS! :D) no solution is valid!
|  and this is the Python script that I wrote:

.. code:: brush:

    from itertools import product

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    pro = [ x for x in product(x, repeat=3)]

    def matSum(c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])

    def check(x, y, z):
        if len(set(x + y + z)) == 9:
            return x, y, z

    for i in pro:
        for j in pro:
            s = matSum(i, j)
            print check(i, j, s)

So, my dear reader, if you see any flaw in my mathematical reasoning,
please let me know in the comment section below. Thanks!
