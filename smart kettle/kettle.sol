pragma solidity >=0.4.0 <0.7.0;

contract ledswitch {
    uint temp;//temperature value
    uint limit;//upper limit value
    uint power;//set power value

    event overlimit(uint temp);

    //Store current temperature of kettle
    function storeTemp(uint t) public{
        temp = t;
        if(temp >= limit){
            emit overlimit(temp);
        }
    }
    //Set upper limit to heat water
    function setLimit(uint k) public{
        limit = k;
    }

    //Set power switch
    function setPower(uint p) public{
        power = p;
    }

    //Obtain current power switch command
    function getPower() public view returns(uint){
        return power;
    }

}