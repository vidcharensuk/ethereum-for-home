pragma solidity >=0.4.0 <0.7.0;

contract ledswitch {
    bool switchValue;
    function getSwitch() public view returns (bool){
        return switchValue;
    }
    function setSwitch(bool value) public{
        switchValue = value;
    }
}