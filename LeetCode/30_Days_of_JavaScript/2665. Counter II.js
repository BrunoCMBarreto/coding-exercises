// 2665. Counter II
// Solved
// Easy
// Companies
// Hint
// Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.

// The three functions are:

// increment() increases the current value by 1 and then returns it.
// decrement() reduces the current value by 1 and then returns it.
// reset() sets the current value to init and then returns it.

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    return {
        initial_count: init,
        current_count: init,
        increment: function() {
            this.current_count += 1
            return this.current_count
        },
        decrement: function() {
            this.current_count -= 1
            return this.current_count
        },
        reset: function() {
            this.current_count = this.initial_count
            return this.current_count
        }

    }
};