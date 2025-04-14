/**
 * @param {string} value
 * @return {Object}
 */
var expect = function(value) {
    return {
        toBe : function(val){
            if(val === value){
                return true;
            }
            else{
                throw("Not Equal")
            }
        },
        notToBe : function(val){
            if(val !== value){
                return true
            }
            else{
                throw("Equal")
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */