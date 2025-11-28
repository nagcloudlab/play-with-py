
// cjs / esm 


// const counter=(function init() {
    count = 0 
    function increment() {
    count += 1
    console.log(`Count is now: ${count}`)
    }

    function decrement() {
    count -= 1
    console.log(`Count is now: ${count}`)
    }

    function getCount() {
    return count
    }
    return {
    increment,
    decrement,
    getCount
    }
// })()

// counter=init()

