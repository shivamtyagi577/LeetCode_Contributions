/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let temp = 0;
    for(let i in args){
        if(i){
            temp = temp + 1;
        }
    }
    return temp;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */