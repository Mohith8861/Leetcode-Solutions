// https://leetcode.com/problems/counter-ii

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  let i = init
  return {
    increment()  {
          return i+=1;
      },
    reset()  {
          i = init
          return i;
      },
    decrement() {
          return i-=1;
      }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */