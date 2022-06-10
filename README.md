# algo-lab3-hamsters

The pet store sells hamsters. These are notable domestic creatures, however, it was that they have interesting eating behavior.

To feed a hamster alone, you need H food packets per product. However, if several hamsters live together, they wake up greedy. In this case, each hamster eats an extra G packet of food for each neighbor. The daily norm of H and greed of G are individual for each hamster.

There are only C hamsters in the store. You want to buy as much as you can, but you don't have food packages for the day. Determine the maximum number of hamsters you can feed.

Entrance stations
The input file hamster_in.txt consists of C + 2 lines.

The first line contains S - a good supply of food. 0 ≤ S ≤ 10 ^ 9
The second line contains C - the total number of hamsters on sale. 1 ≤ C ≤ 10 ^ 5
The next C lines contain H, G are integers separated by a space, which means the daily norm and the level of greed of each hamster. 0 ≤ H, G ≤ 10 ^ 9
Weekend place
The original hamster_out.txt file has one number - the maximum number of hamsters that can be fed together.