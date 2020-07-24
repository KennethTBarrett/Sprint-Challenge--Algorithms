#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The time complexity of this code block is O(n) - this is because the operation within our while loop is constant and depends on the value of n.


b) This kind of threw me off initially - I thought it would be exponential due to the nested for loops, however, the time complexity of this code block is O(log n) - this is because the complexity decreases over time due to j always being multiplied by 2.


c) The time complexity of this code block would be O(n) - the recursion acts as a loop, decreasing n linearly, where n is the number of bunnies.

## Exercise II

There are two ways to go about this, depending on our use case.
If our primary goal is to simply minimize the number of eggs lost:

For every floor in the building, starting from the first floor,
    If the egg doesn't break on this floor when dropped,
        Make sure that there's another floor to go up to. If there is,
            Go up a floor
        If there isn't another floor to go up to,
            We're going to need another building, because the eggs don't break on any of these floors!
    Otherwise, if the egg does break when we drop it, this floor and all floors above will break the egg.
Now we know what the floor to drop an egg on if we want to break it is!

This would be linear search strategy O(n).

Note: Assuming eggs that did not break can be re-used, this would only take one egg to make our initial determination. One could then verify the results by using a second egg at the floor beneath the floor the egg broke on. If it does not break, and a third egg confirms your floor is accurate, you've used three eggs total, and have sufficient evidence to argue the floor at which an egg breaks. I considered this due to the fact that while thin, we cannot say for sure the full integrity of the egg has been retained after falling.

HOWEVER,
If our goal is to both minimize complexity, AS WELL as minimize the number of eggs lost:

So long as there are more than two floors we are comparing if an egg breaks on,
    Figure out what the middle of the building is by taking the floor number of the bottom floor, adding to the top floor and dividing by two.
        If the egg doesn't break when dropped,
            Go back to the beginning and repeat the process, but with this floor being your bottom floor now.
        If the egg does break when dropped,
            Go back and repeat the process, but with this floor being your new top floor.

Once there are only two floors left, the top one will be the floor at which the egg will break, and the bottom will be the floor at which the egg will not break.

This is a binary search strategy, and it has a complexity of O(log n).
