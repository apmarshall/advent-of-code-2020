# Report Repair

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. 

## Brute Force Approach:

    // List of Numbers -> Number 
    // Given a list of nubmers, find the two numbers that add up to 2020, then return the product of those two numbers
    foreach number in list:
        try num[i] + all other numbers in list
            if == 2020, return num[i] * num[x] 
            
This approach will find the solution, but it will rapidly expand at a rate of n^n. That's bad.

## Optimization:

One approach we could take is to look for the compliment we need for a given number. So to use the example given: the first number on the list is 1721. 2020 - 1721 = 299. So now we just need to check if 299 is on the list. If it is, solved. If not, move on.

We can further optimize this by only searching the rest of the list for possible answers. This is because addition works no matter what order you do it in. So to continue using the example: if 299 wasn't in the list and we moved on to 979 (so now looking for 1041), we know that our `x` is not earlier in the list or we would have already found it's compliment. So we only need to search later items in the list. This approach is going to look more like this:

    // List of Numbers -> Number
    // Given a list of numbers, find the two numbers that add up to 2020, then reutnr the product of those two numbers
    if len(list) == 0:
        return NaN
    else:
        if (2020 - list[0] is in list):
            return list[0] * (2020 - list[0])
        else:
            recurse over rest of list // base-shift list[1] to list[0]
            
In this worst case scenario, our two compliments would be the last two items in the input list. Then we would effectively have gone through the entire list before finding them. However, given the shortening we're doing with each run, we'll actually end up with an expansion closer to (n/2)^2 or O(n^2). That's significantly better than the brute force, but not ideal for a long list. We could probably add some additional minimal optimizations: things like `if list[0] >= 2020, skip it`. That would shave a small amount of time off each run, but not be particularly significant in the grand scheme of things. Another possibility is that we could sort the input and then do comparisons from both ends. Here's how that might look on the example given:

    299
    366
    675
    979
    1456
    1721
    
Then, we could take the first item, compare it to the last item, and drop items off the end of the list until they were smaller than `2020 - list[0]`, after which we would drop the first item as well and restart with our shortened list (with the first item lopped off the front and everything greater than its needed complement lopped off the end). This would probably find the solution faster except in cases where the solution was the very middle of the list. If we assume our sort stage has an log(n) expansion rate, then the primary load of this algorithm is still the search, which will, in the worst case, expand at a rate of n/2, or O(n). That's the best we've had so far. Here's how we might do this in pseudocode:

    define: reportRepair(list)
        sort(list)
        if len(list) == 0:
            return NaN
        else:
            t = 2020 - list[0]
            if list[-1] = t
               return list[0] * list[-1]
            elseif (list[-1 > t]):
                reportRepair(list[:-2])
            else: 
                reportReapir(list[1:])
