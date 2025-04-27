// 2704. To Be Or Not To Be
// Solved
// Easy
// Companies
// Write a function expect that helps developers test their code. It should take in any value val and return an object with the following two functions.

// toBe(val) accepts another value and returns true if the two values === each other. If they are not equal, it should throw an error "Not Equal".
// notToBe(val) accepts another value and returns true if the two values !== each other. If they are equal, it should throw an error "Equal".

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        value: val,
        toBe: function(val) {
            if (this.value === val) {
                return true
            } else {
                throw "Not Equal"
            }
        },
        notToBe: function(val) {
            if (this.value !== val) {
                return true
            } else {
                throw "Equal"
            }
        }
    }
};