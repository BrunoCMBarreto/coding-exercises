// 2620. Counter
// Solved
// Easy
// Companies
// Hint
// Given an integer n, return a counter function. This counter function initially returns n and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    count = -1;
    return function() {
        count += 1;
        return n + count;
    };
};